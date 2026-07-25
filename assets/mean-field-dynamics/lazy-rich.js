/* Lazy vs feature-learning training widget for "Mean-Field Dynamics Explained".
 *
 * Trains a two-layer tanh network f(x) = (alpha/N) * sum_i v_i tanh(w_i x + b_i)
 * live in the browser by full-batch gradient descent, with the step size
 * compensated by 1/alpha^2 (Chizat-Oyallon-Bach). The slider sets the output
 * scale alpha: alpha ~ 1 is the rich / mean-field regime (particles migrate),
 * large alpha is the lazy regime (fit converges, particles freeze).
 *
 * Zero dependencies. The simulation core is DOM-free so it can be smoke-tested
 * in Node: `node -e "const m = require('./lazy-rich.js'); ..."`.
 */
(function () {
  'use strict';

  /* ---------------- simulation core (no DOM) ---------------- */

  function mulberry32(seed) {
    var a = seed >>> 0;
    return function () {
      a |= 0; a = (a + 0x6D2B79F5) | 0;
      var t = Math.imul(a ^ (a >>> 15), 1 | a);
      t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }

  function makeRandn(rng) {
    return function () {
      var u = 0, v = 0;
      while (u === 0) u = rng();
      while (v === 0) v = rng();
      return Math.sqrt(-2.0 * Math.log(u)) * Math.cos(2.0 * Math.PI * v);
    };
  }

  // Teacher: three tanh units with kinks at x = -1.5, 0.2, 2.0.
  var TEACHER = [
    { W: 2.0, B: 3.0, V: 1.2 },
    { W: 2.5, B: -0.5, V: -1.4 },
    { W: 1.5, B: -3.0, V: 0.8 }
  ];

  function teacherY(x) {
    var y = 0;
    for (var k = 0; k < TEACHER.length; k++) {
      y += TEACHER[k].V * Math.tanh(TEACHER[k].W * x + TEACHER[k].B);
    }
    return y;
  }

  function makeData(nPoints) {
    var xs = new Float64Array(nPoints), ys = new Float64Array(nPoints);
    for (var j = 0; j < nPoints; j++) {
      var x = -3 + 6 * j / (nPoints - 1);
      xs[j] = x;
      ys[j] = teacherY(x);
    }
    return { xs: xs, ys: ys, n: nPoints };
  }

  // Symmetrized init (v-pairs with opposite signs) so f == 0 at init for any alpha.
  function createNet(N, seed) {
    var randn = makeRandn(mulberry32(seed));
    var w = new Float64Array(N), b = new Float64Array(N), v = new Float64Array(N);
    var half = N / 2;
    for (var i = 0; i < half; i++) {
      var wi = randn() * 1.0, bi = randn() * 1.0, vi = randn() * 1.0;
      w[i] = wi; b[i] = bi; v[i] = vi;
      w[i + half] = wi; b[i + half] = bi; v[i + half] = -vi;
    }
    return {
      N: N, w: w, b: b, v: v,
      w0: w.slice(), b0: b.slice(), v0: v.slice(),
      steps: 0
    };
  }

  function resetToInit(net) {
    net.w = net.w0.slice(); net.b = net.b0.slice(); net.v = net.v0.slice();
    net.steps = 0;
  }

  function netForward(net, alpha, x) {
    var s = 0;
    for (var i = 0; i < net.N; i++) {
      s += net.v[i] * Math.tanh(net.w[i] * x + net.b[i]);
    }
    return alpha * s / net.N;
  }

  // One full-batch GD step. Effective step size eta0 * N / alpha^2:
  // the N-scaling is the mean-field convention (O(1) particle velocity),
  // the 1/alpha^2 keeps the function-space dynamics comparable across alpha.
  function trainStep(net, alpha, eta0, data) {
    var N = net.N, n = data.n;
    var res = new Float64Array(n);
    var tanhCache = new Float64Array(N * n);
    var j, i, x, s, t;
    for (j = 0; j < n; j++) {
      x = data.xs[j]; s = 0;
      for (i = 0; i < N; i++) {
        t = Math.tanh(net.w[i] * x + net.b[i]);
        tanhCache[i * n + j] = t;
        s += net.v[i] * t;
      }
      res[j] = alpha * s / N - data.ys[j];
    }
    var lr = eta0 * N / (alpha * alpha);
    var scale = alpha / (N * n);
    for (i = 0; i < N; i++) {
      var gw = 0, gb = 0, gv = 0;
      for (j = 0; j < n; j++) {
        t = tanhCache[i * n + j];
        var dsig = (1 - t * t) * res[j];
        gv += t * res[j];
        gw += net.v[i] * dsig * data.xs[j];
        gb += net.v[i] * dsig;
      }
      net.w[i] -= lr * scale * gw;
      net.b[i] -= lr * scale * gb;
      net.v[i] -= lr * scale * gv;
    }
    net.steps++;
  }

  function loss(net, alpha, data) {
    var s = 0;
    for (var j = 0; j < data.n; j++) {
      var r = netForward(net, alpha, data.xs[j]) - data.ys[j];
      s += r * r;
    }
    return 0.5 * s / data.n;
  }

  // Mean distance travelled by the particles theta_i = (w_i, b_i, v_i) since init.
  function meanDisplacement(net) {
    var s = 0;
    for (var i = 0; i < net.N; i++) {
      var dw = net.w[i] - net.w0[i], db = net.b[i] - net.b0[i], dv = net.v[i] - net.v0[i];
      s += Math.sqrt(dw * dw + db * db + dv * dv);
    }
    return s / net.N;
  }

  var core = {
    createNet: createNet, resetToInit: resetToInit, netForward: netForward,
    trainStep: trainStep, loss: loss, meanDisplacement: meanDisplacement,
    makeData: makeData, teacherY: teacherY
  };

  if (typeof module !== 'undefined' && module.exports) module.exports = core;
  if (typeof document === 'undefined') return;

  /* ---------------- UI ---------------- */

  var N_NEURONS = 64;
  var N_DATA = 64;
  var ETA0 = 0.1;
  var STEPS_PER_FRAME = 8;
  var MAX_STEPS = 4000;
  var INITIAL_SEED = 42;

  var COL = {
    fit: '#2a7ae2', particle: '#2a7ae2', ghost: '#b9cfee',
    target: '#555', axis: '#dddddd', text: '#888888'
  };

  function injectStyle() {
    if (document.getElementById('mfw-style')) return;
    var css = [
      '.mfw{font:13px/1.45 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;',
      'color:#333;border:1px solid #e5e5e5;border-radius:6px;padding:14px;margin:1.2em 0;background:#fff}',
      '.mfw-row{display:flex;gap:14px;flex-wrap:wrap}',
      '.mfw-panel{flex:1 1 260px;min-width:240px}',
      '.mfw-title{font-size:12px;color:#888;text-align:center;margin:0 0 4px 0}',
      '.mfw canvas{width:100%;height:auto;display:block}',
      '.mfw-controls{display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin-top:10px}',
      '.mfw-controls input[type=range]{flex:1 1 140px;min-width:120px;accent-color:#2a7ae2}',
      '.mfw-btn{font:inherit;padding:3px 12px;border:1px solid #ccc;border-radius:4px;background:#fafafa;cursor:pointer}',
      '.mfw-btn:hover{background:#f0f0f0}',
      '.mfw-readout{font-variant-numeric:tabular-nums;color:#666;white-space:nowrap}',
      '.mfw-slider-label{color:#666;white-space:nowrap}',
      '.mfw-ends{display:flex;justify-content:space-between;font-size:11px;color:#999;margin-top:-4px}'
    ].join('');
    var style = document.createElement('style');
    style.id = 'mfw-style';
    style.textContent = css;
    document.head.appendChild(style);
  }

  function setupCanvas(canvas, cssWidth, cssHeight) {
    var dpr = window.devicePixelRatio || 1;
    canvas.width = Math.round(cssWidth * dpr);
    canvas.height = Math.round(cssHeight * dpr);
    canvas.style.width = '100%';
    var ctx = canvas.getContext('2d');
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    return ctx;
  }

  function makeMapper(xmin, xmax, ymin, ymax, w, h, pad) {
    return {
      x: function (x) { return pad + (x - xmin) / (xmax - xmin) * (w - 2 * pad); },
      y: function (y) { return h - pad - (y - ymin) / (ymax - ymin) * (h - 2 * pad); }
    };
  }

  function drawFrame(ctx, m, w, h, xmin, xmax, ymin, ymax) {
    ctx.clearRect(0, 0, w, h);
    ctx.strokeStyle = COL.axis;
    ctx.lineWidth = 1;
    ctx.strokeRect(m.x(xmin), m.y(ymax), m.x(xmax) - m.x(xmin), m.y(ymin) - m.y(ymax));
    ctx.beginPath();
    ctx.moveTo(m.x(xmin), m.y(0)); ctx.lineTo(m.x(xmax), m.y(0));
    ctx.moveTo(m.x(0), m.y(ymin)); ctx.lineTo(m.x(0), m.y(ymax));
    ctx.stroke();
  }

  function init() {
    var root = document.getElementById('lazy-rich-widget');
    if (!root) return;
    injectStyle();
    root.className = 'mfw';
    root.innerHTML =
      '<div class="mfw-row">' +
      '  <div class="mfw-panel"><p class="mfw-title">function fit</p><canvas></canvas></div>' +
      '  <div class="mfw-panel"><p class="mfw-title">neurons as particles (w<sub>i</sub>, v<sub>i</sub>)</p><canvas></canvas></div>' +
      '</div>' +
      '<div class="mfw-controls">' +
      '  <span class="mfw-slider-label">output scale &alpha; = <b class="mfw-alpha">1</b></span>' +
      '  <input type="range" min="0" max="14" step="1" value="0" aria-label="output scale alpha">' +
      '  <button class="mfw-btn mfw-play">Pause</button>' +
      '  <button class="mfw-btn mfw-restart">Restart</button>' +
      '</div>' +
      '<div class="mfw-ends"><span>&larr; rich (mean-field)</span><span>lazy (NTK) &rarr;</span></div>' +
      '<div class="mfw-controls">' +
      '  <span class="mfw-readout mfw-stats"></span>' +
      '</div>';

    var canvases = root.getElementsByTagName('canvas');
    var CW = 340, CH = 235;
    var ctxFit = setupCanvas(canvases[0], CW, CH);
    var ctxPar = setupCanvas(canvases[1], CW, CH);
    var mFit = makeMapper(-3, 3, -2.6, 2.6, CW, CH, 10);
    var mPar = makeMapper(-4, 4, -6.5, 6.5, CW, CH, 10);

    var slider = root.querySelector('input[type=range]');
    var alphaLabel = root.querySelector('.mfw-alpha');
    var playBtn = root.querySelector('.mfw-play');
    var restartBtn = root.querySelector('.mfw-restart');
    var stats = root.querySelector('.mfw-stats');

    var data = makeData(N_DATA);
    var seed = INITIAL_SEED;
    var net = createNet(N_NEURONS, seed);
    var alpha = 1;
    var running = true;

    function sliderAlpha() {
      // 15 positions, alpha = 2^(k/2): 1, 1.4, 2, 2.8, 4, ..., 128
      var a = Math.pow(2, slider.valueAsNumber / 2);
      return a >= 4 ? Math.round(a) : Math.round(a * 10) / 10;
    }

    function drawFit() {
      drawFrame(ctxFit, mFit, CW, CH, -3, 3, -2.6, 2.6);
      var j, x;
      ctxFit.strokeStyle = COL.target;
      ctxFit.setLineDash([5, 4]);
      ctxFit.lineWidth = 1.4;
      ctxFit.beginPath();
      for (j = 0; j <= 120; j++) {
        x = -3 + 6 * j / 120;
        var yT = teacherY(x);
        if (j === 0) ctxFit.moveTo(mFit.x(x), mFit.y(yT)); else ctxFit.lineTo(mFit.x(x), mFit.y(yT));
      }
      ctxFit.stroke();
      ctxFit.setLineDash([]);
      ctxFit.strokeStyle = COL.fit;
      ctxFit.lineWidth = 2;
      ctxFit.beginPath();
      for (j = 0; j <= 120; j++) {
        x = -3 + 6 * j / 120;
        var yF = Math.max(-2.55, Math.min(2.55, netForward(net, alpha, x)));
        if (j === 0) ctxFit.moveTo(mFit.x(x), mFit.y(yF)); else ctxFit.lineTo(mFit.x(x), mFit.y(yF));
      }
      ctxFit.stroke();
      ctxFit.fillStyle = COL.text;
      ctxFit.font = '11px sans-serif';
      ctxFit.fillText('target (dashed) vs network', 16, 16);
    }

    function drawParticles() {
      drawFrame(ctxPar, mPar, CW, CH, -4, 4, -3.2, 3.2);
      var clampW = function (w) { return Math.max(-3.95, Math.min(3.95, w)); };
      var clampV = function (v) { return Math.max(-6.4, Math.min(6.4, v)); };
      var i;
      ctxPar.strokeStyle = COL.ghost;
      ctxPar.lineWidth = 1;
      for (i = 0; i < net.N; i++) {
        ctxPar.beginPath();
        ctxPar.moveTo(mPar.x(clampW(net.w0[i])), mPar.y(clampV(net.v0[i])));
        ctxPar.lineTo(mPar.x(clampW(net.w[i])), mPar.y(clampV(net.v[i])));
        ctxPar.stroke();
      }
      for (i = 0; i < net.N; i++) {
        ctxPar.beginPath();
        ctxPar.arc(mPar.x(clampW(net.w0[i])), mPar.y(clampV(net.v0[i])), 2.4, 0, 2 * Math.PI);
        ctxPar.strokeStyle = COL.ghost;
        ctxPar.stroke();
      }
      ctxPar.fillStyle = COL.particle;
      ctxPar.globalAlpha = 0.75;
      for (i = 0; i < net.N; i++) {
        ctxPar.beginPath();
        ctxPar.arc(mPar.x(clampW(net.w[i])), mPar.y(clampV(net.v[i])), 2.8, 0, 2 * Math.PI);
        ctxPar.fill();
      }
      ctxPar.globalAlpha = 1;
      ctxPar.fillStyle = COL.text;
      ctxPar.font = '11px sans-serif';
      ctxPar.fillText('open circles: initialization', 16, 16);
    }

    function updateStats() {
      stats.textContent =
        'step ' + net.steps +
        '   |   loss ' + loss(net, alpha, data).toExponential(2) +
        '   |   mean particle displacement ' + meanDisplacement(net).toFixed(3);
    }

    function redraw() {
      drawFit();
      drawParticles();
      updateStats();
    }

    function frame() {
      if (running && net.steps < MAX_STEPS) {
        for (var s = 0; s < STEPS_PER_FRAME; s++) trainStep(net, alpha, ETA0, data);
        redraw();
      }
      requestAnimationFrame(frame);
    }

    slider.addEventListener('input', function () {
      alpha = sliderAlpha();
      alphaLabel.textContent = String(alpha);
      resetToInit(net); // same initialization, new scale: apples-to-apples
      redraw();
    });
    playBtn.addEventListener('click', function () {
      running = !running;
      playBtn.textContent = running ? 'Pause' : 'Play';
    });
    restartBtn.addEventListener('click', function () {
      seed = (Math.random() * 1e9) >>> 0;
      net = createNet(N_NEURONS, seed);
      redraw();
    });

    alphaLabel.textContent = String(alpha);
    redraw();
    requestAnimationFrame(frame);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
