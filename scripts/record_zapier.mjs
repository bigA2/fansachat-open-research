// Records short video clips (Playwright, headless) of public Zapier pages about building Zaps and fixing broken ones.
// No login, no AI. Output: results/zapier/clips/*.webm + pages.json (url, title, ok).
import { chromium } from 'playwright';
import fs from 'node:fs';
const URLS = [
  'https://zapier.com/how-it-works',
  'https://zapier.com/features/autoreplay',
  'https://zapier.com/ai/copilot',
  'https://zapier.com/blog/troubleshoot-zap-errors/',
  'https://help.zapier.com/hc/en-us/articles/8496309697421',
  'https://zapier.com/apps',
];
fs.mkdirSync('results/zapier/clips', { recursive: true });
const browser = await chromium.launch();
const out = [];
for (const [i, url] of URLS.entries()) {
  const ctx = await browser.newContext({ viewport: { width: 1280, height: 800 }, recordVideo: { dir: 'results/zapier/clips', size: { width: 1280, height: 800 } } });
  const page = await ctx.newPage();
  let ok = true, title = '';
  try {
    await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 45000 });
    await page.waitForTimeout(2500); title = await page.title();
    for (let y = 0; y < 8; y++) { await page.mouse.wheel(0, 700); await page.waitForTimeout(900); }   // slow scroll = readable clip
  } catch (e) { ok = false; title = String(e).slice(0, 120); }
  const v = page.video(); await ctx.close();
  const f = `results/zapier/clips/${String(i).padStart(2, '0')}.webm`; if (v) fs.renameSync(await v.path(), f);
  out.push({ url, ok, title, clip: f }); console.log(url, ok, title);
}
await browser.close();
fs.writeFileSync('results/zapier/pages.json', JSON.stringify(out, null, 1));
