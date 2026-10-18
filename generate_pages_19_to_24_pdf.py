import os
import base64
import subprocess

def img_b64(path):
    if not os.path.exists(path):
        return ""
    with open(path, "rb") as f:
        ext = "png" if path.endswith(".png") else "jpeg"
        return f"data:image/{ext};base64," + base64.b64encode(f.read()).decode('utf-8')

# Assets for Pages 19 to 24
b_nucleo_diag = img_b64("fotos/nucleo_diagrama.png")
b_nucleo_micro = img_b64("fotos/nucleo_micrografia.png")
b_cromo_diag = img_b64("fotos/cromosoma_diagrama.png")
b_cromo_3d = img_b64("fotos/cromosoma_3d.png")
b_maria_blasco = img_b64("fotos/maria_blasco.png")
b_cromo_tipos = img_b64("fotos/cromosomas_tipos.png")
b_cariograma = img_b64("fotos/cariograma_esquema.png")
b_haplo_diag = img_b64("fotos/celula_haploide_diag.png")
b_diplo_diag = img_b64("fotos/celula_diploide_diag.png")
b_cariotipo_real = img_b64("fotos/cariotipo_humano_real.png")
b_cariotipo_montaje = img_b64("fotos/cariotipo_montaje.png")
b_fision_binaria = img_b64("fotos/fision_binaria.png")
b_mitosis_diag = img_b64("fotos/mitosis_esquema.png")
b_meiosis_diag = img_b64("fotos/meiosis_esquema.png")
b_ciclo_haplonte = img_b64("fotos/ciclo_haplonte.png")
b_ciclo_diplonte = img_b64("fotos/ciclo_diplonte.png")
b_ciclo_diplohaplo = img_b64("fotos/ciclo_diplohaplonte.png")

html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Tema 2: La Célula y Reproducción - Páginas 19 a 24 en Español</title>
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
    padding: 13mm 16mm 11mm 16mm;
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

  .page-header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 2px solid #e2e8f0;
    padding-bottom: 4px;
    margin-bottom: 8px;
    font-size: 10.5px;
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

  .section-banner {{
    display: inline-flex;
    align-items: center;
    background-color: #0284c7;
    color: #ffffff;
    padding: 4px 10px;
    font-family: 'Oswald', sans-serif;
    font-size: 14.5px;
    font-weight: 600;
    letter-spacing: 0.04em;
    text-transform: uppercase;
    margin-bottom: 8px;
    border-radius: 3px;
  }}

  .section-banner-dark {{
    background-color: #1e293b;
  }}

  .section-subbanner {{
    display: inline-block;
    background-color: #0284c7;
    color: #ffffff;
    padding: 2px 7px;
    font-family: 'Oswald', sans-serif;
    font-size: 12.5px;
    font-weight: 600;
    letter-spacing: 0.04em;
    text-transform: uppercase;
    margin-bottom: 6px;
    border-radius: 2px;
  }}

  p, li {{
    font-size: 10px;
    line-height: 1.4;
    color: #334155;
    text-align: justify;
  }}

  p {{
    margin-bottom: 6px;
  }}

  strong {{
    color: #0f172a;
    font-weight: 700;
  }}

  .card-box {{
    background: #f8fafc;
    border: 1px solid #cbd5e1;
    border-radius: 5px;
    padding: 7px 9px;
    margin-bottom: 6px;
  }}

  .card-title {{
    font-weight: 800;
    color: #0284c7;
    font-size: 10.5px;
    text-transform: uppercase;
    letter-spacing: 0.03em;
    margin-bottom: 3px;
    display: flex;
    align-items: center;
    gap: 5px;
  }}

  .speak-box {{
    background: #fffbeb;
    border: 1px solid #fef3c7;
    border-left: 3.5px solid #f59e0b;
    padding: 7px 9px;
    border-radius: 4px;
    margin-top: 6px;
  }}

  .speak-title {{
    font-family: 'Oswald', sans-serif;
    font-size: 12px;
    color: #b45309;
    font-weight: 700;
    letter-spacing: 0.06em;
    margin-bottom: 3px;
  }}

  .pencil-note {{
    font-family: 'Comic Sans MS', 'Caveat', cursive;
    color: #2563eb;
    font-size: 10px;
    background: rgba(219, 234, 254, 0.7);
    padding: 1px 6px;
    border-radius: 4px;
    display: inline-block;
    border: 1px dashed #3b82f6;
  }}

  .table-comp {{
    width: 100%;
    border-collapse: collapse;
    font-size: 9.5px;
    margin-top: 4px;
  }}

  .table-comp th {{
    background: #0284c7;
    color: #ffffff;
    font-weight: 700;
    padding: 5px 7px;
    text-align: left;
    border: 1px solid #0284c7;
  }}

  .table-comp td {{
    padding: 5px 7px;
    border: 1px solid #cbd5e1;
    vertical-align: top;
    line-height: 1.35;
  }}

  .table-comp tr:nth-child(even) {{
    background: #f8fafc;
  }}

  .img-frame {{
    border-radius: 4px;
    border: 1px solid #cbd5e1;
    overflow: hidden;
    background: #ffffff;
  }}

  .img-caption {{
    font-size: 8.5px;
    color: #64748b;
    padding: 2px 5px;
    background: #f8fafc;
    border-top: 1px solid #e2e8f0;
    text-align: center;
    font-style: italic;
  }}
</style>
</head>
<body>

  <!-- ==================== PÁGINA 19 ==================== -->
  <div class="page">
    <div class="page-header">
      <span>1 CÉLULAS. REPRODUCCIÓN CELULAR</span>
      <span class="page-number">19</span>
    </div>

    <div class="section-banner">3.4 EL NÚCLEO</div>

    <p style="margin-bottom: 8px;">
      El <strong>núcleo</strong> es una estructura característica y distintiva de las células eucariotas. Se observa claramente en el interior celular durante la <strong>interfase</strong>, es decir, cuando la célula no se está dividiendo. En las células animales, el núcleo suele ser esférico y situarse en posición central; en las células vegetales suele presentar una morfología circular-aplanada y aparece desplazado hacia un lateral debido al volumen ocupado por las grandes vacuolas.
    </p>

    <!-- Visual Row: Diagram + Micrograph -->
    <div style="display: grid; grid-template-columns: 1.45fr 1fr; gap: 9px; margin-bottom: 8px;">
      <div class="img-frame">
        <img src="{b_nucleo_diag}" style="width: 100%; height: 160px; object-fit: contain; display: block;">
        <div class="img-caption">Estructura del núcleo interfásico: envoltura, poros nucleares, nucleoplasma, nucleolo y continuidad con el RER.</div>
      </div>
      <div class="img-frame">
        <img src="{b_nucleo_micro}" style="width: 100%; height: 160px; object-fit: cover; display: block;">
        <div class="img-caption">Micrografía electrónica del núcleo celular coloreada artificialmente (nucleolo en azul).</div>
      </div>
    </div>

    <div style="font-size: 10px; font-weight: 700; color: #0284c7; margin-bottom: 5px;">
      COMPONENTES DEL NÚCLEO EN INTERFASE:
    </div>

    <!-- 4 Components Grid -->
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 7px; margin-bottom: 8px;">
      
      <!-- Component 1: Membrana -->
      <div class="card-box">
        <div class="card-title">1. Membrana o Envoltura Nuclear</div>
        <p style="font-size: 9.2px; line-height: 1.35; margin: 0;">
          Rodea el contenido nuclear. Formada por una <strong>doble membrana</strong> (interna y externa) separadas por el <em>espacio perinuclear</em>. La membrana externa es una prolongación directa del retículo endoplasmático rugoso (RER) y posee ribosomas asociados. Ambas membranas se fusionan en los <strong>poros nucleares</strong>: canales dinámicos y regulables que controlan el transporte de macromoléculas (ARN, proteínas) entre el núcleo y el citosol.
        </p>
      </div>

      <!-- Component 2: Nucleoplasma -->
      <div class="card-box">
        <div class="card-title">2. Nucleoplasma</div>
        <p style="font-size: 9.2px; line-height: 1.35; margin: 0;">
          Es el medio interno acuoso del núcleo (matriz nuclear). Está constituido por agua, iones disueltos, nucleótidos libres (para la síntesis de ARN y ADN) y numerosas proteínas y enzimas (como polimerasas) que intervienen en la replicación y transcripción.
        </p>
      </div>

      <!-- Component 3: Nucleolo -->
      <div class="card-box">
        <div class="card-title">3. Nucleolo</div>
        <p style="font-size: 9.2px; line-height: 1.35; margin: 0;">
          Región esférica densa, no delimitada por membrana, formada por secuencias organizadoras nucleolares de ADN y acúmulos de ARN ribosómico (ARNr) y proteínas. Su función primordial es la <strong>síntesis de subunidades ribosómicas</strong>. Puede haber uno o más nucleolos en cada núcleo.
        </p>
      </div>

      <!-- Component 4: Cromatina -->
      <div class="card-box">
        <div class="card-title">
          4. Cromatina <span class="pencil-note">Nota de Blanca: maraña</span>
        </div>
        <p style="font-size: 9.2px; line-height: 1.35; margin: 0;">
          Malla o <em>maraña</em> difusa de filamentos que se extiende por todo el nucleoplasma. Está constituida por moléculas lineales de <strong>ADN bicatenario asociadas a proteínas básicas llamadas histonas</strong>. Las histonas permiten empaquetar y compactar el ADN en nucleosomas durante la interfase.
        </p>
      </div>

    </div>

    <!-- Functions Box -->
    <div style="background: #e0f2fe; border: 1.5px solid #38bdf8; border-radius: 5px; padding: 7px 10px; margin-bottom: 7px;">
      <div style="font-weight: 800; color: #0369a1; font-size: 10px; margin-bottom: 3px; text-transform: uppercase;">
        Funciones Primordiales del Núcleo Celular:
      </div>
      <ul style="padding-left: 14px; font-size: 9.5px; color: #0c4a6e;">
        <li><strong>Controlar la actividad metabólica y celular:</strong> Coordina la expresión génica traduciendo la información genética del ADN en ARN mensajero.</li>
        <li><strong>Garantizar la transmisión hereditaria:</strong> Conserva íntegra la información genética y la replica antes de la división celular para repartirla a las células descendientes.</li>
      </ul>
    </div>

    <!-- Speak Box -->
    <div class="speak-box">
      <div class="speak-title">//// SPEAK & PRACTICE &lt;&lt;&lt;&lt;</div>
      <p style="font-size: 9px; line-height: 1.3; margin: 0;">
        <strong>Actividad comunicativa:</strong> Trabajad por parejas o en pequeños grupos y redactad 3 frases verdaderas y 3 falsas acerca de las semejanzas y diferencias entre el núcleo de la célula animal y vegetal. Luego intercambiad vuestras preguntas con el grupo compañero para comprobar vuestros conocimientos.
      </p>
    </div>

  </div>


  <!-- ==================== PÁGINA 20 ==================== -->
  <div class="page">
    <div class="page-header">
      <span>1 CÉLULAS. REPRODUCCIÓN CELULAR</span>
      <span class="page-number">20</span>
    </div>

    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
      <div class="section-banner section-banner-dark">4 /// LOS CROMOSOMAS</div>
      <span style="font-size: 10px; font-weight: 700; color: #64748b;">Actividades 12–15</span>
    </div>

    <div style="display: grid; grid-template-columns: 1.8fr 1fr; gap: 11px;">
      
      <!-- Left Column: Concepts & Structure -->
      <div>
        <p>
          Un <strong>cromosoma</strong> es una macromolécula formada por una molécula de ADN bicatenario lineal condensada a su máximo nivel de empaquetamiento junto a histonas. Es una estructura <strong>extraordinariamente compacta</strong> que se hace visible al microscopio óptico durante los procesos de división celular (mitosis y meiosis).
        </p>
        <p>
          La función esencial de los cromosomas es asegurar que la información hereditaria se distribuya de forma equitativa y sin pérdidas desde la célula progenitora a las células hijas. Antes de la división, cada molécula de ADN se <strong>replica</strong> formando dos copias idénticas.
        </p>

        <div class="section-subbanner">4.1 ESTRUCTURA DE UN CROMOSOMA</div>

        <p style="margin-bottom: 6px;">
          En un cromosoma metafásico típico se distinguen con claridad tres regiones anatómicas:
        </p>

        <!-- Diagram Replication -->
        <div class="img-frame" style="margin-bottom: 8px; padding: 4px;">
          <img src="{b_cromo_diag}" style="width: 100%; height: 115px; object-fit: contain; display: block;">
          <div class="img-caption">Proceso de replicación del ADN: de un cromosoma no duplicado (1 cromátida) a un cromosoma duplicado (2 cromátidas hermanas).</div>
        </div>

        <div class="card-box">
          <div class="card-title">1. Cromátidas</div>
          <p style="font-size: 9.3px; margin: 0; line-height: 1.35;">
            Brazos filamentosos formados por la fibra de cromatina densamente enrollada. Antes de la replicación del ADN el cromosoma tiene una sola cromátida; tras la fase S de síntesis presenta <strong>dos cromátidas hermanas idénticas</strong> unidas por el centrómero. Los extremos redondeados se denominan <strong>telómeros</strong> y protegen al cromosoma de la degradación.
          </p>
        </div>

        <div class="card-box">
          <div class="card-title">2. Centrómero (Constricción primaria)</div>
          <p style="font-size: 9.3px; margin: 0; line-height: 1.35;">
            Región estrecha y estrangulada del cromosoma que une a las dos cromátidas hermanas. En él se asocian complejos proteicos (cinetocoros) donde se anclan los microtúbulos del huso acromático para arrastrar las cromátidas.
          </p>
        </div>

        <div class="card-box">
          <div class="card-title">3. Brazos</div>
          <p style="font-size: 9.3px; margin: 0; line-height: 1.35;">
            Son las porciones de cromátida que se extienden a cada lado del centrómero. Generalmente se diferencian en brazo corto (denominado <em>p</em>, del francés <em>petit</em>) y brazo largo (denominado <em>q</em>).
          </p>
        </div>

      </div>

      <!-- Right Column: 3D render, Maria Blasco & Speak -->
      <div>
        <div class="img-frame" style="margin-bottom: 8px;">
          <img src="{b_cromo_3d}" style="width: 100%; height: 130px; object-fit: contain; display: block;">
          <div class="img-caption">Reconstrucción 3D de un cromosoma metafásico condensado.</div>
        </div>

        <!-- Maria Blasco Feature -->
        <div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 5px; padding: 7px; margin-bottom: 7px;">
          <div class="img-frame" style="margin-bottom: 5px;">
            <img src="{b_maria_blasco}" style="width: 100%; height: 100px; object-fit: cover; display: block;">
          </div>
          <div style="font-weight: 800; font-size: 9.5px; color: #0f172a; margin-bottom: 2px;">
            CIENCIA ESPAÑOLA: MARÍA A. BLASCO
          </div>
          <p style="font-size: 8.8px; line-height: 1.3; color: #334155; margin: 0;">
            La bióloga molecular alicantina <strong>María Antonia Blasco</strong> es una referencia mundial en el estudio del envejecimiento celular, el cáncer y el papel protector de los <strong>telómeros</strong>. Es Directora del Centro Nacional de Investigaciones Oncológicas (CNIO) desde 2011.
          </p>
        </div>

        <!-- Speak Box -->
        <div class="speak-box" style="margin-top: 0;">
          <div class="speak-title">//// VOCABULARIO CLAVE</div>
          <p style="font-size: 8.8px; line-height: 1.3; margin: 0;">
            <em>Accuracy</em> (precisión), <em>swab</em> (hisopo de muestra), <em>fragmented</em> (fragmentado), <em>contamination</em> (contaminación), <em>paternity test</em> (prueba de paternidad).
          </p>
        </div>
      </div>

    </div>

  </div>


  <!-- ==================== PÁGINA 21 ==================== -->
  <div class="page">
    <div class="page-header">
      <span>1 CÉLULAS. REPRODUCCIÓN CELULAR</span>
      <span class="page-number">21</span>
    </div>

    <div class="section-banner">4.2 TIPOS DE CROMOSOMAS</div>

    <p style="margin-bottom: 6px;">
      Los cromosomas se clasifican en <strong>cuatro morfologías</strong> según la posición exacta que ocupa el centrómero a lo largo del cromosoma:
    </p>

    <!-- Chromosome Types Diagram -->
    <div class="img-frame" style="margin-bottom: 9px; padding: 4px;">
      <img src="{b_cromo_tipos}" style="width: 100%; height: 85px; object-fit: contain; display: block;">
      <div class="img-caption">Morfologías cromosómicas: Metacéntrico (brazos iguales), Submetacéntrico (desiguales), Acrocéntrico (muy desiguales) y Telocéntrico (centrómero terminal).</div>
    </div>

    <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 6px; margin-bottom: 10px;">
      <div class="card-box" style="padding: 5px;">
        <div style="font-weight: 800; font-size: 9.5px; color: #0284c7; text-align: center;">METACÉNTRICO</div>
        <p style="font-size: 8.8px; line-height: 1.3; margin: 0; text-align: center;">Centrómero en posición central exacta. Los dos brazos tienen la misma longitud.</p>
      </div>
      <div class="card-box" style="padding: 5px;">
        <div style="font-weight: 800; font-size: 9.5px; color: #0284c7; text-align: center;">SUBMETACÉNTRICO</div>
        <p style="font-size: 8.8px; line-height: 1.3; margin: 0; text-align: center;">Centrómero ligeramente desplazado. Los brazos presentan longitudes desiguales (p y q).</p>
      </div>
      <div class="card-box" style="padding: 5px;">
        <div style="font-weight: 800; font-size: 9.5px; color: #0284c7; text-align: center;">ACROCÉNTRICO</div>
        <p style="font-size: 8.8px; line-height: 1.3; margin: 0; text-align: center;">Centrómero muy próximo a un extremo. Brazos muy desiguales (brazo p diminuto).</p>
      </div>
      <div class="card-box" style="padding: 5px;">
        <div style="font-weight: 800; font-size: 9.5px; color: #0284c7; text-align: center;">TELOCÉNTRICO</div>
        <p style="font-size: 8.8px; line-height: 1.3; margin: 0; text-align: center;">Centrómero en el extremo terminal absoluto. Solo es visible un juego de brazos (no existen en humanos).</p>
      </div>
    </div>

    <div class="section-banner section-banner-dark">4.3 CARIOTIPO Y NÚMERO CROMOSÓMICO</div>

    <div style="display: grid; grid-template-columns: 1.8fr 1fr; gap: 10px;">
      <div>
        <p>
          Un <strong>cariotipo</strong> es el conjunto ordenado y sistematizado de todos los cromosomas de una célula, clasificados por parejas de homólogos atendiendo a su longitud relativa, la posición del centrómero y el patrón de bandas revelado mediante tinciones químicas específicas.
        </p>

        <ul style="padding-left: 14px; font-size: 9.3px; line-height: 1.38; margin-bottom: 6px;">
          <li><strong>Constancia cromosómica:</strong> El número de cromosomas es constante e invariable para cada especie biológica, salvo la aparición de mutaciones o anomalías genómicas.</li>
          <li><strong>Ploidía celular:</strong> Hace referencia al número de juegos completos de cromosomas:
            <ul style="padding-left: 14px; margin-top: 2px;">
              <li><strong>Haploide (n):</strong> Posee un único juego de cromosomas (sin parejas). Es propio de los <strong>gametos</strong> (óvulos y espermatozoides).</li>
              <li><strong>Diploide (2n):</strong> Posee dos juegos completos de cromosomas (parejas). Es propio de las <strong>células somáticas</strong> y del cigoto formado por fecundación.</li>
            </ul>
          </li>
          <li><strong>Cromosomas homólogos:</strong> Parejas de cromosomas de igual forma, tamaño y posición del centrómero que contienen información para los mismos caracteres (uno materno y otro paterno).</li>
          <li><strong>Autosomas y Heterocromosomas:</strong> Los autosomas no determinan el sexo del individuo. Los heterocromosomas (cromosomas sexuales) determinan el sexo: en mamíferos son <strong>XX (hembra)</strong> y <strong>XY (macho)</strong>.</li>
        </ul>

        <!-- Haploid vs Diploid mini-diagrams -->
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 7px;">
          <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 4px; padding: 4px; display: flex; align-items: center; gap: 6px;">
            <img src="{b_haplo_diag}" style="width: 48px; height: 48px; object-fit: contain;">
            <div style="font-size: 8.8px; line-height: 1.25;">
              <strong>Célula haploide (n = 3)</strong><br>
              Tres cromosomas distintos, sin parejas de homólogos.
            </div>
          </div>
          <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 4px; padding: 4px; display: flex; align-items: center; gap: 6px;">
            <img src="{b_diplo_diag}" style="width: 48px; height: 48px; object-fit: contain;">
            <div style="font-size: 8.8px; line-height: 1.25;">
              <strong>Célula diploide (2n = 6)</strong><br>
              Tres parejas de cromosomas homólogos (2 juegos).
            </div>
          </div>
        </div>

      </div>

      <!-- Right Column: Karyogram Box -->
      <div>
        <div class="card-box" style="margin-bottom: 0;">
          <div class="card-title">Cariograma</div>
          <p style="font-size: 8.8px; line-height: 1.3; margin-bottom: 6px;">
            Un cariograma es la representación gráfica y esquemática a escala del tamaño, forma y bandeado de todos los cromosomas de una especie.
          </p>
          <div class="img-frame">
            <img src="{b_cariograma}" style="width: 100%; height: 165px; object-fit: contain; display: block;">
            <div class="img-caption">Cariograma humano esquemático: 22 pares de autosomas + par sexual (XY).</div>
          </div>
        </div>
      </div>
    </div>

  </div>


  <!-- ==================== PÁGINA 22 ==================== -->
  <div class="page">
    <div class="page-header">
      <span>CARIOTIPOS HUMANOS</span>
      <span class="page-number">22</span>
    </div>

    <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
      <div class="section-banner">ORGANIZACIÓN DEL CARIOTIPO HUMANO</div>
      <span style="font-weight: 800; color: #0284c7; font-size: 13px;">2n = 46 cromosomas</span>
    </div>

    <div style="display: grid; grid-template-columns: 1.4fr 1fr; gap: 9px; margin-bottom: 8px;">
      
      <!-- Text Groups A to G -->
      <div>
        <p style="font-size: 9.3px; margin-bottom: 5px;">
          En la especie humana el cariotipo está constituido por 46 cromosomas (23 pares: 22 pares de autosomas y 1 par de heterocromosomas). Se clasifican en <strong>siete grupos (del A al G)</strong>. Los seres humanos <strong>no poseemos ningún cromosoma telocéntrico</strong>:
        </p>

        <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 4px; padding: 6px; font-size: 8.8px; line-height: 1.35;">
          <strong>CROMOSOMAS GRANDES:</strong><br>
          • <strong>Grupo A:</strong> Pares 1 (metacéntrico), 2 (submetacéntrico) y 3 (metacéntrico).<br>
          • <strong>Grupo B:</strong> Pares 4 y 5 (submetacéntricos).<br>
          <strong style="display: block; margin-top: 3px;">CROMOSOMAS MEDIANOS:</strong>
          • <strong>Grupo C:</strong> Pares 6 al 12 y cromosoma X (todos submetacéntricos).<br>
          • <strong>Grupo D:</strong> Pares 13, 14 y 15 (acrocéntricos con satélites).<br>
          <strong style="display: block; margin-top: 3px;">CROMOSOMAS PEQUEÑOS:</strong>
          • <strong>Grupo E:</strong> Pares 16 (metacéntrico), 17 y 18 (submetacéntricos).<br>
          • <strong>Grupo F:</strong> Pares 19 y 20 (metacéntricos pequeños).<br>
          • <strong>Grupo G:</strong> Pares 21, 22 y cromosoma Y (acrocéntricos).
        </div>
      </div>

      <!-- Real Karyotype Photo -->
      <div class="img-frame">
        <img src="{b_cariotipo_real}" style="width: 100%; height: 185px; object-fit: contain; display: block;">
        <div class="img-caption">Microfotografía de cariotipo humano masculino 46, XY agrupado de A a G.</div>
      </div>

    </div>

    <!-- Practical Lab Section -->
    <div style="background: #f0fdf4; border: 1.5px solid #86efac; border-radius: 5px; padding: 7px 10px;">
      <div style="font-family: 'Oswald', sans-serif; font-size: 12px; color: #166534; font-weight: 700; margin-bottom: 4px; text-transform: uppercase;">
        🔬 PRÁCTICA: ELABORACIÓN DE UN CARIOTIPO HUMANO
      </div>

      <div style="display: grid; grid-template-columns: 1.6fr 1fr; gap: 9px;">
        <div style="font-size: 8.8px; line-height: 1.32; color: #14532d;">
          <p style="margin-bottom: 3px;"><strong>Materiales:</strong> Fotografía de metafase al microscopio óptico teñida con Giemsa, tijeras, cartulina milimetrada y pegamento.</p>
          <strong>Procedimiento (Paso a paso):</strong>
          <ol style="padding-left: 14px; margin-top: 2px;">
            <li><strong>Recuento preliminar:</strong> Contar todos los cromosomas dispersos en la metafase para comprobar el número diploide (46) y detectar aneuploidías (como trisomías).</li>
            <li><strong>Recorte y emparejamiento:</strong> Recortar individualmente cada cromosoma y agruparlos por parejas de homólogos comparando tamaño y bandeo.</li>
            <li><strong>Alineación horizontal:</strong> Pegar los pares homólogos en orden decreciente de longitud, manteniendo los centrómeros sobre la misma línea guía.</li>
            <li><strong>Numeración:</strong> Asignar a cada pareja de autosomas su número del 1 al 22.</li>
            <li><strong>Clasificación por grupos:</strong> Delimitar los 7 grupos morfológicos (A a G).</li>
            <li><strong>Pares sexuales:</strong> Situar la pareja sexual (XX en mujeres, XY en varones) al final del cariotipo para determinar el sexo genético.</li>
          </ol>
        </div>

        <div class="img-frame">
          <img src="{b_cariotipo_montaje}" style="width: 100%; height: 175px; object-fit: contain; display: block;">
          <div class="img-caption">De la metafase desordenada al cariotipo femenino 46, XX ordenado.</div>
        </div>
      </div>

    </div>

  </div>


  <!-- ==================== PÁGINA 23 ==================== -->
  <div class="page">
    <div class="page-header">
      <span>1 CÉLULAS. REPRODUCCIÓN CELULAR</span>
      <span class="page-number">23</span>
    </div>

    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 7px;">
      <div class="section-banner section-banner-dark">5 /// LA DIVISIÓN CELULAR</div>
      <span style="font-size: 10px; font-weight: 700; color: #64748b;">Actividades 16–17</span>
    </div>

    <p style="margin-bottom: 7px;">
      La <strong>división celular</strong> es el proceso biológico fundamental mediante el cual una célula madre genera nuevas células. Garantiza la perpetuación de la vida, el crecimiento de los organismos y la sustitución de células envejecidas o dañadas. Los mecanismos difieren radicalmente entre procariotas y eucariotas.
    </p>

    <!-- 5.1 Procaryotes -->
    <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 5px; padding: 7px; margin-bottom: 9px;">
      <div class="section-subbanner" style="background: #475569; margin-bottom: 4px;">5.1 DIVISIÓN EN CÉLULAS PROCARIOTAS (BACTERIAS)</div>
      <div style="display: grid; grid-template-columns: 2fr 1fr; gap: 9px; align-items: center;">
        <p style="font-size: 9.2px; line-height: 1.35; margin: 0;">
          Las bacterias se dividen mediante <strong>fisión binaria o bipartición (amitosis)</strong>. Primero replican su cromosoma circular de ADN unido a la membrana plasmática. A continuación, la pared celular y la membrana crecen hacia el interior formando un septo de estrangulación (citocinesis) que separa la célula en <strong>dos células hijas clónicas</strong> e idénticas a la progenitora. Es un mecanismo de <strong>reproducción asexual</strong> altamente eficiente.
        </p>
        <div class="img-frame">
          <img src="{b_fision_binaria}" style="width: 100%; height: 75px; object-fit: contain; display: block;">
          <div class="img-caption">Fisión binaria bacteriana.</div>
        </div>
      </div>
    </div>

    <!-- 5.2 Eucaryotes: Mitosis vs Meiosis -->
    <div class="section-banner">5.2 DIVISIÓN EN CÉLULAS EUCARIOTAS</div>

    <p style="font-size: 9.3px; margin-bottom: 6px;">
      En las células eucariotas el material genético está fragmentado en múltiples cromosomas dentro de un núcleo. La segregación cromosómica puede ocurrir mediante dos procesos fundamentales:
    </p>

    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
      
      <!-- MITOSIS CARD -->
      <div style="background: #eff6ff; border: 1.5px solid #60a5fa; border-radius: 5px; padding: 8px;">
        <div style="font-family: 'Oswald', sans-serif; font-size: 13px; color: #1d4ed8; font-weight: 700; margin-bottom: 4px;">
          MITOSIS (División Ecuacional)
        </div>
        <p style="font-size: 9px; line-height: 1.35; margin-bottom: 5px;">
          Proceso de división del núcleo que reparte los cromosomas de forma idéntica en <strong>dos células hijas con la misma dotación cromosómica (2n &rarr; 2n)</strong> e idéntica información que la célula madre.
        </p>
        <div class="img-frame" style="margin-bottom: 5px;">
          <img src="{b_mitosis_diag}" style="width: 100%; height: 115px; object-fit: contain; display: block;">
          <div class="img-caption">Mitosis: de una célula 2n=4 a dos células hijas idénticas 2n=4.</div>
        </div>
        <div style="font-size: 8.8px; line-height: 1.3; color: #1e3a8a;">
          <strong>Funciones biológicas:</strong><br>
          • Reproducción asexual en organismos unicelulares eucariotas.<br>
          • Crecimiento del individuo durante el desarrollo embrionario.<br>
          • Renovación celular y reparación de tejidos en pluricelulares.
        </div>
      </div>

      <!-- MEIOSIS CARD -->
      <div style="background: #fdf2f8; border: 1.5px solid #f472b6; border-radius: 5px; padding: 8px;">
        <div style="font-family: 'Oswald', sans-serif; font-size: 13px; color: #be185d; font-weight: 700; margin-bottom: 4px;">
          MEIOSIS (División Reduccional)
        </div>
        <p style="font-size: 9px; line-height: 1.35; margin-bottom: 5px;">
          Consta de <strong>dos divisiones sucesivas</strong> precedidas de una sola duplicación de ADN. Genera <strong>cuatro células hijas haploides (n)</strong> con la mitad de cromosomas y recombinación genética.
        </p>
        <div class="img-frame" style="margin-bottom: 5px;">
          <img src="{b_meiosis_diag}" style="width: 100%; height: 115px; object-fit: contain; display: block;">
          <div class="img-caption">Ciclo meiótico y fecundación reconstituyendo la dotación 2n.</div>
        </div>
        <div style="font-size: 8.8px; line-height: 1.3; color: #831843;">
          <strong>Funciones biológicas:</strong><br>
          • Formación de gametos haploides en la <strong>reproducción sexual</strong>.<br>
          • Evita que se duplique el número de cromosomas en la fecundación.<br>
          • Aporta <strong>variabilidad genética</strong> mediante el sobrecruzamiento.
        </div>
      </div>

    </div>

  </div>


  <!-- ==================== PÁGINA 24 ==================== -->
  <div class="page">
    <div class="page-header">
      <span>1 CÉLULAS. REPRODUCCIÓN CELULAR</span>
      <span class="page-number">24</span>
    </div>

    <div class="section-banner">5.3 CICLOS BIOLÓGICOS</div>

    <p style="margin-bottom: 6px;">
      Un <strong>ciclo biológico (o ciclo de vida)</strong> es la secuencia ordenada de fases y transformaciones que experimenta un organismo con reproducción sexual a lo largo de su existencia, desde la fecundación del cigoto hasta que alcanza la madurez y produce sus propios gametos. Implica la alternancia obligada de una fase haploide (n) y una fase diploide (2n).
    </p>

    <!-- 3 Cycles Grid -->
    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 7px; margin-bottom: 9px;">
      
      <!-- Cycle 1: Haplonte -->
      <div class="card-box" style="padding: 6px;">
        <div style="font-weight: 800; font-size: 9.5px; color: #b45309; text-align: center;">CICLO HAPLONTE</div>
        <p style="font-size: 8.5px; line-height: 1.25; margin-bottom: 4px; text-align: justify;">
          El adulto es <strong>haploide (n)</strong>. Tras la fecundación, la meiosis ocurre en el propio cigoto, dando esporas meióticas que por mitosis originan adultos haploides. Típico de <strong>algas y hongos</strong>.
        </p>
        <div class="img-frame">
          <img src="{b_ciclo_haplonte}" style="width: 100%; height: 100px; object-fit: contain; display: block;">
          <div class="img-caption">Ciclo haplonte.</div>
        </div>
      </div>

      <!-- Cycle 2: Diplonte -->
      <div class="card-box" style="padding: 6px;">
        <div style="font-weight: 800; font-size: 9.5px; color: #0284c7; text-align: center;">CICLO DIPLONTE</div>
        <p style="font-size: 8.5px; line-height: 1.25; margin-bottom: 4px; text-align: justify;">
          El individuo adulto es <strong>diploide (2n)</strong>. La meiosis ocurre únicamente en los órganos reproductores para fabricar gametos (n). La fecundación genera el cigoto 2n. Típico de <strong>animales</strong>.
        </p>
        <div class="img-frame">
          <img src="{b_ciclo_diplonte}" style="width: 100%; height: 100px; object-fit: contain; display: block;">
          <div class="img-caption">Ciclo diplonte.</div>
        </div>
      </div>

      <!-- Cycle 3: Diplohaplonte -->
      <div class="card-box" style="padding: 6px;">
        <div style="font-weight: 800; font-size: 9.5px; color: #059669; text-align: center;">CICLO HAPLODIPLONTE</div>
        <p style="font-size: 8.5px; line-height: 1.25; margin-bottom: 4px; text-align: justify;">
          Alternancia de dos generaciones adultas: el <strong>esporofito (2n)</strong> produce esporas por meiosis, que germinan en el <strong>gametofito (n)</strong>, formador de gametos. Típico de <strong>plantas</strong>.
        </p>
        <div class="img-frame">
          <img src="{b_ciclo_diplohaplo}" style="width: 100%; height: 100px; object-fit: contain; display: block;">
          <div class="img-caption">Ciclo haplodiplonte.</div>
        </div>
      </div>

    </div>

    <!-- Comparative Table -->
    <div style="font-family: 'Oswald', sans-serif; font-size: 11.5px; color: #0f172a; font-weight: 700; margin-bottom: 3px;">
      COMPARATIVA CRÍTICA: REPRODUCCIÓN ASEXUAL VS REPRODUCCIÓN SEXUAL
    </div>

    <table class="table-comp">
      <thead>
        <tr>
          <th style="width: 22%;">Tipo de Reproducción</th>
          <th style="width: 39%;">Ventajas Evolutivas</th>
          <th style="width: 39%;">Desventajas y Limitaciones</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Reproducción Asexual</strong><br><span style="color:#64748b; font-size:8.5px;">(Mitosis / Bipartición)</span></td>
          <td>
            • Requiere <strong>un solo progenitor</strong>; no hay gasto de tiempo ni recursos buscando pareja.<br>
            • No requiere células especializadas (ahorro energético considerable).<br>
            • Rápida propagación y descendencia adaptada a hábitats estables.
          </td>
          <td>
            • <strong>No genera variabilidad genética</strong>: todos los clones son idénticos al progenitor.<br>
            • La única fuente de novedad son mutaciones espontáneas.<br>
            • Poblaciones muy vulnerables ante cambios ambientales imprevistos.
          </td>
        </tr>
        <tr>
          <td><strong>Reproducción Sexual</strong><br><span style="color:#64748b; font-size:8.5px;">(Meiosis + Fecundación)</span></td>
          <td>
            • Aporta <strong>alta variabilidad genética</strong> por recombinación meiótica y combinación biparental.<br>
            • Incrementa la probabilidad de que existan individuos mejor adaptados ante fluctuaciones del medio.<br>
            • <strong>Motor primordial de la evolución biológica</strong>.
          </td>
          <td>
            • Requiere dos progenitores compatibles (alto coste en búsqueda y cortejo).<br>
            • Fabricar gametos y estructuras reproductivas consume gran cantidad de energía metabólica.<br>
            • Ritmo de multiplicación más lento.
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</body>
</html>
"""

# Write HTML file
with open("libro_paginas_19_a_24.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("libro_paginas_19_a_24.html generado.")

# Render to PDF using Chrome Headless
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
out_pdf = os.path.abspath("Tema_2_La_Celula_Paginas_19_a_24_Espanol.pdf")
in_html = "file:///" + os.path.abspath("libro_paginas_19_a_24.html").replace("\\", "/")

cmd = [
    chrome_path,
    "--headless=new",
    "--disable-gpu",
    "--run-all-compositor-stages-before-draw",
    "--no-pdf-header-footer",
    f"--print-to-pdf={out_pdf}",
    in_html
]

print("Renderizando PDF de páginas 19 a 24 con Chrome...")
subprocess.run(cmd, check=True)
print(f"PDF generado exitosamente: {out_pdf}")
