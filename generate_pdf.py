import os
import base64
import subprocess

def img_to_base64(path):
    with open(path, "rb") as f:
        return "data:image/png;base64," + base64.b64encode(f.read()).decode('utf-8')

b_celula_basica = img_to_base64("fotos/celula_basica.png")
b_bacteria = img_to_base64("fotos/bacteria_procariota.png")
b_muscular = img_to_base64("fotos/celula_muscular_A.png")
b_nerviosa = img_to_base64("fotos/celula_nerviosa_B.png")
b_vegetal = img_to_base64("fotos/celula_vegetal_C.png")

html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Tema 2: La Célula - Páginas 10 y 11 (Español)</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Fira+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400&family=Oswald:wght@500;600;700&display=swap');

  @page {{
    size: A4 portrait;
    margin: 0;
  }}

  * {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }}

  body {{
    font-family: 'Fira Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    background-color: #f1f5f9;
    color: #1e293b;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }}

  .page {{
    width: 210mm;
    height: 297mm;
    padding: 16mm 18mm 14mm 18mm;
    margin: 0 auto 20px auto;
    background: #ffffff;
    position: relative;
    page-break-after: always;
    box-shadow: 0 4px 20px rgba(0,0,0,0.08);
    overflow: hidden;
  }}

  @media print {{
    body {{
      background: none;
    }}
    .page {{
      margin: 0;
      box-shadow: none;
      page-break-after: always;
    }}
  }}

  /* HEADER */
  .page-header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 2px solid #e2e8f0;
    padding-bottom: 6px;
    margin-bottom: 14px;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.08em;
    color: #64748b;
    text-transform: uppercase;
  }}

  .page-number {{
    font-family: 'Oswald', sans-serif;
    font-size: 14px;
    color: #0284c7;
    font-weight: 700;
  }}

  /* SECTION TITLE BANNER */
  .section-banner {{
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: #0284c7;
    color: #ffffff;
    padding: 4px 12px 4px 6px;
    border-radius: 4px;
    margin-bottom: 10px;
  }}

  .sec-num {{
    background: #ffffff;
    color: #0284c7;
    font-family: 'Oswald', sans-serif;
    font-weight: 700;
    font-size: 17px;
    padding: 2px 7px;
    border-radius: 3px;
    line-height: 1;
  }}

  .sec-title {{
    font-family: 'Oswald', sans-serif;
    font-size: 18px;
    font-weight: 700;
    letter-spacing: 0.04em;
    text-transform: uppercase;
  }}

  .intro-p {{
    font-size: 12.5px;
    line-height: 1.45;
    color: #334155;
    margin-bottom: 12px;
  }}

  /* 4 POSTULATES PILL BOXES */
  .postulates-grid {{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 8px;
    margin-bottom: 14px;
  }}

  .postulate-card {{
    background: #f8fafc;
    border: 1.5px solid #cbd5e1;
    border-radius: 10px;
    padding: 9px 8px;
    text-align: center;
    display: flex;
    flex-direction: column;
  }}

  .postulate-pill {{
    display: inline-block;
    border: 1.5px solid #64748b;
    border-radius: 999px;
    padding: 2px 10px;
    font-weight: 700;
    font-size: 11.5px;
    color: #0f172a;
    margin: 0 auto 6px auto;
    background: #ffffff;
  }}

  .postulate-desc {{
    font-size: 11px;
    line-height: 1.35;
    color: #475569;
    text-align: left;
  }}

  /* TIMELINE BOX */
  .timeline-container {{
    border: 1.5px solid #0284c7;
    border-radius: 8px;
    padding: 10px 14px;
    background: #f0f9ff;
    margin-bottom: 14px;
  }}

  .timeline-title {{
    font-family: 'Oswald', sans-serif;
    font-size: 13.5px;
    color: #0369a1;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-bottom: 8px;
    font-weight: 700;
  }}

  .timeline-items {{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 10px;
    position: relative;
  }}

  .timeline-items::before {{
    content: '';
    position: absolute;
    top: 26px;
    left: 20px;
    right: 20px;
    height: 2px;
    background: #0284c7;
    z-index: 1;
  }}

  .timeline-node {{
    position: relative;
    z-index: 2;
    text-align: center;
  }}

  .timeline-year {{
    font-family: 'Oswald', sans-serif;
    font-size: 15px;
    font-weight: 700;
    color: #0284c7;
    margin-bottom: 2px;
    background: #f0f9ff;
    display: inline-block;
    padding: 0 4px;
    position: relative;
    z-index: 3;
  }}

  .timeline-dot {{
    width: 14px;
    height: 14px;
    background: #0284c7;
    border: 3px solid #ffffff;
    border-radius: 50%;
    margin: 0 auto 6px auto;
    box-shadow: 0 0 0 1px #0284c7;
    position: relative;
    z-index: 3;
  }}

  .timeline-text {{
    font-size: 10.2px;
    line-height: 1.3;
    color: #334155;
    text-align: left;
  }}

  .timeline-text strong {{
    color: #0f172a;
    font-weight: 700;
  }}

  /* 2.2 DIAGRAM CELL */
  .cell-diagram-wrap {{
    position: relative;
    display: grid;
    grid-template-columns: 1fr 180px 1fr;
    gap: 12px;
    align-items: center;
    background: #ffffff;
    border-radius: 8px;
    padding: 4px 0;
  }}

  .cell-callout {{
    border: 1.5px solid #94a3b8;
    border-radius: 8px;
    padding: 8px 10px;
    background: #ffffff;
    box-shadow: 0 2px 6px rgba(0,0,0,0.03);
    margin-bottom: 12px;
    position: relative;
  }}

  .callout-header {{
    border: 1.5px solid #64748b;
    border-radius: 999px;
    display: inline-block;
    padding: 1px 10px;
    font-weight: 700;
    font-size: 12px;
    color: #0f172a;
    margin-bottom: 4px;
    background: #f8fafc;
  }}

  .callout-body {{
    font-size: 10.8px;
    line-height: 1.35;
    color: #475569;
  }}

  .cell-center-img {{
    text-align: center;
  }}

  .cell-center-img img {{
    width: 170px;
    height: auto;
    border-radius: 8px;
    filter: drop-shadow(0 4px 10px rgba(0,0,0,0.12));
  }}

  /* FOOTER */
  .page-footer {{
    position: absolute;
    bottom: 8mm;
    left: 18mm;
    right: 18mm;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 10px;
    color: #94a3b8;
    border-top: 1px solid #e2e8f0;
    padding-top: 4px;
  }}

  /* PAGE 2 STYLES */
  .models-grid {{
    display: grid;
    grid-template-columns: 1.15fr 0.85fr;
    gap: 14px;
    margin-bottom: 12px;
  }}

  .cell-type-block {{
    background: #f8fafc;
    border: 1px solid #cbd5e1;
    border-radius: 8px;
    padding: 9px 12px;
    margin-bottom: 10px;
  }}

  .cell-type-pill {{
    display: inline-block;
    border: 1.5px solid #64748b;
    border-radius: 999px;
    padding: 2px 12px;
    font-weight: 700;
    font-size: 12px;
    color: #0f172a;
    margin-bottom: 6px;
    background: #ffffff;
  }}

  .bullets-list {{
    list-style: none;
    font-size: 11px;
    line-height: 1.4;
    color: #334155;
  }}

  .bullets-list li {{
    position: relative;
    padding-left: 14px;
    margin-bottom: 4px;
  }}

  .bullets-list li::before {{
    content: "•";
    position: absolute;
    left: 2px;
    color: #0284c7;
    font-weight: bold;
    font-size: 14px;
    line-height: 1;
  }}

  .bact-img-box {{
    background: #000000;
    border-radius: 8px;
    overflow: hidden;
    text-align: center;
    border: 1.5px solid #334155;
    margin-bottom: 10px;
  }}

  .bact-img-box img {{
    width: 100%;
    height: auto;
    display: block;
  }}

  .bact-caption {{
    background: #0f172a;
    color: #94a3b8;
    font-size: 9.5px;
    padding: 3px 6px;
    text-align: center;
  }}

  /* SECTION ANIMAL & PLANT CELLS */
  .sub-banner {{
    background: #e2e8f0;
    color: #1e293b;
    display: inline-block;
    padding: 3px 10px;
    border-radius: 4px;
    font-family: 'Oswald', sans-serif;
    font-size: 13px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    margin-bottom: 6px;
  }}

  /* 3 CELLS ROW (A, B, C) */
  .cells-triplet {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 8px;
    margin-top: 6px;
    margin-bottom: 10px;
  }}

  .triplet-card {{
    border: 1px solid #cbd5e1;
    border-radius: 6px;
    overflow: hidden;
    background: #ffffff;
  }}

  .triplet-card img {{
    width: 100%;
    height: 120px;
    object-fit: cover;
    display: block;
  }}

  .triplet-label {{
    padding: 5px 6px;
    font-size: 10.5px;
    font-weight: 600;
    color: #0f172a;
    background: #f8fafc;
    border-top: 1px solid #e2e8f0;
  }}

  .triplet-label strong {{
    color: #0284c7;
  }}

  /* BLANCA STUDY BOX */
  .blanca-box {{
    background: #fffbeb;
    border: 1.5px dashed #f59e0b;
    border-radius: 8px;
    padding: 8px 12px;
    margin-top: 6px;
  }}

  .blanca-header {{
    display: flex;
    align-items: center;
    gap: 6px;
    font-size: 11px;
    font-weight: 700;
    color: #b45309;
    text-transform: uppercase;
    margin-bottom: 4px;
  }}

  .blanca-badge {{
    background: #f59e0b;
    color: #ffffff;
    font-size: 9px;
    padding: 1px 6px;
    border-radius: 999px;
    font-weight: 800;
  }}

  .blanca-content {{
    font-size: 10.5px;
    line-height: 1.35;
    color: #78350f;
  }}

</style>
</head>
<body>

  <!-- ==================== PÁGINA 10 ==================== -->
  <div class="page" id="page-10">
    <div class="page-header">
      <span>1 CÉLULAS. REPRODUCCIÓN CELULAR</span>
      <span class="page-number">10</span>
    </div>

    <!-- 2.1 LA TEORÍA CELULAR -->
    <div class="section-banner">
      <span class="sec-num">2.1</span>
      <span class="sec-title">La teoría celular</span>
    </div>

    <p class="intro-p">
      La <strong>teoría celular</strong> define a la célula como la unidad <strong>estructural</strong>, <strong>funcional</strong>, <strong>reproductora</strong> y <strong>genética</strong> de los seres vivos.
    </p>

    <!-- 4 POSTULADOS -->
    <div class="postulates-grid">
      <div class="postulate-card">
        <span class="postulate-pill">Unidad estructural</span>
        <p class="postulate-desc">
          Las células son las unidades básicas de los seres vivos. Esto significa que todos los seres vivos están formados por <strong>al menos una célula</strong>.
        </p>
      </div>

      <div class="postulate-card">
        <span class="postulate-pill">Unidad funcional</span>
        <p class="postulate-desc">
          Las células son las unidades básicas capaces de mantener su propia existencia mediante la <strong>nutrición</strong> y la <strong>relación</strong> (interacción).
        </p>
      </div>

      <div class="postulate-card">
        <span class="postulate-pill">Unidad reproductora</span>
        <p class="postulate-desc">
          Las células son las unidades básicas de reproducción, dado que todas las células provienen de la división de <strong>células preexistentes</strong>.
        </p>
      </div>

      <div class="postulate-card">
        <span class="postulate-pill">Unidad genética</span>
        <p class="postulate-desc">
          Las células son las unidades básicas de la herencia: contienen la <strong>información hereditaria</strong> requerida para regular sus funciones y transmitirla a sus descendientes.
        </p>
      </div>
    </div>

    <!-- CIENTÍFICOS QUE DESARROLLARON LA TEORÍA CELULAR -->
    <div class="timeline-container">
      <div class="timeline-title">Los científicos que desarrollaron la teoría celular</div>
      <div class="timeline-items">
        <!-- 1838 -->
        <div class="timeline-node">
          <div class="timeline-year">1838</div>
          <div class="timeline-dot"></div>
          <p class="timeline-text">
            El botánico alemán <strong>Matthias Schleiden</strong> comenzó a desarrollar la teoría celular en <strong>plantas</strong>. Tras examinar tejido vegetal al microscopio, concluyó que estaban compuestas por unidades individuales: células.
          </p>
        </div>

        <!-- 1839 -->
        <div class="timeline-node">
          <div class="timeline-year">1839</div>
          <div class="timeline-dot"></div>
          <p class="timeline-text">
            El médico alemán <strong>Theodor Schwann</strong> amplió la teoría a todos los <strong>animales</strong> al descubrir que sus tejidos estaban formados por células. La única excepción aparente era el tejido nervioso por su forma reticular.
          </p>
        </div>

        <!-- 1858 -->
        <div class="timeline-node">
          <div class="timeline-year">1858</div>
          <div class="timeline-dot"></div>
          <p class="timeline-text">
            El médico alemán <strong>Rudolf Virchow</strong> amplió la teoría al <strong>origen de las células</strong>: demostró que todas provienen de la división de células preexistentes (<em>omnis cellula e cellula</em>).
          </p>
        </div>

        <!-- 1888 -->
        <div class="timeline-node">
          <div class="timeline-year">1888</div>
          <div class="timeline-dot" style="background:#059669; box-shadow:0 0 0 1px #059669;"></div>
          <p class="timeline-text">
            El médico español <strong>Santiago Ramón y Cajal</strong> generalizó la teoría al demostrar que el <strong>tejido nervioso</strong> también está formado por células individuales (las neuronas), usando técnicas de tinción con nitrato de plata.
          </p>
        </div>
      </div>
    </div>

    <!-- 2.2 COMPONENTES CELULARES BÁSICOS -->
    <div class="section-banner" style="margin-top: 4px;">
      <span class="sec-num">2.2</span>
      <span class="sec-title">Componentes celulares básicos</span>
    </div>

    <p class="intro-p" style="margin-bottom: 8px;">
      Todos los seres vivos están formados por células, pero no todas las células son iguales ni tienen el mismo grado de organización y complejidad. Sin embargo, a pesar de las diferencias entre los diversos tipos de células, todas las células comparten <strong>cuatro componentes esenciales</strong>: una <strong>membrana plasmática</strong>, <strong>citoplasma</strong>, <strong>material genético</strong> y <strong>ribosomas</strong>.
    </p>

    <!-- DIAGRAMA DE LA CÉLULA CON LLAMADAS -->
    <div class="cell-diagram-wrap">
      <!-- Columna Izquierda -->
      <div>
        <div class="cell-callout">
          <span class="callout-header">Membrana plasmática ➔</span>
          <p class="callout-body">
            Esta estructura rodea la célula y controla el intercambio de sustancias hacia dentro y hacia fuera.
          </p>
        </div>

        <div class="cell-callout" style="margin-bottom:0;">
          <span class="callout-header">Citoplasma ➔</span>
          <p class="callout-body">
            Es el fluido del interior celular que contiene todos los componentes y estructuras celulares, y donde tienen lugar las reacciones químicas vitales de la célula.
          </p>
        </div>
      </div>

      <!-- Imagen central -->
      <div class="cell-center-img">
        <img src="{b_celula_basica}" alt="Célula básica">
      </div>

      <!-- Columna Derecha -->
      <div>
        <div class="cell-callout">
          <span class="callout-header">⬅ Material genético</span>
          <p class="callout-body">
            Está formado por moléculas de ácidos nucleicos de la herencia que controlan las funciones celulares y la reproducción.
          </p>
        </div>

        <div class="cell-callout" style="margin-bottom:0;">
          <span class="callout-header">⬅ Ribosomas</span>
          <p class="callout-body">
            Son partículas ribonucleoproteicas (formadas por ARN y proteínas), responsables de la síntesis de proteínas.
          </p>
        </div>
      </div>
    </div>

    <div class="page-footer">
      <span>Biología y Geología 4º ESO • Unidad 2: La Célula</span>
      <span>Página 10 (Traducción al Español)</span>
    </div>
  </div>


  <!-- ==================== PÁGINA 11 ==================== -->
  <div class="page" id="page-11">
    <div class="page-header">
      <span>1 CÉLULAS. REPRODUCCIÓN CELULAR</span>
      <span class="page-number">11</span>
    </div>

    <!-- 2.3 MODELOS DE ORGANIZACIÓN CELULAR -->
    <div class="section-banner">
      <span class="sec-num">2.3</span>
      <span class="sec-title">Modelos de organización celular</span>
    </div>

    <p class="intro-p" style="margin-bottom: 8px;">
      Según su grado de complejidad y su historia evolutiva, existen dos tipos de células: <strong>procariotas</strong> y <strong>eucariotas</strong>.
    </p>

    <!-- COLUMNAS PROCARIOTAS Y BACTERIA + EUCARIOTAS -->
    <div class="models-grid">
      <!-- Columna Izquierda: Texto de ambas -->
      <div>
        <!-- Procariotas -->
        <div class="cell-type-block">
          <span class="cell-type-pill">Células procariotas (Bacterias)</span>
          <ul class="bullets-list">
            <li>No tienen membranas internas y, por lo tanto, carecen de orgánulos citoplasmáticos con membrana.</li>
            <li>No tienen núcleo. Su material genético está localizado en la región central del citoplasma en forma de <strong>nucleoide</strong>, y no está rodeado por ninguna membrana nuclear.</li>
            <li>Miden entre <strong>0,5 µm y 5 µm</strong>.</li>
            <li>Los procariotas son <strong>organismos unicelulares</strong>, como las bacterias.</li>
            <li>No forman organismos pluricelulares.</li>
          </ul>
        </div>

        <!-- Eucariotas -->
        <div class="cell-type-block" style="margin-bottom: 0;">
          <span class="cell-type-pill">Células eucariotas</span>
          <ul class="bullets-list">
            <li>Tienen un núcleo que contiene el material genético, el cual está envuelto por una <strong>doble membrana nuclear</strong>.</li>
            <li>Tienen membranas internas que rodean a los orgánulos citoplasmáticos.</li>
            <li>Tienen, de media, un tamaño <strong>más de diez veces mayor</strong> que el de las células procariotas.</li>
            <li>Forman tanto organismos <strong>unicelulares como pluricelulares</strong>.</li>
            <li>Las células eucariotas pueden pertenecer a <strong>animales o a plantas</strong>.</li>
          </ul>
        </div>
      </div>

      <!-- Columna Derecha: Micrografía de Bacteria -->
      <div>
        <div class="bact-img-box">
          <img src="{b_bacteria}" alt="Bacteria procariota">
          <div class="bact-caption">Micrografía de célula procariota (bacteria con flagelos)</div>
        </div>

        <!-- Tabla resumen manuscrita de Blanca -->
        <div class="blanca-box">
          <div class="blanca-header">
            <span class="blanca-badge">Apuntes de Blanca</span>
            <span>Resumen mnemotécnico</span>
          </div>
          <div class="blanca-content">
            <strong>• Procariotas (Bacterias):</strong> Sin núcleo, sin membrana nuclear, sin orgánulos membranosos, pequeñas, siempre unicelulares.<br>
            <strong>• Eucariotas:</strong> Con núcleo y doble membrana, con orgánulos citoplasmáticos, 10 veces mayores, unicelulares y pluricelulares.
          </div>
        </div>
      </div>
    </div>

    <!-- SECCIÓN CÉLULAS ANIMALES Y VEGETALES -->
    <div class="sub-banner">Células eucariotas animales y vegetales</div>
    <p class="intro-p" style="margin-bottom: 6px;">
      Las células eucariotas animales son <strong>heterótrofas</strong> y suelen tener forma esférica. No obstante, en los organismos pluricelulares, en los que el trabajo se reparte entre células especializadas, la forma celular depende de su función. Por ejemplo, las <strong>células musculares son alargadas</strong> y las <strong>células nerviosas son ramificadas</strong>.
      Por contra, las células eucariotas vegetales son <strong>autótrofas</strong> y tienen forma <strong>poliédrica</strong>.
    </p>

    <!-- FIGURAS A, B, C -->
    <div class="cells-triplet">
      <div class="triplet-card">
        <img src="{b_muscular}" alt="Célula muscular">
        <div class="triplet-label">
          <strong>A. Célula muscular:</strong> Forma alargada para la contracción y movimiento.
        </div>
      </div>

      <div class="triplet-card">
        <img src="{b_nerviosa}" alt="Célula nerviosa">
        <div class="triplet-label">
          <strong>B. Célula nerviosa (neurona):</strong> Ramificada para transmitir impulsos eléctricos.
        </div>
      </div>

      <div class="triplet-card">
        <img src="{b_vegetal}" alt="Célula vegetal">
        <div class="triplet-label">
          <strong>C. Célula vegetal:</strong> Forma poliédrica, autótrofa y con pared celular rígida.
        </div>
      </div>
    </div>

    <!-- GLOSARIO CLAVE -->
    <div style="background:#f1f5f9; border-radius:6px; padding:6px 10px; font-size:10.5px; color:#475569; display:flex; justify-content:space-around;">
      <span><strong>Heterótrofa:</strong> no produce su propio alimento; toma materia orgánica de otras fuentes.</span>
      <span><strong>Autótrofa:</strong> produce su propio alimento mediante fotosíntesis.</span>
    </div>

    <div class="page-footer">
      <span>Biología y Geología 4º ESO • Unidad 2: La Célula</span>
      <span>Página 11 (Traducción al Español)</span>
    </div>
  </div>

</body>
</html>
"""

with open("libro_espanol.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("HTML actualizado con exito.")
