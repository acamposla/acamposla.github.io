// Previews de 1200x630 para el blog: PNG para og:image (LinkedIn no lee bien
// WebP) y WebP para la miniatura del listado.
// Uso: node render-previews.mjs  (desde una carpeta donde se resuelva playwright,
// p. ej. NODE_PATH=~/dotfiles/claude/skills/brand-assets/scripts/node_modules)
import { chromium } from 'playwright';
import { execFileSync } from 'node:child_process';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const aqui = path.dirname(fileURLToPath(import.meta.url));
const salida = path.resolve(aqui, '../../assets/img/previews');
const navegador = await chromium.launch();
const pagina = await navegador.newPage({ viewport: { width: 1200, height: 630 }, deviceScaleFactor: 1 });

async function exportar(id, elemento) {
  const png = path.join(salida, `${id}.png`);
  await elemento.screenshot({ path: png });
  execFileSync('cwebp', ['-quiet', '-q', '84', '-resize', '800', '0', png, '-o', png.replace(/\.png$/, '.webp')]);
  console.log(id);
}

// 1. Lienzos propios.
await pagina.goto('file://' + path.join(aqui, 'previews.html'));
await pagina.waitForLoadState('load');
for (const s of await pagina.$$('section[id]')) await exportar(await s.getAttribute('id'), s);

// 2. Antes de la skill: los dos borradores (OLMO/OMLO) del mockup de la entrada,
//    reencuadrados sin el texto de Claude.
await pagina.goto('file://' + path.resolve(aqui, '../mockups/encargo-a-skill.html'));
await pagina.waitForTimeout(300);
await pagina.evaluate(() => {
  const fotos = document.querySelector('#borradores .fotos');
  const lienzo = document.createElement('section');
  lienzo.id = 'lienzo';
  lienzo.className = 'claude';
  lienzo.style.cssText = 'width:1200px;height:630px;border-radius:0;display:grid;place-items:center;padding:0 56px';
  fotos.style.cssText = 'width:100%;gap:28px';
  for (const c of fotos.querySelectorAll('figcaption')) c.style.cssText = 'font-size:20px;padding:14px 18px';
  lienzo.append(fotos);
  document.body.replaceChildren(lienzo);
  document.body.style.margin = '0';
});
await exportar('antes-de-la-skill', await pagina.$('#lienzo'));

await navegador.close();
