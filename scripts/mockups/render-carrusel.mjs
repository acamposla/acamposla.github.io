// Exporta el carrusel: un PNG 1080x1350 por slide y un PDF con todas (el formato
// que LinkedIn publica como documento deslizable).
// Uso: node render-carrusel.mjs <carrusel.html> <carpeta-salida>
import { chromium } from 'playwright';
import path from 'node:path';

const [html, salida] = process.argv.slice(2);
const navegador = await chromium.launch();
const pagina = await navegador.newPage({ viewport: { width: 1080, height: 1350 } });
await pagina.goto('file://' + path.resolve(html));
await pagina.waitForLoadState('networkidle');
const slides = await pagina.$$('section.slide');
for (const [i, s] of slides.entries()) {
  await s.screenshot({ path: path.join(salida, `slide-${String(i + 1).padStart(2, '0')}.png`) });
}
await pagina.pdf({ path: path.join(salida, 'carrusel.pdf'), width: '1080px', height: '1350px', printBackground: true });
console.log(`${slides.length} slides`);
await navegador.close();
