/* Interactive widgets for "The Mean-Field Theory of Two-Layer Neural Networks".
 *
 *   #lln-widget        the law of large numbers. Two two-layer tanh networks in
 *                      the mean-field parametrization, same data, different
 *                      seeds, trained side by side at a width N set by a slider.
 *
 *   #lazy-rich-widget  lazy vs rich training. One network at output scale
 *                      alpha with the step size compensated by 1/alpha^2
 *                      (Chizat-Oyallon-Bach); the slider sets alpha and is
 *                      marked at alpha = sqrt(N), where the NTK parametrization sits.
 *
 * Each widget is two panels (the fit, the neurons as particles in the (w, v)
 * plane), one control row (slider, pause, restart, target menu) and one status
 * line. The container div may hold a `.mfw-math` block written in the post
 * (MathJax typesets it); the widget appends its UI after it.
 *
 * Zero dependencies. The simulation core is DOM-free so it can be smoke-tested
 * in Node: `node -e "const m = require('./mf-widgets.js'); ..."`.
 */
(function () {
  'use strict';

  /* ===================== simulation core (DOM-free) ===================== */

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

  var TARGETS = [
    { key: 'kinks', label: 'three kinks',
      units: [{ W: 2.0, B: 3.0, V: 1.2 }, { W: 2.5, B: -0.5, V: -1.4 }, { W: 1.5, B: -3.0, V: 0.8 }] },
    { key: 'single', label: 'single neuron',
      units: [{ W: 2.0, B: -1.0, V: 1.5 }] },
    { key: 'bump', label: 'bump',
      units: [{ W: 3.0, B: 3.0, V: 1.0 }, { W: 3.0, B: -3.0, V: -1.0 }] },
    { key: 'sine', label: 'sine',
      fn: function (x) { return 1.5 * Math.sin(1.3 * x); } }
  ];

  function targetFn(t) {
    if (t.fn) return t.fn;
    var u = t.units;
    return function (x) {
      var y = 0;
      for (var k = 0; k < u.length; k++) y += u[k].V * Math.tanh(u[k].W * x + u[k].B);
      return y;
    };
  }

  function makeData(t, nPoints) {
    var f = targetFn(t);
    var xs = new Float64Array(nPoints), ys = new Float64Array(nPoints);
    for (var j = 0; j < nPoints; j++) {
      xs[j] = -3 + 6 * j / (nPoints - 1);
      ys[j] = f(xs[j]);
    }
    return { xs: xs, ys: ys, n: nPoints, f: f };
  }

  // i.i.d. Gaussian init: neurons are samples from the same base measure, so
  // different seeds are different empirical draws of the SAME initial law.
  // `symmetric` pairs units with opposite output weights so f == 0 at init.
  function createNet(N, seed, symmetric) {
    var randn = makeRandn(mulberry32(seed));
    var w = new Float64Array(N), b = new Float64Array(N), v = new Float64Array(N);
    var i;
    if (symmetric) {
      var half = N >> 1;
      for (i = 0; i < half; i++) {
        var wi = randn(), bi = randn(), vi = randn();
        w[i] = wi; b[i] = bi; v[i] = vi;
        w[i + half] = wi; b[i + half] = bi; v[i + half] = -vi;
      }
    } else {
      for (i = 0; i < N; i++) { w[i] = randn(); b[i] = randn(); v[i] = randn(); }
    }
    return { N: N, w: w, b: b, v: v, w0: w.slice(), b0: b.slice(), v0: v.slice(),
             steps: 0, cache: null, res: null };
  }

  function netForward(net, alpha, x) {
    var s = 0;
    for (var i = 0; i < net.N; i++) s += net.v[i] * Math.tanh(net.w[i] * x + net.b[i]);
    return alpha * s / net.N;
  }

  // One full-batch GD step. Effective step size eta0 * N / alpha^2: the
  // N-scaling is the mean-field convention (O(1) particle velocity), the
  // 1/alpha^2 keeps the function-space dynamics comparable across alpha.
  function trainStep(net, alpha, eta0, data) {
    var N = net.N, n = data.n;
    if (!net.cache || net.cache.length !== N * n) net.cache = new Float64Array(N * n);
    if (!net.res || net.res.length !== n) net.res = new Float64Array(n);
    var res = net.res, tanhCache = net.cache;
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
      var gw = 0, gb = 0, gv = 0, vi = net.v[i], base = i * n;
      for (j = 0; j < n; j++) {
        t = tanhCache[base + j];
        var dsig = (1 - t * t) * res[j];
        gv += t * res[j];
        gw += vi * dsig * data.xs[j];
        gb += vi * dsig;
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

  // RMS gap between two networks' outputs: the visible face of the LLN.
  function rmsGap(netA, netB, data) {
    var s = 0;
    for (var j = 0; j < data.n; j++) {
      var d = netForward(netA, 1, data.xs[j]) - netForward(netB, 1, data.xs[j]);
      s += d * d;
    }
    return Math.sqrt(s / data.n);
  }

  var core = {
    TARGETS: TARGETS, targetFn: targetFn, makeData: makeData, createNet: createNet,
    netForward: netForward, trainStep: trainStep, loss: loss,
    meanDisplacement: meanDisplacement, rmsGap: rmsGap
  };

  if (typeof module !== 'undefined' && module.exports) module.exports = core;
  if (typeof document === 'undefined') return;

  /* ============================ shared UI ============================ */

  // Palette shared with the post's static figures.
  var COL = { blue: '#2166ac', red: '#b2182b', orange: '#e08214', ghost: '#c8c8c8',
              target: '#333333', axis: '#cfcfcf', zero: '#ececec', text: '#777777', dark: '#333333' };

  function hexToRgb(h) { return [parseInt(h.slice(1, 3), 16), parseInt(h.slice(3, 5), 16), parseInt(h.slice(5, 7), 16)]; }
  function lerpColor(c1, c2, t) {
    var a = hexToRgb(c1), b = hexToRgb(c2), o = [];
    for (var i = 0; i < 3; i++) o.push(Math.round(a[i] + (b[i] - a[i]) * t));
    return 'rgb(' + o.join(',') + ')';
  }

  function injectStyle() {
    if (document.getElementById('mfw-style')) return;
    var css = [
      '.mfw{font:13px/1.45 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;',
      'color:#333;border:1px solid #e3e3e3;border-radius:8px;padding:12px 14px 10px;margin:1.4em 0;background:#fff}',
      '.mfw-math{text-align:center;margin:0 0 6px;overflow-x:auto}',
      '.mfw-row{display:flex;gap:14px;flex-wrap:wrap}',
      '.mfw-panel{flex:1 1 260px;min-width:240px}',
      '.mfw-panel canvas{width:100%;display:block}',
      '.mfw-title{font-size:12px;color:#666;text-align:center;margin:0 0 3px}',
      '.mfw-ctrl{display:flex;align-items:center;gap:10px 14px;flex-wrap:wrap;margin-top:12px;font-size:12.5px;color:#555}',
      '.mfw-ctrl label{white-space:nowrap}',
      '.mfw-ctrl select{font:inherit;font-size:12px;padding:2px 4px;margin-left:4px}',
      '.mfw-slider{flex:1 1 220px;min-width:180px;position:relative;padding-bottom:16px}',
      '.mfw-slider input{width:100%;margin:0;display:block;accent-color:#555}',
      '.mfw-ticks{position:absolute;left:8px;right:8px;top:20px;font-size:10.5px;color:#888}',
      '.mfw-tick{position:absolute;transform:translateX(-50%);white-space:nowrap}',
      '.mfw-btn{font:inherit;font-size:12px;padding:3px 10px;border:1px solid #ccc;border-radius:4px;background:#fafafa;cursor:pointer;color:#333}',
      '.mfw-btn:hover{background:#f0f0f0}',
      '.mfw-status{font-size:12px;color:#777;margin-top:8px;font-variant-numeric:tabular-nums;min-height:1.4em}'
    ].join('');
    var style = document.createElement('style');
    style.id = 'mfw-style';
    style.textContent = css;
    document.head.appendChild(style);
  }

  function el(tag, cls, html) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (html !== undefined) e.innerHTML = html;
    return e;
  }

  function makePanel(parent, title) {
    var div = el('div', 'mfw-panel');
    var t = el('p', 'mfw-title', title);
    var canvas = document.createElement('canvas');
    div.appendChild(t); div.appendChild(canvas);
    parent.appendChild(div);
    var p = { div: div, title: t, canvas: canvas, ctx: canvas.getContext('2d'), W: 300, H: 210 };
    p.resize = function () {
      var w = div.clientWidth || 300;
      var h = Math.round(w * 0.7);
      var dpr = window.devicePixelRatio || 1;
      canvas.width = Math.round(w * dpr);
      canvas.height = Math.round(h * dpr);
      canvas.style.height = h + 'px';
      p.ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      p.W = w; p.H = h;
    };
    p.resize();
    return p;
  }

  // Plot area with a frame, faint zero lines, tick labels and axis labels.
  function makePlot(panel, o) {
    var padL = 30, padB = 24, padT = 6, padR = 6;
    var pl = { o: o, panel: panel };
    pl.X = function (v) { return padL + (v - o.xmin) / (o.xmax - o.xmin) * (panel.W - padL - padR); };
    pl.Y = function (v) { return panel.H - padB - (v - o.ymin) / (o.ymax - o.ymin) * (panel.H - padB - padT); };
    pl.begin = function () {
      var ctx = panel.ctx, W = panel.W, H = panel.H, k;
      ctx.clearRect(0, 0, W, H);
      ctx.lineWidth = 1;
      ctx.strokeStyle = COL.zero;
      ctx.beginPath();
      ctx.moveTo(pl.X(0), padT); ctx.lineTo(pl.X(0), H - padB);
      ctx.moveTo(padL, pl.Y(0)); ctx.lineTo(W - padR, pl.Y(0));
      ctx.stroke();
      ctx.strokeStyle = COL.axis;
      ctx.strokeRect(padL + 0.5, padT + 0.5, W - padL - padR - 1, H - padB - padT - 1);
      ctx.fillStyle = COL.text;
      ctx.font = '9.5px sans-serif';
      ctx.textAlign = 'center'; ctx.textBaseline = 'top';
      for (k = 0; k < o.xticks.length; k++) ctx.fillText(String(o.xticks[k]), pl.X(o.xticks[k]), H - padB + 4);
      ctx.textAlign = 'right'; ctx.textBaseline = 'middle';
      for (k = 0; k < o.yticks.length; k++) ctx.fillText(String(o.yticks[k]), padL - 4, pl.Y(o.yticks[k]));
      ctx.fillStyle = COL.dark;
      ctx.font = 'italic 11px serif';
      ctx.textAlign = 'center'; ctx.textBaseline = 'alphabetic';
      ctx.fillText(o.xlabel, (padL + W - padR) / 2, H - 3);
      ctx.save();
      ctx.translate(9, (padT + H - padB) / 2);
      ctx.rotate(-Math.PI / 2);
      ctx.fillText(o.ylabel, 0, 0);
      ctx.restore();
      ctx.save(); ctx.beginPath(); ctx.rect(padL, padT, W - padL - padR, H - padB - padT); ctx.clip();
    };
    pl.end = function () { panel.ctx.restore(); };
    return pl;
  }

  var FIT = { xmin: -3, xmax: 3, ymin: -2.6, ymax: 2.6, xlabel: 'x', ylabel: 'f(x)',
              xticks: [-3, -2, -1, 0, 1, 2, 3], yticks: [-2, -1, 0, 1, 2] };
  var PAR = { xmin: -4, xmax: 4, ymin: -5, ymax: 5, xlabel: 'w', ylabel: 'v',
              xticks: [-4, -2, 0, 2, 4], yticks: [-4, -2, 0, 2, 4] };

  function drawCurve(pl, f, color, dash, lw) {
    var ctx = pl.panel.ctx;
    ctx.strokeStyle = color;
    ctx.setLineDash(dash || []);
    ctx.lineWidth = lw;
    ctx.beginPath();
    for (var j = 0; j <= 120; j++) {
      var x = -3 + 6 * j / 120, y = f(x);
      if (j === 0) ctx.moveTo(pl.X(x), pl.Y(y)); else ctx.lineTo(pl.X(x), pl.Y(y));
    }
    ctx.stroke();
    ctx.setLineDash([]);
  }

  function clampW(w) { return Math.max(-3.95, Math.min(3.95, w)); }
  function clampV(v) { return Math.max(-4.95, Math.min(4.95, v)); }

  function drawDots(pl, net, color, alpha, init) {
    var ctx = pl.panel.ctx, w = init ? net.w0 : net.w, v = init ? net.v0 : net.v;
    ctx.globalAlpha = alpha;
    ctx.beginPath();
    for (var i = 0; i < net.N; i++) {
      var x = pl.X(clampW(w[i])), y = pl.Y(clampV(v[i]));
      ctx.moveTo(x + 2.6, y);
      ctx.arc(x, y, 2.6, 0, 2 * Math.PI);
    }
    if (init) { ctx.strokeStyle = color; ctx.lineWidth = 1; ctx.stroke(); }
    else { ctx.fillStyle = color; ctx.fill(); }
    ctx.globalAlpha = 1;
  }

  function makeSelect(parent, labelText, options, value, onChange) {
    var lab = el('label', null, labelText);
    var sel = document.createElement('select');
    for (var k = 0; k < options.length; k++) {
      var op = document.createElement('option');
      op.value = options[k][0]; op.textContent = options[k][1];
      if (options[k][0] === value) op.selected = true;
      sel.appendChild(op);
    }
    lab.appendChild(sel);
    parent.appendChild(lab);
    sel.addEventListener('change', function () { onChange(sel.value); });
    return sel;
  }

  function makeButton(parent, text, onClick) {
    var b = el('button', 'mfw-btn', text);
    b.type = 'button';
    b.addEventListener('click', onClick);
    parent.appendChild(b);
    return b;
  }

  // Slider with labelled ticks underneath. ticks: [[value, label, align], ...]
  function makeSlider(parent, labelHtml, min, max, value, ticks) {
    var lab = el('span', null, labelHtml);
    var wrap = el('div', 'mfw-slider');
    var input = document.createElement('input');
    input.type = 'range'; input.min = min; input.max = max; input.step = 1; input.value = value;
    var tk = el('div', 'mfw-ticks');
    for (var k = 0; k < ticks.length; k++) {
      var t = el('div', 'mfw-tick', ticks[k][1]);
      t.style.left = ((ticks[k][0] - min) / (max - min) * 100) + '%';
      if (ticks[k][2] === 'left') t.style.transform = 'none';
      if (ticks[k][2] === 'right') t.style.transform = 'translateX(-100%)';
      tk.appendChild(t);
    }
    wrap.appendChild(input); wrap.appendChild(tk);
    parent.appendChild(lab); parent.appendChild(wrap);
    return { input: input, label: lab };
  }

  var SELECT_TARGETS = TARGETS.map(function (t) { return [t.key, t.label]; });
  function findTarget(key) {
    for (var k = 0; k < TARGETS.length; k++) if (TARGETS[k].key === key) return TARGETS[k];
    return TARGETS[0];
  }

  function prepareRoot(id) {
    var root = document.getElementById(id);
    if (!root || root.hasAttribute('data-mfw-init')) return null;
    root.setAttribute('data-mfw-init', '1');
    injectStyle();
    root.classList.add('mfw'); root.classList.add('tex2jax_ignore');
    var m = root.getElementsByClassName('mfw-math');
    for (var k = 0; k < m.length; k++) m[k].classList.add('tex2jax_process');
    return root;
  }

  function watchVisibility(root, st) {
    st.visible = true;
    if (!('IntersectionObserver' in window)) return;
    new IntersectionObserver(function (entries) { st.visible = entries[0].isIntersecting; },
                             { rootMargin: '100px' }).observe(root);
  }

  function onResize(fn) {
    var pending = false;
    window.addEventListener('resize', function () {
      if (pending) return;
      pending = true;
      requestAnimationFrame(function () { pending = false; fn(); });
    });
  }

  function swatch(text, color) { return '<span style="color:' + color + ';font-weight:600">' + text + '</span>'; }

  /* ====================== widget 1: law of large numbers ====================== */

  function initLLN() {
    var root = prepareRoot('lln-widget');
    if (!root) return;

    var N_DATA = 64, ETA0 = 0.1, SPF = 6, MAX_STEPS = 3000;
    var WIDTHS = [8, 16, 32, 64, 128, 256, 512];
    var st = { target: TARGETS[0], k: 0, seedA: 42, seedB: 1337, running: true };

    var row = el('div', 'mfw-row');
    root.appendChild(row);
    var pFit = makePanel(row, 'two fits: ' + swatch('seed A', COL.blue) + ', ' + swatch('seed B', COL.orange) + '; target dashed');
    var pPar = makePanel(row, 'the neurons as particles (w<sub>i</sub>, v<sub>i</sub>)');
    var plFit = makePlot(pFit, FIT), plPar = makePlot(pPar, PAR);

    var ctrl = el('div', 'mfw-ctrl');
    root.appendChild(ctrl);
    var sl = makeSlider(ctrl, 'width N = <b>8</b>', 0, WIDTHS.length - 1, 0,
      [[0, '&larr; few particles: luck matters', 'left'], [6, 'many particles: deterministic &rarr;', 'right']]);
    var nLabel = sl.label.querySelector('b');
    var playBtn = makeButton(ctrl, 'Pause', function () {
      st.running = !st.running; playBtn.textContent = st.running ? 'Pause' : 'Play';
    });
    makeButton(ctrl, 'Restart', function () {
      st.seedA = (Math.random() * 1e9) >>> 0; st.seedB = (Math.random() * 1e9) >>> 0;
      rebuild(); redraw();
    });
    makeSelect(ctrl, 'target', SELECT_TARGETS, st.target.key, function (v) {
      st.target = findTarget(v); data = makeData(st.target, N_DATA); rebuild(); redraw();
    });

    var status = el('div', 'mfw-status');
    root.appendChild(status);

    var data = makeData(st.target, N_DATA);
    var netA, netB;

    function width() { return WIDTHS[st.k]; }
    function rebuild() {
      netA = createNet(width(), st.seedA, false);
      netB = createNet(width(), st.seedB, false);
    }

    function redraw() {
      plFit.begin();
      drawCurve(plFit, data.f, COL.target, [5, 4], 1.4);
      drawCurve(plFit, function (x) { return netForward(netA, 1, x); }, COL.blue, [], 2);
      drawCurve(plFit, function (x) { return netForward(netB, 1, x); }, COL.orange, [], 2);
      plFit.end();
      plPar.begin();
      drawDots(plPar, netA, COL.blue, 0.6, false);
      drawDots(plPar, netB, COL.orange, 0.6, false);
      plPar.end();
      status.textContent = 'step ' + netA.steps + (netA.steps >= MAX_STEPS ? ' (done)' : '') +
        '   ·   loss A ' + loss(netA, 1, data).toExponential(1) +
        ', B ' + loss(netB, 1, data).toExponential(1) +
        '   ·   gap between seeds ' + rmsGap(netA, netB, data).toFixed(3);
    }

    function frame() {
      if (st.running && st.visible && netA.steps < MAX_STEPS) {
        for (var s = 0; s < SPF; s++) {
          trainStep(netA, 1, ETA0, data);
          trainStep(netB, 1, ETA0, data);
        }
        redraw();
      }
      requestAnimationFrame(frame);
    }

    sl.input.addEventListener('input', function () {
      st.k = sl.input.valueAsNumber;
      nLabel.textContent = String(width());
      rebuild(); redraw();
    });

    onResize(function () { pFit.resize(); pPar.resize(); redraw(); });
    watchVisibility(root, st);
    rebuild();
    redraw();
    requestAnimationFrame(frame);
  }

  /* ====================== widget 2: lazy vs rich ====================== */

  function initLazyRich() {
    var root = prepareRoot('lazy-rich-widget');
    if (!root) return;

    var N = 64, N_DATA = 64, ETA0 = 0.1, SPF = 8, MAX_STEPS = 3000;
    var K_MAX = 14, K_NTK = 6;              // alpha = 2^(k/2): 1 ... 128; sqrt(N) = 8 at k = 6
    var st = { target: TARGETS[0], k: 0, seed: 42, running: true };

    function alpha() {
      var a = Math.pow(2, st.k / 2);
      return a >= 4 ? Math.round(a) : Math.round(a * 10) / 10;
    }
    function color() { return lerpColor(COL.blue, COL.red, st.k / K_MAX); }

    var row = el('div', 'mfw-row');
    root.appendChild(row);
    var pFit = makePanel(row, 'the fit; target dashed');
    var pPar = makePanel(row, 'the neurons as particles (w<sub>i</sub>, v<sub>i</sub>); open circles: initialization');
    var plFit = makePlot(pFit, FIT), plPar = makePlot(pPar, PAR);

    var ctrl = el('div', 'mfw-ctrl');
    root.appendChild(ctrl);
    var sl = makeSlider(ctrl, 'output scale &alpha; = <b>1</b>', 0, K_MAX, 0,
      [[0, '&larr; rich', 'left'], [K_NTK, 'NTK: &alpha; = &radic;N'], [K_MAX, 'lazy &rarr;', 'right']]);
    var aLabel = sl.label.querySelector('b');
    var playBtn = makeButton(ctrl, 'Pause', function () {
      st.running = !st.running; playBtn.textContent = st.running ? 'Pause' : 'Play';
    });
    makeButton(ctrl, 'Restart', function () {
      st.seed = (Math.random() * 1e9) >>> 0; rebuild(); redraw();
    });
    makeSelect(ctrl, 'target', SELECT_TARGETS, st.target.key, function (v) {
      st.target = findTarget(v); data = makeData(st.target, N_DATA); rebuild(); redraw();
    });

    var status = el('div', 'mfw-status');
    root.appendChild(status);

    var data = makeData(st.target, N_DATA);
    var net;

    function rebuild() { net = createNet(N, st.seed, true); }

    function redraw() {
      var a = alpha(), c = color();
      plFit.begin();
      drawCurve(plFit, data.f, COL.target, [5, 4], 1.4);
      drawCurve(plFit, function (x) { return netForward(net, a, x); }, c, [], 2);
      plFit.end();
      plPar.begin();
      drawDots(plPar, net, COL.ghost, 1, true);
      drawDots(plPar, net, c, 0.75, false);
      plPar.end();
      status.textContent = 'step ' + net.steps + (net.steps >= MAX_STEPS ? ' (done)' : '') +
        '   ·   loss ' + loss(net, a, data).toExponential(1) +
        '   ·   mean particle displacement ' + meanDisplacement(net).toFixed(3);
    }

    function frame() {
      if (st.running && st.visible && net.steps < MAX_STEPS) {
        var a = alpha();
        for (var s = 0; s < SPF; s++) trainStep(net, a, ETA0, data);
        redraw();
      }
      requestAnimationFrame(frame);
    }

    sl.input.addEventListener('input', function () {
      st.k = sl.input.valueAsNumber;
      aLabel.textContent = String(alpha());
      rebuild(); // same initialization, new scale: apples-to-apples
      redraw();
    });

    onResize(function () { pFit.resize(); pPar.resize(); redraw(); });
    watchVisibility(root, st);
    rebuild();
    redraw();
    requestAnimationFrame(frame);
  }

  function init() { initLLN(); initLazyRich(); }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
