import os
import base64
import subprocess

def img_b64(path):
    if not os.path.exists(path):
        return ""
    with open(path, "rb") as f:
        ext = "png" if path.endswith(".png") else "jpeg"
        return f"data:image/{ext};base64," + base64.b64encode(f.read()).decode('utf-8')

# Load all images
b_celula_basica = img_b64("fotos/celula_basica.png")
b_bacteria = img_b64("fotos/bacteria_procariota.png")
b_muscular = img_b64("fotos/celula_muscular_A.png")
b_nerviosa = img_b64("fotos/celula_nerviosa_B.png")
b_vegetal = img_b64("fotos/celula_vegetal_C.png")

b_membrana = img_b64("fotos/membrana_mosaico_fluido.png")
b_transporte = img_b64("fotos/transporte_membrana.png")
b_endocitosis = img_b64("fotos/endocitosis_exocitosis.png")
b_pared = img_b64("fotos/pared_celular_microscopio.png")

b_citoesq_diag = img_b64("fotos/citoesqueleto_diagrama.png")
b_citoesq_micro = img_b64("fotos/citoesqueleto_micrografia.png")

b_reticulo_diag = img_b64("fotos/reticulo_endoplasmatico.png")
b_reticulo_micro = img_b64("fotos/reticulo_micrografia.png")
b_golgi_diag = img_b64("fotos/golgi_diagrama.png")
b_golgi_micro = img_b64("fotos/golgi_micrografia.png")

b_lisosomas_micro = img_b64("fotos/lisosomas_micrografia.png")
b_mitoc_diag = img_b64("fotos/mitocondria_diagrama.png")
b_mitoc_micro = img_b64("fotos/mitocondria_micrografia.png")

b_cloro_diag = img_b64("fotos/cloroplasto_diagrama.png")
b_cloro_micro = img_b64("fotos/cloroplasto_micrografia.png")
b_endosimbiotica = img_b64("fotos/teoria_endosimbiotica.png")

b_ribos_diag = img_b64("fotos/ribosoma_diagrama.png")
b_ribos_micro = img_b64("fotos/ribosomas_micrografia.png")
b_centro_diag = img_b64("fotos/centrosoma_diagrama.png")
b_centro_micro = img_b64("fotos/centriolos_micrografia.png")

html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Tema 2: La Célula - Libro Completo (Páginas 10 a 18 en Español)</title>
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
    padding: 15mm 17mm 13mm 17mm;
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
    padding-bottom: 5px;
    margin-bottom: 12px;
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

  /* BANNERS */
  .section-banner {{
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: #0284c7;
    color: #ffffff;
    padding: 3px 12px 3px 6px;
    border-radius: 4px;
    margin-bottom: 8px;
  }}

  .unit-main-banner {{
    background: #1e293b;
    color: #ffffff;
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 4px 14px;
    border-radius: 4px;
    font-family: 'Oswald', sans-serif;
    font-size: 17px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-bottom: 8px;
  }}

  .sec-num {{
    background: #ffffff;
    color: #0284c7;
    font-family: 'Oswald', sans-serif;
    font-weight: 700;
    font-size: 16px;
    padding: 2px 7px;
    border-radius: 3px;
    line-height: 1;
  }}

  .sec-title {{
    font-family: 'Oswald', sans-serif;
    font-size: 17px;
    font-weight: 700;
    letter-spacing: 0.04em;
    text-transform: uppercase;
  }}

  .intro-p {{
    font-size: 11.8px;
    line-height: 1.4;
    color: #334155;
    margin-bottom: 9px;
  }}

  /* POSTULATES */
  .postulates-grid {{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 7px;
    margin-bottom: 11px;
  }}

  .postulate-card {{
    background: #f8fafc;
    border: 1.5px solid #cbd5e1;
    border-radius: 8px;
    padding: 7px 7px;
    text-align: center;
  }}

  .postulate-pill {{
    display: inline-block;
    border: 1.5px solid #64748b;
    border-radius: 999px;
    padding: 2px 8px;
    font-weight: 700;
    font-size: 11px;
    color: #0f172a;
    margin: 0 auto 5px auto;
    background: #ffffff;
  }}

  .postulate-desc {{
    font-size: 10.5px;
    line-height: 1.3;
    color: #475569;
    text-align: left;
  }}

  /* TIMELINE */
  .timeline-container {{
    border: 1.5px solid #0284c7;
    border-radius: 8px;
    padding: 9px 12px;
    background: #f0f9ff;
    margin-bottom: 12px;
  }}

  .timeline-title {{
    font-family: 'Oswald', sans-serif;
    font-size: 13px;
    color: #0369a1;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-bottom: 6px;
    font-weight: 700;
  }}

  .timeline-items {{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 8px;
    position: relative;
  }}

  .timeline-items::before {{
    content: '';
    position: absolute;
    top: 25px;
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
    font-size: 14px;
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
    width: 13px;
    height: 13px;
    background: #0284c7;
    border: 3px solid #ffffff;
    border-radius: 50%;
    margin: 0 auto 5px auto;
    box-shadow: 0 0 0 1px #0284c7;
    position: relative;
    z-index: 3;
  }}

  .timeline-text {{
    font-size: 10px;
    line-height: 1.25;
    color: #334155;
    text-align: left;
  }}

  /* CELL DIAGRAM */
  .cell-diagram-wrap {{
    display: grid;
    grid-template-columns: 1fr 170px 1fr;
    gap: 10px;
    align-items: center;
    background: #ffffff;
    padding: 4px 0;
  }}

  .cell-callout {{
    border: 1.5px solid #94a3b8;
    border-radius: 8px;
    padding: 7px 9px;
    background: #ffffff;
    margin-bottom: 10px;
  }}

  .callout-header {{
    border: 1.5px solid #64748b;
    border-radius: 999px;
    display: inline-block;
    padding: 1px 9px;
    font-weight: 700;
    font-size: 11.5px;
    color: #0f172a;
    margin-bottom: 3px;
    background: #f8fafc;
  }}

  .callout-body {{
    font-size: 10.5px;
    line-height: 1.3;
    color: #475569;
  }}

  .cell-center-img img {{
    width: 160px;
    height: auto;
    border-radius: 8px;
    filter: drop-shadow(0 4px 8px rgba(0,0,0,0.12));
    display: block;
    margin: 0 auto;
  }}

  /* FOOTER */
  .page-footer {{
    position: absolute;
    bottom: 7mm;
    left: 17mm;
    right: 17mm;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 9.5px;
    color: #94a3b8;
    border-top: 1px solid #e2e8f0;
    padding-top: 3px;
  }}

  /* PAGE 2 STYLES */
  .models-grid {{
    display: grid;
    grid-template-columns: 1.15fr 0.85fr;
    gap: 12px;
    margin-bottom: 10px;
  }}

  .cell-type-block {{
    background: #f8fafc;
    border: 1px solid #cbd5e1;
    border-radius: 8px;
    padding: 8px 10px;
    margin-bottom: 8px;
  }}

  .cell-type-pill {{
    display: inline-block;
    border: 1.5px solid #64748b;
    border-radius: 999px;
    padding: 2px 10px;
    font-weight: 700;
    font-size: 11.5px;
    color: #0f172a;
    margin-bottom: 5px;
    background: #ffffff;
  }}

  .bullets-list {{
    list-style: none;
    font-size: 10.5px;
    line-height: 1.35;
    color: #334155;
  }}

  .bullets-list li {{
    position: relative;
    padding-left: 13px;
    margin-bottom: 3px;
  }}

  .bullets-list li::before {{
    content: "•";
    position: absolute;
    left: 2px;
    color: #0284c7;
    font-weight: bold;
    font-size: 13px;
    line-height: 1;
  }}

  .bact-img-box {{
    background: #000;
    border-radius: 8px;
    overflow: hidden;
    text-align: center;
    border: 1.5px solid #334155;
    margin-bottom: 8px;
  }}

  .bact-img-box img {{
    width: 100%;
    height: auto;
    display: block;
  }}

  .bact-caption {{
    background: #0f172a;
    color: #94a3b8;
    font-size: 9px;
    padding: 3px 6px;
    text-align: center;
  }}

  .sub-banner {{
    background: #e2e8f0;
    color: #1e293b;
    display: inline-block;
    padding: 3px 9px;
    border-radius: 4px;
    font-family: 'Oswald', sans-serif;
    font-size: 12.5px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    margin-bottom: 5px;
  }}

  .cells-triplet {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 7px;
    margin-top: 5px;
    margin-bottom: 8px;
  }}

  .triplet-card {{
    border: 1px solid #cbd5e1;
    border-radius: 6px;
    overflow: hidden;
    background: #ffffff;
  }}

  .triplet-card img {{
    width: 100%;
    height: 110px;
    object-fit: cover;
    display: block;
  }}

  .triplet-label {{
    padding: 4px 6px;
    font-size: 10px;
    font-weight: 600;
    color: #0f172a;
    background: #f8fafc;
    border-top: 1px solid #e2e8f0;
  }}

  .triplet-label strong {{
    color: #0284c7;
  }}

  .blanca-box {{
    background: #fffbeb;
    border: 1.5px dashed #f59e0b;
    border-radius: 7px;
    padding: 7px 10px;
    margin-top: 5px;
  }}

  .blanca-header {{
    display: flex;
    align-items: center;
    gap: 5px;
    font-size: 10.5px;
    font-weight: 700;
    color: #b45309;
    text-transform: uppercase;
    margin-bottom: 3px;
  }}

  .blanca-badge {{
    background: #f59e0b;
    color: #ffffff;
    font-size: 8.5px;
    padding: 1px 5px;
    border-radius: 999px;
    font-weight: 800;
  }}

  .blanca-content {{
    font-size: 10px;
    line-height: 1.3;
    color: #78350f;
  }}

  /* REUSABLE STYLES FOR PAGES 12 - 18 */
  .diagram-full {{
    width: 100%;
    border-radius: 7px;
    border: 1px solid #cbd5e1;
    display: block;
    margin: 6px 0;
  }}

  .two-col-layout {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin-bottom: 10px;
  }}

  .three-col-layout {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 8px;
    margin-bottom: 10px;
  }}

  .organelle-card {{
    background: #f8fafc;
    border: 1px solid #cbd5e1;
    border-radius: 7px;
    padding: 8px 10px;
    margin-bottom: 10px;
  }}

  .organelle-title {{
    font-family: 'Oswald', sans-serif;
    font-size: 14px;
    font-weight: 700;
    color: #0369a1;
    text-transform: uppercase;
    margin-bottom: 4px;
    display: flex;
    align-items: center;
    gap: 5px;
  }}

  .organelle-pill {{
    background: #e0f2fe;
    color: #0284c7;
    font-size: 10px;
    padding: 1px 7px;
    border-radius: 999px;
    font-weight: 700;
  }}

  .micrograph-box {{
    border-radius: 6px;
    overflow: hidden;
    border: 1px solid #94a3b8;
    background: #0f172a;
    text-align: center;
  }}

  .micrograph-box img {{
    width: 100%;
    display: block;
  }}

  .micrograph-caption {{
    font-size: 9px;
    color: #94a3b8;
    padding: 3px 5px;
    background: #1e293b;
  }}

  .chem-eq {{
    background: #f0fdf4;
    border: 1.5px solid #86efac;
    border-radius: 6px;
    padding: 6px 12px;
    text-align: center;
    font-family: 'Fira Sans', monospace;
    font-weight: 700;
    font-size: 12px;
    color: #166534;
    margin: 6px 0;
  }}

  .highlight-badge {{
    background: #e0f2fe;
    border-left: 3px solid #0284c7;
    padding: 5px 8px;
    font-size: 10.5px;
    color: #0369a1;
    border-radius: 0 4px 4px 0;
    margin-bottom: 6px;
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

    <div class="section-banner">
      <span class="sec-num">2.1</span>
      <span class="sec-title">La teoría celular</span>
    </div>

    <p class="intro-p">
      La <strong>teoría celular</strong> define a la célula como la unidad <strong>estructural</strong>, <strong>funcional</strong>, <strong>reproductora</strong> y <strong>genética</strong> de los seres vivos.
    </p>

    <div class="postulates-grid">
      <div class="postulate-card">
        <span class="postulate-pill">Unidad estructural</span>
        <p class="postulate-desc">
          Las células son las unidades básicas de los seres vivos: todos los organismos están formados por <strong>al menos una célula</strong>.
        </p>
      </div>
      <div class="postulate-card">
        <span class="postulate-pill">Unidad funcional</span>
        <p class="postulate-desc">
          Capaces de mantener su propia existencia realizando las funciones vitales de <strong>nutrición</strong> y <strong>relación</strong>.
        </p>
      </div>
      <div class="postulate-card">
        <span class="postulate-pill">Unidad reproductora</span>
        <p class="postulate-desc">
          Toda célula proviene de la división de <strong>células preexistentes</strong> (no por generación espontánea).
        </p>
      </div>
      <div class="postulate-card">
        <span class="postulate-pill">Unidad genética</span>
        <p class="postulate-desc">
          Contienen la <strong>información hereditaria (ADN)</strong> que regula sus funciones y la transmiten a sus descendientes.
        </p>
      </div>
    </div>

    <div class="timeline-container">
      <div class="timeline-title">Los científicos que desarrollaron la teoría celular</div>
      <div class="timeline-items">
        <div class="timeline-node">
          <div class="timeline-year">1838</div>
          <div class="timeline-dot"></div>
          <p class="timeline-text">
            <strong>Matthias Schleiden</strong> (Botánico): Inició la teoría celular en <strong>plantas</strong> al descubrir que todo tejido vegetal está formado por células.
          </p>
        </div>
        <div class="timeline-node">
          <div class="timeline-year">1839</div>
          <div class="timeline-dot"></div>
          <p class="timeline-text">
            <strong>Theodor Schwann</strong> (Médico): La extendió a todos los <strong>animales</strong>. La excepción aparente era el tejido nervioso reticular.
          </p>
        </div>
        <div class="timeline-node">
          <div class="timeline-year">1858</div>
          <div class="timeline-dot"></div>
          <p class="timeline-text">
            <strong>Rudolf Virchow</strong> (Médico): Origen celular: toda célula procede de otra preexistente (<em>omnis cellula e cellula</em>).
          </p>
        </div>
        <div class="timeline-node">
          <div class="timeline-year">1888</div>
          <div class="timeline-dot" style="background:#059669; box-shadow:0 0 0 1px #059669;"></div>
          <p class="timeline-text">
            <strong>Santiago Ramón y Cajal</strong> (Médico español): Universalizó la teoría: demostró que el <strong>tejido nervioso</strong> son células individuales (neuronas).
          </p>
        </div>
      </div>
    </div>

    <div class="section-banner" style="margin-top: 4px;">
      <span class="sec-num">2.2</span>
      <span class="sec-title">Componentes celulares básicos</span>
    </div>

    <p class="intro-p" style="margin-bottom: 6px;">
      A pesar de su enorme variedad, todas las células de la biosfera comparten <strong>cuatro componentes esenciales</strong>:
    </p>

    <div class="cell-diagram-wrap">
      <div>
        <div class="cell-callout">
          <span class="callout-header">Membrana plasmática ➔</span>
          <p class="callout-body">Estructura que rodea la célula y controla el intercambio de sustancias hacia dentro y hacia fuera.</p>
        </div>
        <div class="cell-callout" style="margin-bottom:0;">
          <span class="callout-header">Citoplasma ➔</span>
          <p class="callout-body">Fluido interior que contiene los orgánulos y donde ocurren las reacciones químicas vitales.</p>
        </div>
      </div>
      <div class="cell-center-img">
        <img src="{b_celula_basica}" alt="Célula básica">
      </div>
      <div>
        <div class="cell-callout">
          <span class="callout-header">⬅ Material genético</span>
          <p class="callout-body">Ácidos nucleicos (ADN) que contienen las instrucciones hereditarias para la función y reproducción.</p>
        </div>
        <div class="cell-callout" style="margin-bottom:0;">
          <span class="callout-header">⬅ Ribosomas</span>
          <p class="callout-body">Partículas de ARN y proteínas responsables de la síntesis de proteínas.</p>
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

    <div class="section-banner">
      <span class="sec-num">2.3</span>
      <span class="sec-title">Modelos de organización celular</span>
    </div>

    <p class="intro-p" style="margin-bottom: 6px;">
      Según su complejidad estructural y su historia evolutiva, existen dos modelos celulares: <strong>procariotas</strong> y <strong>eucariotas</strong>.
    </p>

    <div class="models-grid">
      <div>
        <div class="cell-type-block">
          <span class="cell-type-pill">Células procariotas (Bacterias)</span>
          <ul class="bullets-list">
            <li>No tienen membranas internas: carecen de orgánulos citoplasmáticos con membrana.</li>
            <li><strong>Sin núcleo:</strong> ADN ubicado en el citoplasma en forma de <strong>nucleoide</strong>, sin membrana nuclear.</li>
            <li>Tamaño muy pequeño: entre <strong>0,5 µm y 5 µm</strong>.</li>
            <li>Organismos <strong>siempre unicelulares</strong> (bacterias y arqueas).</li>
            <li>No forman jamás organismos pluricelulares.</li>
          </ul>
        </div>

        <div class="cell-type-block" style="margin-bottom: 0;">
          <span class="cell-type-pill">Células eucariotas</span>
          <ul class="bullets-list">
            <li><strong>Con núcleo verdadero:</strong> ADN encerrado por una <strong>doble membrana nuclear</strong>.</li>
            <li>Poseen orgánulos citoplasmáticos complejos rodeados por membranas internas.</li>
            <li>Tamaño <strong>más de 10 veces mayor</strong> que procariotas (aprox. 10 a 50 µm).</li>
            <li>Forman tanto organismos <strong>unicelulares como pluricelulares</strong>.</li>
            <li>Presentes en animales, plantas, hongos y protoctistas.</li>
          </ul>
        </div>
      </div>

      <div>
        <div class="bact-img-box">
          <img src="{b_bacteria}" alt="Bacteria procariota">
          <div class="bact-caption">Micrografía de bacteria procariota con flagelos</div>
        </div>

        <div class="blanca-box">
          <div class="blanca-header">
            <span class="blanca-badge">Apuntes de Blanca</span>
            <span>Resumen mnemotécnico</span>
          </div>
          <div class="blanca-content">
            <strong>• Procariotas (Bacterias):</strong> Sin núcleo, sin membrana nuclear, sin orgánulos membranosos, pequeñas, siempre unicelulares.<br>
            <strong>• Eucariotas:</strong> Con núcleo y doble membrana, con orgánulos citoplasmáticos, 10x mayores, unicelulares y pluricelulares.
          </div>
        </div>
      </div>
    </div>

    <div class="sub-banner">Células eucariotas animales y vegetales</div>
    <p class="intro-p" style="margin-bottom: 5px;">
      Las células animales son <strong>heterótrofas</strong> y comúnmente esféricas, pero en seres pluricelulares su forma se adapta a su función: las <strong>células musculares son alargadas</strong> y las <strong>células nerviosas son ramificadas</strong>. Las células vegetales son <strong>autótrofas</strong> y de forma <strong>poliédrica</strong>.
    </p>

    <div class="cells-triplet">
      <div class="triplet-card">
        <img src="{b_muscular}" alt="Célula muscular">
        <div class="triplet-label">
          <strong>A. Célula muscular:</strong> Alargada (contracción y movimiento).
        </div>
      </div>
      <div class="triplet-card">
        <img src="{b_nerviosa}" alt="Célula nerviosa">
        <div class="triplet-label">
          <strong>B. Célula nerviosa (neurona):</strong> Ramificada (impulsos eléctricos).
        </div>
      </div>
      <div class="triplet-card">
        <img src="{b_vegetal}" alt="Célula vegetal">
        <div class="triplet-label">
          <strong>C. Célula vegetal:</strong> Poliédrica (autótrofa con pared celular).
        </div>
      </div>
    </div>

    <div style="background:#f1f5f9; border-radius:6px; padding:5px 8px; font-size:10px; color:#475569; display:flex; justify-content:space-around;">
      <span><strong>Heterótrofa:</strong> no produce su propio alimento; toma materia orgánica externa.</span>
      <span><strong>Autótrofa:</strong> produce su propio alimento orgánico por fotosíntesis.</span>
    </div>

    <div class="page-footer">
      <span>Biología y Geología 4º ESO • Unidad 2: La Célula</span>
      <span>Página 11 (Traducción al Español)</span>
    </div>
  </div>


  <!-- ==================== PÁGINA 12 ==================== -->
  <div class="page" id="page-12">
    <div class="page-header">
      <span>1 CÉLULAS. REPRODUCCIÓN CELULAR</span>
      <span class="page-number">12</span>
    </div>

    <div class="unit-main-banner">
      <span>3 /// Células eucariotas (Eukaryotic Cells)</span>
    </div>

    <p class="intro-p">
      Las células eucariotas están rodeadas por una <strong>membrana plasmática</strong> y poseen un <strong>núcleo</strong> y un <strong>citoplasma</strong>. También pueden tener una <strong>pared celular</strong>, así como <strong>cilios y flagelos</strong>. El citoplasma está formado por el citosol, el citoesqueleto y los <strong>orgánulos citoplasmáticos</strong> (que pueden tener membrana simple, doble o carecer de ella).
    </p>

    <div class="section-banner">
      <span class="sec-num">3.1</span>
      <span class="sec-title">Membrana plasmática (Plasma Membrane)</span>
    </div>

    <p class="intro-p">
      La membrana plasmática es un <strong>complejo supramolecular</strong> formado por <strong>lípidos</strong> y <strong>proteínas</strong> que envuelve a la célula. Estructuralmente es una <strong>bicapa fluida de fosfolípidos</strong> en la cual las proteínas se disponen de forma irregular y asimétrica (<em>modelo del mosaico fluido</em>).
    </p>

    <div class="highlight-badge">
      En células animales, la membrana contiene además cantidades variables de <strong>colesterol</strong> y cadenas cortas de glúcidos (<strong>oligosacáridos</strong>) unidos a su superficie externa (glucocálix).
    </div>

    <div class="organelle-card">
      <div class="organelle-title">Funciones principales de la membrana:</div>
      <ul class="bullets-list" style="font-size: 11px;">
        <li><strong>1. Rodear y proteger la célula:</strong> Actúa como barrera física que aísla el medio intracelular del extracelular.</li>
        <li><strong>2. Mantener la forma celular:</strong> Proporciona estabilidad y forma a la célula.</li>
        <li><strong>3. Regular el intercambio de sustancias:</strong> Controla selectivamente lo que entra y sale de la célula (transporte).</li>
        <li><strong>4. Transmitir señales:</strong> Capta estímulos externos y transmite señales hacia el interior y hacia el exterior.</li>
        <li><strong>5. Reconocimiento celular:</strong> Permite que la célula sea reconocible e identificable (antígenos celulares).</li>
        <li><strong>6. Comunicación y adhesión:</strong> En pluricelulares, favorece la adhesión y la comunicación con las células vecinas mediante uniones intercelulares especializadas.</li>
      </ul>
    </div>

    <div style="margin-top: 10px;">
      <div style="font-family:'Oswald'; font-size:12.5px; color:#0369a1; text-transform:uppercase; margin-bottom:4px;">
        Estructura de la Membrana Plasmática (Modelo del Mosaico Fluido)
      </div>
      <img src="{b_membrana}" alt="Membrana plasmática" style="width:100%; border-radius:6px; border:1.5px solid #cbd5e1;">
      <div style="display:flex; justify-content:space-between; font-size:9.5px; color:#64748b; margin-top:2px;">
        <span>Superficie exterior: Glúcidos (oligosacáridos) + Proteínas</span>
        <span>Bicapa de fosfolípidos con colesterol</span>
        <span>Superficie interior citoplasmática</span>
      </div>
    </div>

    <div class="page-footer">
      <span>Biología y Geología 4º ESO • Unidad 2: La Célula</span>
      <span>Página 12 (Traducción al Español)</span>
    </div>
  </div>


  <!-- ==================== PÁGINA 13 ==================== -->
  <div class="page" id="page-13">
    <div class="page-header">
      <span>1 CÉLULAS. REPRODUCCIÓN CELULAR</span>
      <span class="page-number">13</span>
    </div>

    <div class="sub-banner">Transporte a través de la membrana</div>
    <p class="intro-p">
      La membrana plasmática es semipermeable y selectiva:
    </p>

    <div class="two-col-layout">
      <div class="organelle-card">
        <div class="organelle-title">Sustancias pequeñas</div>
        <p style="font-size:10.5px; line-height:1.35; color:#334155; margin-bottom:6px;">
          Atraviesan directamente entre los fosfolípidos de la bicapa (ej. gases como O₂ y CO₂) o a través de canales formados por proteínas de transporte (ej. agua H₂O, iones, glucosa y aminoácidos).
        </p>
        <img src="{b_transporte}" alt="Transporte de sustancias pequeñas" style="width:100%; border-radius:5px; border:1px solid #cbd5e1;">
      </div>

      <div class="organelle-card">
        <div class="organelle-title">Partículas de gran tamaño</div>
        <p style="font-size:10.5px; line-height:1.35; color:#334155; margin-bottom:6px;">
          Entran por <strong>endocitosis</strong> y salen por <strong>exocitosis</strong>. La membrana se deforma para envolver partículas en pequeñas vesículas que facilitan su transporte.
        </p>
        <img src="{b_endocitosis}" alt="Endocitosis y exocitosis" style="width:100%; border-radius:5px; border:1px solid #cbd5e1;">
      </div>
    </div>

    <div class="section-banner">
      <span class="sec-num">3.2</span>
      <span class="sec-title">Cubiertas celulares / Pared celular (Cell Coverings)</span>
    </div>

    <p class="intro-p">
      Las cubiertas celulares son paredes gruesas y rígidas que rodean la membrana plasmática por su parte externa. Están compuestas principalmente por <strong>glúcidos (carbohidratos)</strong>:
    </p>

    <div class="two-col-layout" style="margin-bottom: 6px;">
      <div>
        <ul class="bullets-list">
          <li><strong>Pared celular bacteriana (procariotas):</strong> Formada por un carbohidrato complejo unido a cadenas cortas de aminoácidos, denominado <strong>peptidoglicano (mureína)</strong>, dispuesto en forma de malla o red.</li>
          <li><strong>Pared celular vegetal (plantas):</strong> Formada por fibras del polisacárido <strong>celulosa</strong>.</li>
          <li><strong>Pared celular fúngica (hongos):</strong> Formada por fibras del polisacárido <strong>quitina</strong>.</li>
          <li>Los espacios entre las fibras están rellenos por una <strong>matriz amorfa</strong>.</li>
        </ul>

        <div class="organelle-card" style="margin-top: 6px; padding: 6px 8px;">
          <strong style="font-size:11px; color:#0369a1;">Funciones principales de la pared celular:</strong>
          <ul class="bullets-list" style="margin-top: 3px;">
            <li>Dar forma, uniformidad y resistencia estructural a la célula y al organismo.</li>
            <li>Limitar y prevenir la entrada de moléculas tóxicas y microorganismos patógenos.</li>
          </ul>
        </div>
      </div>

      <div>
        <div class="micrograph-box">
          <img src="{b_pared}" alt="Pared celular de patata">
          <div class="micrograph-caption">Pared celular de células de patata y fibras de celulosa al microscopio electrónico</div>
        </div>

        <div class="blanca-box" style="margin-top: 5px;">
          <div class="blanca-header">
            <span class="blanca-badge">Apuntes de Blanca</span>
            <span>Glosario Bioquímico</span>
          </div>
          <div class="blanca-content">
            • <strong>Aminoácido:</strong> moléculas que se combinan para formar proteínas.<br>
            • <strong>Proteína:</strong> moléculas grandes y complejas con función estructural/enzimática.<br>
            • <strong>Lípido:</strong> compuesto orgánico de C, H y O (insoluble en agua).
          </div>
        </div>
      </div>
    </div>

    <div class="page-footer">
      <span>Biología y Geología 4º ESO • Unidad 2: La Célula</span>
      <span>Página 13 (Traducción al Español)</span>
    </div>
  </div>


  <!-- ==================== PÁGINA 14 ==================== -->
  <div class="page" id="page-14">
    <div class="page-header">
      <span>1 CÉLULAS. REPRODUCCIÓN CELULAR</span>
      <span class="page-number">14</span>
    </div>

    <div class="section-banner">
      <span class="sec-num">3.3</span>
      <span class="sec-title">Citoplasma (Cytoplasm)</span>
    </div>

    <p class="intro-p">
      El <strong>citoplasma</strong> es la región de la célula comprendida entre la membrana plasmática y el núcleo. Contiene el <strong>citosol</strong>, el <strong>citoesqueleto</strong> y los <strong>orgánulos citoplasmáticos</strong>.
    </p>

    <div class="organelle-card">
      <div class="organelle-title">Citosol o hialoplasma (Cytosol / Hyaloplasm)</div>
      <p style="font-size:11px; line-height:1.35; color:#334155;">
        Es la matriz acuosa formada por agua, sales minerales, glúcidos, lípidos, aminoácidos, nucleótidos, ácidos ribonucleicos (ARN) y proteínas. En él tienen lugar la mayor parte de las reacciones químicas del metabolismo celular.
      </p>
    </div>

    <div class="organelle-card">
      <div class="organelle-title">Citoesqueleto (Cytoskeleton)</div>
      <p style="font-size:11px; line-height:1.35; color:#334155; margin-bottom: 5px;">
        Es un armazón tridimensional de filamentos proteicos que recorre el hialoplasma en todas las células eucariotas. Es una estructura dinámica que se ensambla y reorganiza continuamente según las necesidades de la célula.
      </p>
      <div style="font-size:10.5px; color:#0369a1; font-weight:700;">Funciones principales:</div>
      <ul class="bullets-list" style="font-size:10.5px;">
        <li>Servir de soporte y anclaje a los orgánulos celulares.</li>
        <li>Mantener y modificar la forma de la célula.</li>
        <li>Permitir el tránsito de sustancias y vesículas a través del citoplasma.</li>
      </ul>
    </div>

    <div style="font-family:'Oswald'; font-size:12.5px; color:#0369a1; text-transform:uppercase; margin-bottom:4px;">
      Los 3 Tipos de Filamentos del Citoesqueleto
    </div>

    <div class="three-col-layout">
      <div class="organelle-card">
        <div class="postulate-pill" style="display:block; text-align:center;">Microfilamentos</div>
        <p style="font-size:10px; color:#475569; line-height:1.3;">
          Formados por polimerización en doble hélice de la proteína <strong>actina</strong>. Son los <strong>más delgados y frágiles</strong>. Participan en la deformación celular y movimiento.
        </p>
      </div>

      <div class="organelle-card">
        <div class="postulate-pill" style="display:block; text-align:center;">Filamentos intermedios</div>
        <p style="font-size:10px; color:#475569; line-height:1.3;">
          Presentes solo en células animales, con aspecto de cuerdas. Formados por proteínas como la <strong>citoqueratina</strong>. Son los <strong>más resistentes</strong> del citoesqueleto.
        </p>
      </div>

      <div class="organelle-card">
        <div class="postulate-pill" style="display:block; text-align:center;">Microtúbulos</div>
        <p style="font-size:10px; color:#475569; line-height:1.3;">
          Cilindros huecos y rígidos formados por la proteína <strong>tubulina</strong>. Son los <strong>más gruesos</strong>. Forman el huso mitótico, el centrosoma, cilios y flagelos.
        </p>
      </div>
    </div>

    <div class="two-col-layout">
      <div>
        <img src="{b_citoesq_diag}" alt="Diagrama del citoesqueleto" style="width:100%; border-radius:6px; border:1px solid #cbd5e1;">
        <p style="font-size:9.5px; color:#64748b; text-align:center; margin-top:2px;">
          Armazón del citoesqueleto sosteniendo mitocondrias, retículo, lisosomas y ribosomas.
        </p>
      </div>
      <div>
        <div class="micrograph-box">
          <img src="{b_citoesq_micro}" alt="Micrografía del citoesqueleto">
          <div class="micrograph-caption">Micrografía óptica de fluorescencia: microtúbulos en amarillo y microfilamentos en azul</div>
        </div>
      </div>
    </div>

    <div class="page-footer">
      <span>Biología y Geología 4º ESO • Unidad 2: La Célula</span>
      <span>Página 14 (Traducción al Español)</span>
    </div>
  </div>


  <!-- ==================== PÁGINA 15 ==================== -->
  <div class="page" id="page-15">
    <div class="page-header">
      <span>1 CÉLULAS. REPRODUCCIÓN CELULAR</span>
      <span class="page-number">15</span>
    </div>

    <div class="sub-banner">Orgánulos citoplasmáticos (Solo en Eucariotas)</div>
    <p class="intro-p" style="margin-bottom:6px;">
      Los orgánulos citoplasmáticos incluyen el retículo endoplasmático, el aparato de Golgi, los lisosomas, las vacuolas, las mitocondrias, los cloroplastos, los ribosomas y el centrosoma.
    </p>

    <!-- 1. RETÍCULO ENDOPLASMÁTICO -->
    <div class="organelle-card">
      <div class="organelle-title">
        <span>1. Retículo endoplasmático (Endoplasmic Reticulum)</span>
        <span class="organelle-pill">Membrana simple</span>
      </div>
      <p style="font-size:10.8px; line-height:1.35; color:#334155; margin-bottom:5px;">
        Sistema de sacos membranosos y túbulos delimitados por una membrana simple en el citosol, interconectados entre sí y comunicados con la envoltura nuclear. Existen dos tipos:
      </p>

      <div class="two-col-layout" style="margin-bottom: 5px;">
        <div style="background:#fff; border:1px solid #cbd5e1; border-radius:6px; padding:6px;">
          <strong style="color:#0284c7; font-size:11px;">REL: Retículo endoplasmático liso</strong>
          <p style="font-size:10px; color:#475569; line-height:1.3;">
            Carece de ribosomas en su membrana. Función: sintetizar los <strong>lípidos de membrana</strong> y detoxificar o destruir sustancias tóxicas.
          </p>
        </div>
        <div style="background:#fff; border:1px solid #cbd5e1; border-radius:6px; padding:6px;">
          <strong style="color:#0284c7; font-size:11px;">RER: Retículo endoplasmático rugoso</strong>
          <p style="font-size:10px; color:#475569; line-height:1.3;">
            Con ribosomas adheridos a su cara externa. Función: sintetizar, procesar y secretar <strong>proteínas de membrana y secreción</strong>.
          </p>
        </div>
      </div>

      <div class="two-col-layout" style="margin-bottom:0;">
        <img src="{b_reticulo_diag}" alt="Diagrama del retículo" style="width:100%; border-radius:5px; border:1px solid #cbd5e1;">
        <div class="micrograph-box">
          <img src="{b_reticulo_micro}" alt="Micrografía de RER">
          <div class="micrograph-caption">Micrografía electrónica del retículo endoplasmático rugoso</div>
        </div>
      </div>
    </div>

    <!-- 2. APARATO DE GOLGI -->
    <div class="organelle-card" style="margin-bottom:0;">
      <div class="organelle-title">
        <span>2. Aparato de Golgi (Golgi Body)</span>
        <span class="organelle-pill">Membrana simple</span>
      </div>
      <p style="font-size:10.8px; line-height:1.35; color:#334155; margin-bottom:5px;">
        Formado por unidades estructurales llamadas <strong>dictiosomas</strong> (apilamientos de sacos discoidales delimitados por membrana lisa). Presenta dos caras funcionales:
      </p>

      <div class="two-col-layout" style="margin-bottom: 5px;">
        <div style="background:#fff; border:1px solid #cbd5e1; border-radius:6px; padding:6px;">
          <strong style="color:#0284c7; font-size:11px;">Cara Cis (de formación):</strong>
          <p style="font-size:10px; color:#475569; line-height:1.3;">
            Próxima al RER. Recibe las proteínas fabricadas en el RER empaquetadas en pequeñas <strong>vesículas de transición</strong>.
          </p>
        </div>
        <div style="background:#fff; border:1px solid #cbd5e1; border-radius:6px; padding:6px;">
          <strong style="color:#0284c7; font-size:11px;">Cara Trans (de maduración):</strong>
          <p style="font-size:10px; color:#475569; line-height:1.3;">
            Opuesta a la cara cis, orientada a la membrana. Libera <strong>vesículas de secreción</strong> con proteínas modificadas listas para exocitosis.
          </p>
        </div>
      </div>

      <div class="two-col-layout">
        <div>
          <strong style="font-size:10px; color:#0369a1;">Funciones del Aparato de Golgi:</strong>
          <ul class="bullets-list" style="font-size:10px;">
            <li>Modificar proteínas y lípidos procedentes del retículo (glucosilación).</li>
            <li>Empaquetar y liberar sustancias en vesículas de secreción para exocitosis.</li>
            <li>Formar orgánulos celulares, especialmente los <strong>lisosomas</strong>.</li>
          </ul>
          <img src="{b_golgi_diag}" alt="Diagrama de Golgi" style="width:100%; border-radius:5px; border:1px solid #cbd5e1; margin-top:4px;">
        </div>
        <div class="micrograph-box">
          <img src="{b_golgi_micro}" alt="Micrografía de Golgi">
          <div class="micrograph-caption">Micrografía electrónica del aparato de Golgi</div>
        </div>
      </div>
    </div>

    <div class="page-footer">
      <span>Biología y Geología 4º ESO • Unidad 2: La Célula</span>
      <span>Página 15 (Traducción al Español)</span>
    </div>
  </div>


  <!-- ==================== PÁGINA 16 ==================== -->
  <div class="page" id="page-16">
    <div class="page-header">
      <span>1 CÉLULAS. REPRODUCCIÓN CELULAR</span>
      <span class="page-number">16</span>
    </div>

    <!-- 3. LISOSOMAS Y 4. VACUOLAS -->
    <div class="two-col-layout">
      <!-- LISOSOMAS -->
      <div class="organelle-card">
        <div class="organelle-title">
          <span>3. Lisosomas (Lysosomes)</span>
          <span class="organelle-pill">Membrana simple</span>
        </div>
        <p style="font-size:10.5px; line-height:1.35; color:#334155; margin-bottom:5px;">
          Vesículas de membrana simple formadas por el aparato de Golgi que contienen <strong>enzimas hidrolíticas</strong> (digestivas).
        </p>
        <p style="font-size:10.5px; line-height:1.35; color:#334155; margin-bottom:5px;">
          <strong>Función:</strong> Digerir sustancias procedentes del exterior celular (endocitosis) o materiales y orgánulos viejos del interior celular (autofagia).
        </p>
        <div class="micrograph-box">
          <img src="{b_lisosomas_micro}" alt="Micrografía de lisosomas">
          <div class="micrograph-caption">Micrografía electrónica de lisosomas (en azul) próximos al aparato de Golgi</div>
        </div>
        <div class="blanca-content" style="background:#fffbeb; padding:4px 6px; border-radius:4px; margin-top:4px; font-size:9.5px;">
          💡 <em>Apunte de Blanca:</em> "Personal de limpieza y defensa de la célula".
        </div>
      </div>

      <!-- VACUOLAS -->
      <div class="organelle-card">
        <div class="organelle-title">
          <span>4. Vacuolas (Vacuoles)</span>
          <span class="organelle-pill">Membrana simple</span>
        </div>
        <p style="font-size:10.5px; line-height:1.35; color:#334155; margin-bottom:5px;">
          Vesículas de membrana simple presentes en animales y plantas, aunque están <strong>especialmente desarrolladas en células vegetales</strong> (ocupan gran parte del volumen).
        </p>
        <strong style="font-size:10px; color:#0369a1;">Funciones principales:</strong>
        <ul class="bullets-list" style="font-size:10px; margin-bottom:6px;">
          <li>Almacenar agua, sustancias de reserva, productos de desecho, sustancias aromáticas y pigmentos.</li>
          <li>Mantener la <strong>turgencia celular</strong> (rigidez y elasticidad en vegetales).</li>
        </ul>
        <div style="background:#f1f5f9; border-left:3px solid #0284c7; padding:4px 6px; font-size:9.5px; color:#334155;">
          <strong>Nota comparativa:</strong> Los lisosomas en células animales y las vacuolas líticas en células vegetales desempeñan la misma función digestiva.
        </div>
      </div>
    </div>

    <!-- 5. MITOCONDRIAS -->
    <div class="organelle-card" style="margin-bottom:0;">
      <div class="organelle-title">
        <span>5. Mitocondrias (Mitochondria)</span>
        <span class="organelle-pill" style="background:#fef3c7; color:#b45309;">Doble membrana</span>
      </div>
      <p style="font-size:10.8px; line-height:1.35; color:#334155; margin-bottom:4px;">
        Orgánulos cilíndricos rodeados por una <strong>doble membrana</strong>. Son capaces de dividirse autónomamente por <strong>fisión binaria</strong>.
      </p>
      <p style="font-size:10.8px; line-height:1.35; color:#334155; margin-bottom:4px;">
        <strong>Función principal:</strong> Generar energía química (ATP) a partir de los nutrientes (glucosa) mediante la <strong>respiración celular</strong> aeróbica (requiere oxígeno):
      </p>

      <div class="chem-eq">
        Glucosa + 6 O₂ ➔ 6 CO₂ + 6 H₂O + Energía (ATP)
      </div>

      <div class="three-col-layout" style="margin-top:6px; margin-bottom:6px;">
        <div style="background:#fff; border:1px solid #cbd5e1; border-radius:5px; padding:5px;">
          <strong style="font-size:10px; color:#0284c7;">Doble membrana:</strong>
          <p style="font-size:9.5px; color:#475569;">Externa lisa e interna replegada en <strong>crestas mitocondriales</strong>.</p>
        </div>
        <div style="background:#fff; border:1px solid #cbd5e1; border-radius:5px; padding:5px;">
          <strong style="font-size:10px; color:#0284c7;">Espacio intermembrana:</strong>
          <p style="font-size:9.5px; color:#475569;">Pequeño espacio entre ambas membranas.</p>
        </div>
        <div style="background:#fff; border:1px solid #cbd5e1; border-radius:5px; padding:5px;">
          <strong style="font-size:10px; color:#0284c7;">Matriz mitocondrial:</strong>
          <p style="font-size:9.5px; color:#475569;">Interior acuoso con <strong>ADN circular propio</strong> y ribosomas tipo procariota.</p>
        </div>
      </div>

      <div class="two-col-layout">
        <img src="{b_mitoc_diag}" alt="Diagrama de mitocondria" style="width:100%; border-radius:5px; border:1px solid #cbd5e1;">
        <div class="micrograph-box">
          <img src="{b_mitoc_micro}" alt="Micrografía de mitocondria">
          <div class="micrograph-caption">Micrografía electrónica de una mitocondria con sus crestas</div>
        </div>
      </div>
    </div>

    <div class="page-footer">
      <span>Biología y Geología 4º ESO • Unidad 2: La Célula</span>
      <span>Página 16 (Traducción al Español)</span>
    </div>
  </div>


  <!-- ==================== PÁGINA 17 ==================== -->
  <div class="page" id="page-17">
    <div class="page-header">
      <span>1 CÉLULAS. REPRODUCCIÓN CELULAR</span>
      <span class="page-number">17</span>
    </div>

    <!-- 6. CLOROPLASTOS -->
    <div class="organelle-card">
      <div class="organelle-title">
        <span>6. Cloroplastos (Chloroplasts)</span>
        <span class="organelle-pill" style="background:#fef3c7; color:#b45309;">Doble membrana • Solo Vegetales</span>
      </div>
      <p style="font-size:10.8px; line-height:1.35; color:#334155; margin-bottom:4px;">
        Orgánulos rodeados por una <strong>doble membrana</strong>, exclusivos de las <strong>células vegetales</strong>. Al igual que las mitocondrias, se dividen por fisión binaria. Son responsables de realizar la <strong>fotosíntesis</strong> en dos fases:
      </p>

      <div class="two-col-layout" style="margin-bottom:4px;">
        <div style="background:#fff; border:1px solid #cbd5e1; border-radius:5px; padding:5px;">
          <strong style="font-size:10px; color:#059669;">1. Fase dependiente de la luz (luminosa):</strong>
          <p style="font-size:9.5px; color:#475569;">Ocurre en la membrana de los <strong>tilacoides</strong>. La energía solar se transforma en energía química.</p>
        </div>
        <div style="background:#fff; border:1px solid #cbd5e1; border-radius:5px; padding:5px;">
          <strong style="font-size:10px; color:#059669;">2. Fase independiente de la luz (oscura):</strong>
          <p style="font-size:9.5px; color:#475569;">Ocurre en el <strong>estroma</strong>. La energía química se emplea para transformar CO₂ en glucosa.</p>
        </div>
      </div>

      <div class="chem-eq">
        6 CO₂ + 6 H₂O + Energía solar ➔ Glucosa + 6 O₂
      </div>

      <div class="three-col-layout" style="margin-top:4px; margin-bottom:4px;">
        <div style="background:#fff; border:1px solid #cbd5e1; border-radius:5px; padding:4px;">
          <strong style="font-size:9.5px; color:#0284c7;">Doble membrana:</strong>
          <p style="font-size:9px; color:#475569;">Membrana externa e interna lisas con espacio intermembrana.</p>
        </div>
        <div style="background:#fff; border:1px solid #cbd5e1; border-radius:5px; padding:4px;">
          <strong style="font-size:9.5px; color:#0284c7;">Estroma:</strong>
          <p style="font-size:9px; color:#475569;">Fluido interior delimitado por membrana interna. Contiene <strong>ADN circular</strong> y ribosomas.</p>
        </div>
        <div style="background:#fff; border:1px solid #cbd5e1; border-radius:5px; padding:4px;">
          <strong style="font-size:9.5px; color:#0284c7;">Tilacoides y Grana:</strong>
          <p style="font-size:9px; color:#475569;">Sacos aplanados (tilacoides). Los apilamientos de tilacoides se llaman <strong>grana</strong>.</p>
        </div>
      </div>

      <div class="two-col-layout">
        <img src="{b_cloro_diag}" alt="Diagrama del cloroplasto" style="width:100%; border-radius:5px; border:1px solid #cbd5e1;">
        <div class="micrograph-box">
          <img src="{b_cloro_micro}" alt="Micrografía del cloroplasto">
          <div class="micrograph-caption">Micrografía electrónica de un cloroplasto con sus tilacoides y grana</div>
        </div>
      </div>
    </div>

    <!-- TEORÍA ENDOSIMBIÓTICA -->
    <div class="organelle-card" style="margin-bottom:0; background:#f0fdf4; border-color:#86efac;">
      <div class="organelle-title" style="color:#166534;">
        <span>El origen evolutivo de mitocondrias y cloroplastos (Teoría Endosimbiótica)</span>
      </div>
      <p style="font-size:10.5px; line-height:1.35; color:#14532d; margin-bottom:4px;">
        Propuesta y popularizada por la bióloga estadounidense <strong>Lynn Margulis</strong>. Establece que mitocondrias y cloroplastos se originaron a partir de células procariotas primitivas mediante dos procesos endosimbióticos consecutivos:
      </p>

      <div class="two-col-layout">
        <div>
          <ul class="bullets-list" style="font-size:10px; color:#14532d;">
            <li><strong>Endosimbiosis primaria:</strong> Una célula procariota anaerobia ancestral fagocitó <strong>bacterias aerobias</strong>. En lugar de ser digeridas, establecieron una simbiosis y evolucionaron hasta convertirse en <strong>mitocondrias</strong>. Da lugar a la <em>célula eucariota animal</em>.</li>
            <li><strong>Endosimbiosis secundaria:</strong> Posteriormente, la célula eucariota primitiva fagocitó <strong>bacterias fotosintéticas (cianobacterias)</strong>, que con el tiempo se convirtieron en <strong>cloroplastos</strong>. Da lugar a la <em>célula eucariota vegetal</em>.</li>
            <li><strong>Evidencias clave:</strong> Ambos orgánulos tienen doble membrana, su propio ADN circular, ribosomas propios y se dividen de forma autónoma por fisión binaria.</li>
          </ul>
        </div>
        <div>
          <img src="{b_endosimbiotica}" alt="Teoría endosimbiótica" style="width:100%; border-radius:5px; border:1px solid #86efac;">
        </div>
      </div>
    </div>

    <div class="page-footer">
      <span>Biología y Geología 4º ESO • Unidad 2: La Célula</span>
      <span>Página 17 (Traducción al Español)</span>
    </div>
  </div>


  <!-- ==================== PÁGINA 18 ==================== -->
  <div class="page" id="page-18">
    <div class="page-header">
      <span>1 CÉLULAS. REPRODUCCIÓN CELULAR</span>
      <span class="page-number">18</span>
    </div>

    <!-- 7. RIBOSOMAS -->
    <div class="organelle-card">
      <div class="organelle-title">
        <span>7. Ribosomas (Ribosomes)</span>
        <span class="organelle-pill" style="background:#e0e7ff; color:#3730a3;">Sin membrana • En todas las células</span>
      </div>
      <p style="font-size:10.8px; line-height:1.35; color:#334155; margin-bottom:4px;">
        Partículas compactas <strong>no rodeadas por membrana</strong>. Están formadas por <strong>ARN ribosómico (ARNr)</strong> y proteínas, organizadas en <strong>dos subunidades</strong> (subunidad mayor y subunidad menor).
      </p>

      <div class="two-col-layout">
        <div>
          <strong style="font-size:10px; color:#0369a1;">¿Dónde se encuentran?</strong>
          <ul class="bullets-list" style="font-size:10px; margin-bottom:4px;">
            <li>Dispersos en el citoplasma de células procariotas y eucariotas.</li>
            <li>En la matriz mitocondrial y en el estroma de cloroplastos.</li>
            <li>Adheridos a la cara citoplasmática del RER y en la cara externa de la membrana nuclear.</li>
          </ul>
          <p style="font-size:10.5px; color:#334155; line-height:1.3;">
            <strong>Función:</strong> Sintetizar proteínas a partir de la información genética contenida en los ácidos nucleicos (traducción).
          </p>
          <div class="blanca-content" style="background:#fffbeb; padding:3px 6px; border-radius:4px; margin-top:3px; font-size:9.5px;">
            💡 <em>Apunte de Blanca:</em> "Los obreros de la fábrica celular".
          </div>
        </div>

        <div style="display:flex; gap:6px;">
          <div style="flex:1; text-align:center;">
            <img src="{b_ribos_diag}" alt="Diagrama del ribosoma" style="width:100%; max-width:110px; display:block; margin:0 auto;">
            <span style="font-size:8.5px; color:#64748b;">Subunidad mayor y menor</span>
          </div>
          <div class="micrograph-box" style="flex:1.2;">
            <img src="{b_ribos_micro}" alt="Micrografía de ribosomas">
            <div class="micrograph-caption">Micrografía electrónica de ribosomas</div>
          </div>
        </div>
      </div>
    </div>

    <!-- 8. CENTROSOMA -->
    <div class="organelle-card" style="margin-bottom:0;">
      <div class="organelle-title">
        <span>8. Centrosoma (Centrosome)</span>
        <span class="organelle-pill" style="background:#e0e7ff; color:#3730a3;">Sin membrana • Solo Células Animales</span>
      </div>
      <p style="font-size:10.8px; line-height:1.35; color:#334155; margin-bottom:4px;">
        Orgánulo <strong>no rodeado por membrana</strong> presente exclusivamente en células animales, localizado cerca del núcleo. Formado por microtúbulos de la proteína tubulina:
      </p>

      <div class="three-col-layout" style="margin-bottom:5px;">
        <div style="background:#fff; border:1px solid #cbd5e1; border-radius:5px; padding:5px;">
          <strong style="font-size:10px; color:#0284c7;">Diplosoma:</strong>
          <p style="font-size:9.5px; color:#475569;">Dos cilindros perpendiculares llamados <strong>centriolos</strong>. Cada centriolo tiene <strong>9 tripletes de microtúbulos</strong> (9x3).</p>
        </div>
        <div style="background:#fff; border:1px solid #cbd5e1; border-radius:5px; padding:5px;">
          <strong style="font-size:10px; color:#0284c7;">Material pericentriolar:</strong>
          <p style="font-size:9.5px; color:#475569;">Región amorfa que envuelve al diplosoma.</p>
        </div>
        <div style="background:#fff; border:1px solid #cbd5e1; border-radius:5px; padding:5px;">
          <strong style="font-size:10px; color:#0284c7;">Fibras del áster:</strong>
          <p style="font-size:9.5px; color:#475569;">Microtúbulos radiales en forma de estrella que salen del material pericentriolar.</p>
        </div>
      </div>

      <div class="two-col-layout">
        <div>
          <strong style="font-size:10px; color:#0369a1;">Funciones del Centrosoma (Centro Organizador):</strong>
          <ul class="bullets-list" style="font-size:10px;">
            <li>Formar los microtúbulos del citoesqueleto.</li>
            <li>Formar el <strong>huso acromático / mitótico</strong> durante la división celular (mitosis y meiosis) para repartir los cromosomas.</li>
            <li>Formar los <strong>cilios y flagelos</strong> (estructuras de motilidad celular: los cilios son cortos y numerosos; los flagelos son largos y escasos).</li>
          </ul>
          <img src="{b_centro_diag}" alt="Diagrama del centrosoma" style="width:100%; border-radius:5px; border:1px solid #cbd5e1; margin-top:4px;">
        </div>

        <div class="micrograph-box">
          <img src="{b_centro_micro}" alt="Micrografía de par de centriolos">
          <div class="micrograph-caption">Micrografía electrónica de un par de centriolos perpendiculares</div>
        </div>
      </div>
    </div>

    <div class="page-footer">
      <span>Biología y Geología 4º ESO • Unidad 2: La Célula</span>
      <span>Página 18 (Traducción al Español)</span>
    </div>
  </div>

</body>
</html>
"""

with open("libro_completo_espanol.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("libro_completo_espanol.html generado con exito.")
