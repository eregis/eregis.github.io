/* Law-of-large-numbers widget for "Mean-Field Dynamics Explained".
 *
 * Trains TWO two-layer tanh networks in the mean-field parametrization
 * f(x) = (1/N) * sum_i v_i tanh(w_i x + b_i) -- same architecture, same data,
 * different random seeds -- live in the browser by full-batch gradient descent
 * with the width-scaled step size (eta = eta0 * N). A slider sets the width N.
 * At small N the two particle clouds and fits evolve visibly differently; at
 * large N they collapse onto the same deterministic flow.
 *
 * Zero dependencies. The simulation core is DOM-free so it can be smoke-tested
 * in Node: `node -e "const m = require('./lln-width.js'); ..."`.
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

  // Same teacher as the lazy-rich widget: kinks at x = -1.5, 0.2, 2.0.
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

  // i.i.d. Gaussian init: neurons are samples from the same base measure mu_0,
  // so different seeds are different empirical draws of the SAME initial law.
  function createNet(N, seed) {
    var randn = makeRandn(mulberry32(seed));
    var w = new Float64Array(N), b = new Float64Array(N), v = new Float64Array(N);
    for (var i = 0; i < N; i++) {
      w[i] = randn(); b[i] = randn(); v[i] = randn();
    }
    return { N: N, w: w, b: b, v: v, steps: 0 };
  }

  function netForward(net, x) {
    var s = 0;
    for (var i = 0; i < net.N; i++) {
      s += net.v[i] * Math.tanh(net.w[i] * x + net.b[i]);
    }
    return s / net.N;
  }

  // One full-batch GD step in the mean-field convention: step size eta0 * N,
  // so each particle moves at O(1) speed regardless of the width.
  function trainStep(net, eta0, data) {
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
      res[j] = s / N - data.ys[j];
    }
    var lr = eta0 * N;
    var scale = 1 / (N * n);
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

  function loss(net, data) {
    var s = 0;
    for (var j = 0; j < data.n; j++) {
      var r = netForward(net, data.xs[j]) - data.ys[j];
      s += r * r;
    }
    return 0.5 * s / data.n;
  }

  // RMS gap between the two networks' outputs: the visible face of the LLN.
  function seedGap(netA, netB, data) {
    var s = 0;
    for (var j = 0; j < data.n; j++) {
      var d = netForward(netA, data.xs[j]) - netForward(netB, data.xs[j]);
      s += d * d;
    }
    return Math.sqrt(s / data.n);
  }

  var core = {
    createNet: createNet, netForward: netForward, trainStep: trainStep,
    loss: loss, seedGap: seedGap, makeData: makeData, teacherY: teacherY
  };

  if (typeof module !== 'undefined' && module.exports) module.exports = core;
  if (typeof document === 'undefined') return;

  /* ---------------- UI ---------------- */

  var N_DATA = 64;
  var ETA0 = 0.1;
  var STEPS_PER_FRAME = 6;
  var MAX_STEPS = 4000;
  var SEED_A = 42, SEED_B = 1337;

  var COL = {
    a: '#2a7ae2', b: '#e2762a',
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
    var root = document.getElementById('lln-widget');
    if (!root) return;
    injectStyle();
    root.className = 'mfw';
    root.innerHTML =
      '<div class="mfw-row">' +
      '  <div class="mfw-panel"><p class="mfw-title">two fits, two seeds</p><canvas></canvas></div>' +
      '  <div class="mfw-panel"><p class="mfw-title">two particle clouds (w<sub>i</sub>, v<sub>i</sub>)</p><canvas></canvas></div>' +
      '</div>' +
      '<div class="mfw-controls">' +
      '  <span class="mfw-slider-label">width N = <b class="mfw-n">8</b></span>' +
      '  <input type="range" min="3" max="9" step="1" value="3" aria-label="network width N">' +
      '  <button class="mfw-btn mfw-play">Pause</button>' +
      '  <button class="mfw-btn mfw-restart">Restart</button>' +
      '</div>' +
      '<div class="mfw-ends"><span>&larr; few particles: luck matters</span><span>many particles: deterministic &rarr;</span></div>' +
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
    var nLabel = root.querySelector('.mfw-n');
    var playBtn = root.querySelector('.mfw-play');
    var restartBtn = root.querySelector('.mfw-restart');
    var stats = root.querySelector('.mfw-stats');

    var data = makeData(N_DATA);
    var seedA = SEED_A, seedB = SEED_B;
    var N = 8;
    var netA = createNet(N, seedA);
    var netB = createNet(N, seedB);
    var running = true;

    function rebuild() {
      netA = createNet(N, seedA);
      netB = createNet(N, seedB);
    }

    function drawCurve(ctx, m, f, color, dash, width) {
      ctx.strokeStyle = color;
      ctx.setLineDash(dash);
      ctx.lineWidth = width;
      ctx.beginPath();
      for (var j = 0; j <= 120; j++) {
        var x = -3 + 6 * j / 120;
        var y = Math.max(-2.55, Math.min(2.55, f(x)));
        if (j === 0) ctx.moveTo(m.x(x), m.y(y)); else ctx.lineTo(m.x(x), m.y(y));
      }
      ctx.stroke();
      ctx.setLineDash([]);
    }

    function drawFits() {
      drawFrame(ctxFit, mFit, CW, CH, -3, 3, -2.6, 2.6);
      drawCurve(ctxFit, mFit, teacherY, COL.target, [5, 4], 1.4);
      drawCurve(ctxFit, mFit, function (x) { return netForward(netA, x); }, COL.a, [], 2);
      drawCurve(ctxFit, mFit, function (x) { return netForward(netB, x); }, COL.b, [], 2);
      ctxFit.fillStyle = COL.text;
      ctxFit.font = '11px sans-serif';
      ctxFit.fillText('target dashed; seeds in blue and orange', 16, 16);
    }

    function drawCloud(ctx, m, net, color) {
      var clampW = function (w) { return Math.max(-3.95, Math.min(3.95, w)); };
      var clampV = function (v) { return Math.max(-6.4, Math.min(6.4, v)); };
      ctx.fillStyle = color;
      ctx.globalAlpha = 0.55;
      for (var i = 0; i < net.N; i++) {
        ctx.beginPath();
        ctx.arc(m.x(clampW(net.w[i])), m.y(clampV(net.v[i])), 2.6, 0, 2 * Math.PI);
        ctx.fill();
      }
      ctx.globalAlpha = 1;
    }

    function drawParticles() {
      drawFrame(ctxPar, mPar, CW, CH, -4, 4, -3.2, 3.2);
      drawCloud(ctxPar, mPar, netA, COL.a);
      drawCloud(ctxPar, mPar, netB, COL.b);
      ctxPar.fillStyle = COL.text;
      ctxPar.font = '11px sans-serif';
      ctxPar.fillText('same initial law, different draws', 16, 16);
    }

    function updateStats() {
      stats.textContent =
        'step ' + netA.steps +
        '   |   loss A ' + loss(netA, data).toExponential(2) +
        '   |   loss B ' + loss(netB, data).toExponential(2) +
        '   |   gap between seeds ' + seedGap(netA, netB, data).toFixed(3);
    }

    function redraw() {
      drawFits();
      drawParticles();
      updateStats();
    }

    function frame() {
      if (running && netA.steps < MAX_STEPS) {
        for (var s = 0; s < STEPS_PER_FRAME; s++) {
          trainStep(netA, ETA0, data);
          trainStep(netB, ETA0, data);
        }
        redraw();
      }
      requestAnimationFrame(frame);
    }

    slider.addEventListener('input', function () {
      N = Math.pow(2, slider.valueAsNumber);
      nLabel.textContent = String(N);
      rebuild();
      redraw();
    });
    playBtn.addEventListener('click', function () {
      running = !running;
      playBtn.textContent = running ? 'Pause' : 'Play';
    });
    restartBtn.addEventListener('click', function () {
      seedA = (Math.random() * 1e9) >>> 0;
      seedB = (Math.random() * 1e9) >>> 0;
      rebuild();
      redraw();
    });

    nLabel.textContent = String(N);
    redraw();
    requestAnimationFrame(frame);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
