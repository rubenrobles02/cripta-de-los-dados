// Capturas para Google Play (teléfono, tablet 7", tablet 10") y banner 1024x500 con Chrome headless.
// Uso: python -m http.server 18931 --bind 127.0.0.1  (en cripta-dados/)  y luego  node app/capturas.mjs
import { spawn } from 'node:child_process';
import { writeFileSync, mkdirSync } from 'node:fs';

const OUT = 'C:/Users/Gabriel/Desktop/claudecode/cripta-dados/app/store';
const URL = 'http://127.0.0.1:18931/docs/index.html';
const chrome = spawn('C:/Program Files/Google/Chrome/Application/chrome.exe', [
  '--headless=new', '--remote-debugging-port=9333', '--user-data-dir=' + process.env.TEMP + '/cripta-shots',
  '--mute-audio', 'about:blank']);
const sleep = ms => new Promise(r => setTimeout(r, ms));
let tabs;
for (let i = 0; i < 40; i++) { try { tabs = await (await fetch('http://127.0.0.1:9333/json')).json(); break; } catch { await sleep(250); } }
const ws = new WebSocket(tabs.find(t => t.type === 'page').webSocketDebuggerUrl);
await new Promise(r => ws.onopen = r);
let id = 0; const pend = {};
ws.onmessage = e => { const m = JSON.parse(e.data); if (m.id && pend[m.id]) { pend[m.id](m); delete pend[m.id]; } };
const cmd = (method, params = {}) => new Promise(r => { const i = ++id; pend[i] = r; ws.send(JSON.stringify({ id: i, method, params })); });
const js = async expr => (await cmd('Runtime.evaluate', { expression: expr, awaitPromise: true, returnByValue: true })).result?.result?.value;
const click = sel => js(`(()=>{const e=document.querySelector(${JSON.stringify(sel)}); if(e){e.click();return true} return false})()`);
const META = JSON.stringify({ best: 31, wins: 1, runs: 9, bank: 2400, skins: ['bone', 'gold', 'crystal', 'storm'], introSeen: true,
  gear: { owned: { hm_crown: 3, am_phoenix: 5, sh_iron: 4, ch_mail: 6, bt_scout: 2, sh_oak: 7, ch_leather: 3, am_coin: 2 },
    eq: { helm: 'hm_crown', amulet: 'am_phoenix', shield: 'sh_iron', chest: 'ch_mail', boots: 'bt_scout' } } });
let dir, W, H, SC, n;
async function shot(name) {
  const r = await cmd('Page.captureScreenshot', { format: 'png' });
  writeFileSync(`${OUT}/${dir}/${++n}-${name}.png`, Buffer.from(r.result.data, 'base64'));
  const fit = await js(`(()=>{const c=document.querySelector('#sheet:not([hidden]) .sheet-card'); return c?c.scrollHeight+'/'+c.clientHeight:''})()`);
  console.log(dir, n, name, fit || '');
}
async function fresh(meta) {
  await cmd('Emulation.setDeviceMetricsOverride', { width: W, height: H, deviceScaleFactor: SC, mobile: true });
  await cmd('Page.navigate', { url: URL }); await sleep(1500);
  await js(`localStorage.clear(); localStorage.setItem('cripta-music','false'); localStorage.setItem('cripta-skin','"crystal"'); ${meta ? `localStorage.setItem('cripta-meta',${JSON.stringify(META)})` : ''}; location.reload()`);
  await sleep(2500);
}
async function series(d, w, h, sc) {
  dir = d; W = w; H = h; SC = sc; n = 0; mkdirSync(`${OUT}/${dir}`, { recursive: true });
  await fresh(true);
  await shot('portada');
  await click('#bNew'); await sleep(700); await click('#mInf'); await sleep(1500);
  if (await click('#iSkip')) await sleep(1500);
  await shot('puertas');
  await click('.door'); await sleep(2000);
  await click('#bRoll'); await sleep(3500);
  await shot('combate');
  await click('#pause'); await sleep(600); await click('#pGear'); await sleep(900);
  await shot('equipo');
  await click('#gBack'); await sleep(500); await click('#pArm'); await sleep(900); await js(`document.querySelector('#devGold')?.remove()`);
  await shot('armeria');
  await fresh(false); await click('#bNew'); await sleep(700); await click('#mInf'); await sleep(2500);
  await shot('historia');
}
await cmd('Page.enable'); await cmd('Runtime.enable');
await cmd('Emulation.setTouchEmulationEnabled', { enabled: true });

await series('telefono', 844, 475, 2);      // 1688x950  (16:9)
await series('tablet-7', 960, 600, 1.5);    // 1440x900  (16:10)
await series('tablet-10', 1280, 800, 2);    // 2560x1600 (16:10)

// feature graphic / banner 1024x500
W = 1024; H = 500; SC = 1; await fresh(true);
await js(`(()=>{const m=document.querySelector('#bNew').closest('.pf')||document.querySelector('#bNew').parentElement; m.style.visibility='hidden';
  const t=document.createElement('div'); t.innerHTML='Tira · Fija · Baja'; t.style.cssText='position:fixed;left:0;right:0;bottom:34px;text-align:center;font:600 30px Pixelify Sans;color:#f4ecd8;letter-spacing:2px;text-shadow:0 3px 0 #000,3px 0 0 #000,-3px 0 0 #000,0 -3px 0 #000;z-index:50';
  document.body.appendChild(t)})()`);
await sleep(800);
const r = await cmd('Page.captureScreenshot', { format: 'png' });
writeFileSync(`${OUT}/banner-1024x500.png`, Buffer.from(r.result.data, 'base64')); console.log('banner');
ws.close(); chrome.kill();
