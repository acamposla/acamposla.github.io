// Exporta cada <section id> de un HTML de mockups a PNG (2x) y WebP.
// Uso: node render.mjs <mockups.html> <carpeta-salida> <prefijo>
// Playwright se resuelve desde donde se ejecute (p. ej. brand-assets/scripts).
import { chromium } from 'playwright';
import { execFileSync } from 'node:child_process';
import path from 'node:path';

const [html, salida, prefijo] = process.argv.slice(2);
const navegador = await chromium.launch();
const pagina = await navegador.newPage({ viewport: { width: 900, height: 900 }, deviceScaleFactor: 2 });
await pagina.goto('file://' + path.resolve(html));
await pagina.waitForTimeout(300);
for (const s of await pagina.$$('section[id]')) {
  const id = await s.getAttribute('id');
  const png = path.join(salida, `${prefijo}-${id}.png`);
  const destino = (await s.$('.claude, .hf, .editor')) ?? s;
  await destino.screenshot({ path: png, omitBackground: true });
  execFileSync('cwebp', ['-quiet', '-q', '86', png, '-o', png.replace(/\.png$/, '.webp')]);
  console.log(id);
}
await navegador.close();
