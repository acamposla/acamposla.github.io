// Genera la MISMA slide con dos fichas de marca distintas.
// Uso: node slide-desde-tokens.mjs <tokens.json> <salida.png> "<Nombre de la marca>"
//
// El unico trabajo real es el mapeo de papeles: decidir que token de esta marca
// hace de fondo, cual de tinta y cual de acento. Todo lo demas es el mismo HTML.
import { readFileSync } from 'node:fs';
import { chromium } from 'playwright';

const [rutaTokens, salida, nombreMarca] = process.argv.slice(2);
const ficha = JSON.parse(readFileSync(rutaTokens, 'utf8'));

// Los tokens DTCG anidan y se referencian entre si con {color.brand.600}.
const leer = (ruta) => ruta.split('.').reduce((o, k) => o?.[k], ficha)?.$value;
const resolver = (ruta) => {
  const v = leer(ruta);
  return typeof v === 'string' && v.startsWith('{') ? resolver(v.slice(1, -1)) : v;
};

// Mapeo de papeles: lo que cambia entre una marca y otra.
const papeles = {
  vertienza: { fondo: 'color.neutral.cream', tinta: 'color.ink.base', acento: 'color.accent.copper',
               marca: 'color.brand.600', suave: 'color.text.secondary',
               display: 'typography.fontFamily.display', cuerpo: 'typography.fontFamily.body',
               radio: 'radius.lg' },
  sapioverse: { fondo: 'color.paper.base', tinta: 'color.ink.base', acento: 'color.brand.600',
                marca: 'color.indigo.600', suave: 'color.ink.soft',
                display: 'typography.fontFamily.sans', cuerpo: 'typography.fontFamily.sans',
                radio: 'radius.card' },
};
const p = papeles[nombreMarca.toLowerCase()];
const v = Object.fromEntries(Object.entries(p).map(([papel, ruta]) => [papel, resolver(ruta)]));

const html = `<!doctype html><meta charset="utf-8"><style>
  * { margin: 0; box-sizing: border-box; }
  body { width: 1280px; height: 720px; background: ${v.fondo}; color: ${v.tinta};
         font-family: ${v.cuerpo}; display: flex; flex-direction: column;
         justify-content: center; padding: 96px; gap: 28px; }
  .etiqueta { font-size: 13px; letter-spacing: .22em; text-transform: uppercase;
              font-weight: 700; color: ${v.acento}; }
  h1 { font-family: ${v.display}; font-size: 76px; line-height: 1.05; max-width: 15ch;
       font-weight: 700; }
  p { font-size: 24px; color: ${v.suave}; max-width: 44ch; line-height: 1.5; }
  .barra { width: 120px; height: 10px; background: ${v.marca}; border-radius: ${v.radio}; }
  .pie { position: absolute; bottom: 56px; left: 96px; font-size: 15px;
         letter-spacing: .12em; text-transform: uppercase; color: ${v.marca}; font-weight: 600; }
</style>
<div class="etiqueta">Ejemplo del artículo</div>
<h1>Esta slide no elige ningún color</h1>
<div class="barra"></div>
<p>Los lee de la ficha de valores de la marca. El HTML es el mismo en las dos: lo único
   que cambia es qué fichero se le pasa.</p>
<div class="pie">${nombreMarca}</div>`;

const navegador = await chromium.launch();
const pagina = await navegador.newPage({ viewport: { width: 1280, height: 720 }, deviceScaleFactor: 2 });
await pagina.setContent(html, { waitUntil: 'networkidle' });
await pagina.screenshot({ path: salida });
await navegador.close();
console.log(`${nombreMarca}: fondo ${v.fondo} · tinta ${v.tinta} · acento ${v.acento} · ${v.display.split(',')[0]}`);
