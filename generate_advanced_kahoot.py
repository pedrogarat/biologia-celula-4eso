import os
import base64
import json

def img_b64(path):
    if not os.path.exists(path):
        return ""
    with open(path, "rb") as f:
        ext = "png" if path.endswith(".png") else "jpeg"
        return f"data:image/{ext};base64," + base64.b64encode(f.read()).decode('utf-8')

# Dictionary of base64 images
images = {
    "celula_basica": img_b64("fotos/celula_basica.png"),
    "bacteria": img_b64("fotos/bacteria_procariota.png"),
    "muscular": img_b64("fotos/celula_muscular_A.png"),
    "nerviosa": img_b64("fotos/celula_nerviosa_B.png"),
    "vegetal": img_b64("fotos/celula_vegetal_C.png"),
    "membrana": img_b64("fotos/membrana_mosaico_fluido.png"),
    "transporte": img_b64("fotos/transporte_membrana.png"),
    "endocitosis": img_b64("fotos/endocitosis_exocitosis.png"),
    "pared": img_b64("fotos/pared_celular_microscopio.png"),
    "citoesq_diag": img_b64("fotos/citoesqueleto_diagrama.png"),
    "citoesq_micro": img_b64("fotos/citoesqueleto_micrografia.png"),
    "reticulo_diag": img_b64("fotos/reticulo_endoplasmatico.png"),
    "reticulo_micro": img_b64("fotos/reticulo_micrografia.png"),
    "golgi_diag": img_b64("fotos/golgi_diagrama.png"),
    "golgi_micro": img_b64("fotos/golgi_micrografia.png"),
    "lisosomas_micro": img_b64("fotos/lisosomas_micrografia.png"),
    "mitoc_diag": img_b64("fotos/mitocondria_diagrama.png"),
    "mitoc_micro": img_b64("fotos/mitocondria_micrografia.png"),
    "cloro_diag": img_b64("fotos/cloroplasto_diagrama.png"),
    "cloro_micro": img_b64("fotos/cloroplasto_micrografia.png"),
    "endosimbiotica": img_b64("fotos/teoria_endosimbiotica.png"),
    "ribos_diag": img_b64("fotos/ribosoma_diagrama.png"),
    "ribos_micro": img_b64("fotos/ribosomas_micrografia.png"),
    "centro_diag": img_b64("fotos/centrosoma_diagrama.png"),
    "centro_micro": img_b64("fotos/centriolos_micrografia.png"),
    "nucleo_diag": img_b64("fotos/nucleo_diagrama.png"),
    "nucleo_micro": img_b64("fotos/nucleo_micrografia.png"),
    "cromo_diag": img_b64("fotos/cromosoma_diagrama.png"),
    "cromo_3d": img_b64("fotos/cromosoma_3d.png"),
    "cromo_tipos": img_b64("fotos/cromosomas_tipos.png"),
    "cariotipo_real": img_b64("fotos/cariotipo_humano_real.png"),
    "fision_binaria": img_b64("fotos/fision_binaria.png"),
    "mitosis_diag": img_b64("fotos/mitosis_esquema.png"),
    "meiosis_diag": img_b64("fotos/meiosis_esquema.png"),
    "ciclo_haplonte": img_b64("fotos/ciclo_haplonte.png"),
    "ciclo_diplonte": img_b64("fotos/ciclo_diplonte.png"),
    "ciclo_diplohaplo": img_b64("fotos/ciclo_diplohaplonte.png"),
    "maria_blasco": img_b64("fotos/maria_blasco.png")
}

# Bank of 52 detailed questions categorized into 6 sections
questions_bank = [
    # SECCIÓN 1: TEORÍA CELULAR Y MODELOS CELULARES (Págs 10 - 11)
    {
        "sec": 1,
        "cat": "2.1 Teoría Celular",
        "q": "¿Qué científico demostró que el tejido nervioso también está formado por células individuales (neuronas)?",
        "img": None,
        "opts": ["Matthias Schleiden", "Theodor Schwann", "Rudolf Virchow", "Santiago Ramón y Cajal"],
        "correct": 3,
        "expl": "Santiago Ramón y Cajal demostró en 1888 que el tejido nervioso está formado por células independientes (neuronas) gracias a su método de tinción con nitrato de plata."
    },
    {
        "sec": 1,
        "cat": "2.1 Teoría Celular",
        "q": "¿Qué famosa frase en latín acuñó Rudolf Virchow en 1858 para formular el principio de reproducción celular?",
        "img": None,
        "opts": ["Omnis cellula e cellula", "Cogito ergo sum", "Carpe diem", "Primum non nocere"],
        "correct": 0,
        "expl": "'Omnis cellula e cellula' significa 'toda célula proviene de otra célula', descartando la generación espontánea."
    },
    {
        "sec": 1,
        "cat": "2.1 Teoría Celular",
        "q": "¿Quién concluyó en 1838 que todas las PLANTAS están compuestas por unidades individuales llamadas células?",
        "img": None,
        "opts": ["Matthias Schleiden", "Theodor Schwann", "Robert Hooke", "Lynn Margulis"],
        "correct": 0,
        "expl": "El botánico alemán Matthias Schleiden inició la teoría celular en plantas en 1838."
    },
    {
        "sec": 1,
        "cat": "2.1 Teoría Celular",
        "q": "El postulado genético de la teoría celular establece que la célula es la unidad genética porque...",
        "img": None,
        "opts": [
          "Contiene ADN que regula sus funciones y se transmite a los descendientes",
          "Puede moverse libremente por la sangre",
          "Fabrica energía mediante la respiración celular",
          "Posee una pared celular externa protectora"
        ],
        "correct": 0,
        "expl": "Es la unidad genética porque alberga la información hereditaria necesaria para regular sus funciones y transmitirla a la descendencia."
    },
    {
        "sec": 1,
        "cat": "2.2 Componentes Básicos",
        "q": "Observa la imagen: ¿Cuáles son los 4 componentes universales señalados que poseen TODAS las células vivas?",
        "img": "celula_basica",
        "opts": [
          "Membrana plasmática, citoplasma, material genético (ADN) y ribosomas",
          "Núcleo, mitocondrias, citoplasma y cloroplastos",
          "Pared celular, flagelos, ADN y ribosomas",
          "Membrana nuclear, nucleolo, centrosoma y citosol"
        ],
        "correct": 0,
        "expl": "Toda célula (procariota o eucariota) comparte obligatoriamente: membrana plasmática, citoplasma, ADN y ribosomas."
    },
    {
        "sec": 1,
        "cat": "2.3 Modelos Celulares",
        "q": "Observa esta micrografía: ¿Qué tipo de célula representa este organismo con flagelos?",
        "img": "bacteria",
        "opts": ["Célula procariota (bacteria)", "Célula animal", "Célula vegetal", "Neurona"],
        "correct": 0,
        "expl": "Es una bacteria procariota: carece de núcleo verdadero, tiene forma bacilar y presenta abundantes flagelos filamentosos."
    },
    {
        "sec": 1,
        "cat": "2.3 Modelos Celulares",
        "q": "¿Dónde se localiza el material genético (ADN) en una célula procariota?",
        "img": None,
        "opts": [
          "Disperso en el citoplasma en una región llamada nucleoide",
          "Dentro de un núcleo rodeado por doble membrana",
          "En el interior de los cloroplastos",
          "Exclusivamente adherido a la pared celular"
        ],
        "correct": 0,
        "expl": "En procariotas no hay membrana nuclear; su ADN circular se halla en una región citoplasmática llamada nucleoide."
    },
    {
        "sec": 1,
        "cat": "2.3 Modelos Celulares",
        "q": "¿Cuál es la diferencia de tamaño promedio entre las células eucariotas y las procariotas?",
        "img": None,
        "opts": [
          "Las eucariotas son más de 10 veces mayores que las procariotas",
          "Las procariotas son 10 veces mayores que las eucariotas",
          "Ambas tienen exactamente el mismo tamaño (1 µm)",
          "Las procariotas son visibles a simple vista y las eucariotas no"
        ],
        "correct": 0,
        "expl": "Las procariotas miden de 0,5 a 5 µm, mientras que las eucariotas miden entre 10 y 50 µm (más de diez veces mayores de media)."
    },
    {
        "sec": 1,
        "cat": "2.3 Especialización Celular",
        "q": "Observa la imagen: ¿Qué tipo celular es esta célula alargada (elongated) adaptada para la contracción?",
        "img": "muscular",
        "opts": ["Célula muscular", "Célula nerviosa", "Célula vegetal", "Glóbulo blanco"],
        "correct": 0,
        "expl": "La célula muscular es alargada para permitir su acortamiento mecánico durante la contracción muscular."
    },
    {
        "sec": 1,
        "cat": "2.3 Especialización Celular",
        "q": "Observa la imagen: ¿Qué tipo celular presenta prolongaciones ramificadas (branch out) para conducir impulsos?",
        "img": "nerviosa",
        "opts": ["Célula nerviosa (neurona)", "Célula vegetal", "Célula muscular", "Bacteria"],
        "correct": 0,
        "expl": "Las neuronas o células nerviosas ramifican sus prolongaciones (dendritas y axón) para transmitir impulsos eléctricos a distancia."
    },
    {
        "sec": 1,
        "cat": "2.3 Especialización Celular",
        "q": "Observa la imagen: ¿Qué tipo de célula tiene forma poliédrica, pared celular y nutrición autótrofa?",
        "img": "vegetal",
        "opts": ["Célula vegetal", "Célula muscular", "Célula nerviosa", "Bacteria"],
        "correct": 0,
        "expl": "La célula vegetal es típicamente poliédrica, rodeada de pared de celulosa y realiza la fotosíntesis (nutrición autótrofa)."
    },

    # SECCIÓN 2: MEMBRANA PLASMÁTICA, TRANSPORTE Y PARED (Págs 12 - 13)
    {
        "sec": 2,
        "cat": "3.1 Membrana Plasmática",
        "q": "Observa el diagrama del modelo del mosaico fluido: ¿Cuál es la estructura lipídica básica de la membrana?",
        "img": "membrana",
        "opts": [
          "Bicapa fluida de fosfolípidos",
          "Capa sólida de celulosa",
          "Red inmóvil de microtúbulos",
          "Capa única de colesterol puro"
        ],
        "correct": 0,
        "expl": "La membrana plasmática es una bicapa fluida y asimétrica de fosfolípidos con proteínas intercaladas que se desplazan libremente."
    },
    {
        "sec": 2,
        "cat": "3.1 Membrana Plasmática",
        "q": "¿Qué lípido se encuentra en la membrana plasmática de las células ANIMALES para regular su fluidez?",
        "img": None,
        "opts": ["Colesterol", "Celulosa", "Quitina", "Peptidoglicano"],
        "correct": 0,
        "expl": "El colesterol se intercala entre los fosfolípidos en células animales para modular la fluidez y estabilidad de la membrana."
    },
    {
        "sec": 2,
        "cat": "3.1 Membrana Plasmática",
        "q": "¿Qué función cumplen los oligosacáridos (cadenas de glúcidos) en la superficie externa de la membrana?",
        "img": None,
        "opts": [
          "Reconocimiento celular e identificación de la célula (glucocálix)",
          "Fabricación de ATP por respiración",
          "Contracción y movimiento de la célula",
          "Almacenamiento de agua y turgencia"
        ],
        "correct": 0,
        "expl": "Los oligosacáridos forman el glucocálix en la cara exterior y actúan como huella dactilar de reconocimiento celular."
    },
    {
        "sec": 2,
        "cat": "3.1 Membrana Plasmática",
        "q": "¿Cuál de las siguientes NO es una función de la membrana plasmática?",
        "img": None,
        "opts": [
          "Sintetizar la mayor parte del ATP celular",
          "Rodear y proteger la célula",
          "Regular el intercambio de sustancias que entran y salen",
          "Transmitir señales químicas hacia el interior y exterior"
        ],
        "correct": 0,
        "expl": "La síntesis de ATP es función de las mitocondrias (respiración celular), no de la membrana plasmática."
    },
    {
        "sec": 2,
        "cat": "Transporte de Membrana",
        "q": "Observa la imagen: ¿Cómo cruzan los gases pequeños como el O₂ y el CO₂ la membrana plasmática?",
        "img": "transporte",
        "opts": [
          "Directamente entre los fosfolípidos de la bicapa",
          "Exclusivamente por endocitosis en grandes vesículas",
          "A través del centrosoma",
          "Unidos a fibras de celulosa"
        ],
        "correct": 0,
        "expl": "Las moléculas pequeñas y apolares (como O₂ y CO₂) atraviesan directamente la bicapa lipídica por difusión simple."
    },
    {
        "sec": 2,
        "cat": "Transporte de Membrana",
        "q": "Observa el proceso: ¿Cómo se llama la entrada de grandes partículas mediante deformación de la membrana en vesículas?",
        "img": "endocitosis",
        "opts": ["Endocitosis", "Exocitosis", "Fotosíntesis", "Fisión binaria"],
        "correct": 0,
        "expl": "La endocitosis es el mecanismo por el que la célula engloba partículas extracelulares invaginando su membrana en vesículas."
    },
    {
        "sec": 2,
        "cat": "Transporte de Membrana",
        "q": "¿Cómo se llama el proceso inverso, donde vesículas internas se fusionan con la membrana para expulsar sustancias?",
        "img": None,
        "opts": ["Exocitosis", "Endocitosis", "Mitosis", "Osmosis inversa"],
        "correct": 0,
        "expl": "La exocitosis es la expulsión o secreción de sustancias hacia el exterior celular mediante fusión de vesículas con la membrana."
    },
    {
        "sec": 2,
        "cat": "3.2 Cubiertas Celulares",
        "q": "Observa la micrografía: ¿De qué polisacárido están formadas las fibras de la pared celular vegetal?",
        "img": "pared",
        "opts": ["Celulosa", "Quitina", "Peptidoglicano", "Colesterol"],
        "correct": 0,
        "expl": "La pared vegetal de plantas y algas está compuesta por fibras del polisacárido celulosa inmersas en una matriz amorfa."
    },
    {
        "sec": 2,
        "cat": "3.2 Cubiertas Celulares",
        "q": "¿De qué componente químico está formada la pared celular de las BACTERIAS?",
        "img": None,
        "opts": ["Peptidoglicano (mureína)", "Celulosa", "Quitina", "Fosfolípidos exclusivamente"],
        "correct": 0,
        "expl": "La pared bacteriana está formada por peptidoglicanos (cadenas de glúcidos unidas por péptidos) en estructura de malla."
    },
    {
        "sec": 2,
        "cat": "3.2 Cubiertas Celulares",
        "q": "¿Qué sustancia polisacárida compone la pared celular de los HONGOS?",
        "img": None,
        "opts": ["Quitina", "Celulosa", "Peptidoglicano", "Glucógeno"],
        "correct": 0,
        "expl": "La pared de las células fúngicas (hongos y levaduras) está formada por quitina."
    },

    # SECCIÓN 3: CITOPLASMA Y CITOESQUELETO (Pág 14)
    {
        "sec": 3,
        "cat": "3.3 Citoplasma",
        "q": "¿Qué es el citosol o hialoplasma?",
        "img": None,
        "opts": [
          "La matriz líquida intracelular donde ocurren las reacciones del metabolismo",
          "La membrana que rodea al núcleo",
          "El espacio interior de los centriolos",
          "La pared celular de las bacterias"
        ],
        "correct": 0,
        "expl": "El citosol es el fluido acuoso del citoplasma compuesto por agua, sales, proteínas y nutrientes, donde ocurre el metabolismo."
    },
    {
        "sec": 3,
        "cat": "3.3 Citoesqueleto",
        "q": "Observa el diagrama: ¿Qué estructura filamentosa sostiene los orgánulos y da forma a la célula eucariota?",
        "img": "citoesq_diag",
        "opts": ["El citoesqueleto", "La pared celular", "El aparato de Golgi", "Los ribosomas"],
        "correct": 0,
        "expl": "El citoesqueleto es una red tridimensional dinámica de filamentos proteicos que sostiene orgánulos y organiza el tráfico interno."
    },
    {
        "sec": 3,
        "cat": "3.3 Citoesqueleto",
        "q": "¿Qué proteína forma los microfilamentos (los filamentos más delgados y frágiles del citoesqueleto)?",
        "img": None,
        "opts": ["Actina", "Tubulina", "Citoqueratina", "Celulosa"],
        "correct": 0,
        "expl": "Los microfilamentos están formados por polimerización en doble hélice de la proteína actina."
    },
    {
        "sec": 3,
        "cat": "3.3 Citoesqueleto",
        "q": "¿Qué filamentos proteicos tipo cuerda, exclusivos de células animales, aportan la máxima resistencia mecánica?",
        "img": None,
        "opts": ["Filamentos intermedios (citoqueratina)", "Microtúbulos", "Microfilamentos", "Fibras de celulosa"],
        "correct": 0,
        "expl": "Los filamentos intermedios (como la citoqueratina) son los más resistentes del citoesqueleto y soportan tensiones mecánicas."
    },
    {
        "sec": 3,
        "cat": "3.3 Citoesqueleto",
        "q": "Observa esta micrografía óptica: ¿Qué proteína forma los microtúbulos (cilindros huecos y rígidos mostrados en amarillo)?",
        "img": "citoesq_micro",
        "opts": ["Tubulina", "Actina", "Colágeno", "Miosina"],
        "correct": 0,
        "expl": "Los microtúbulos están formados por cilindros huecos de la proteína tubulina, y son los filamentos más gruesos del citoesqueleto."
    },

    # SECCIÓN 4: ORGÁNULOS DE MEMBRANA SIMPLE: RE, GOLGI, LISOSOMAS, VACUOLAS (Págs 15 - 16)
    {
        "sec": 4,
        "cat": "Retículo Endoplasmático",
        "q": "Observa el diagrama: ¿Qué parte del retículo presenta ribosomas adheridos en su superficie?",
        "img": "reticulo_diag",
        "opts": [
          "Retículo endoplasmático rugoso (RER)",
          "Retículo endoplasmático liso (REL)",
          "Aparato de Golgi",
          "Matriz mitocondrial"
        ],
        "correct": 0,
        "expl": "El RER tiene ribosomas adheridos en su cara externa, lo que le da aspecto rugoso, y sintetiza proteínas de membrana y secreción."
    },
    {
        "sec": 4,
        "cat": "Retículo Endoplasmático",
        "q": "¿Cuál es la función principal del Retículo Endoplasmático LISO (REL)?",
        "img": None,
        "opts": [
          "Sintetizar lípidos de membrana y detoxificar sustancias tóxicas",
          "Sintetizar proteínas para la exportación",
          "Realizar la fotosíntesis con luz solar",
          "Almacenar los cromosomas de la célula"
        ],
        "correct": 0,
        "expl": "El REL carece de ribosomas y se encarga de sintetizar lípidos (fosfolípidos, colesterol) y destruir sustancias tóxicas o fármacos."
    },
    {
        "sec": 4,
        "cat": "Retículo Endoplasmático",
        "q": "Observa la micrografía electrónica: ¿Qué orgánulo muestra estas membranas paralelas con ribosomas incrustados?",
        "img": "reticulo_micro",
        "opts": [
          "Retículo endoplasmático rugoso (RER)",
          "Aparato de Golgi",
          "Cloroplasto",
          "Centrosoma"
        ],
        "correct": 0,
        "expl": "La micrografía muestra las cisternas membranosas paralelas del RER salpicadas de pequeños ribosomas electrodensos."
    },
    {
        "sec": 4,
        "cat": "Aparato de Golgi",
        "q": "Observa el diagrama: ¿Qué unidades estructurales (pilas de sacos aplanados) forman el Aparato de Golgi?",
        "img": "golgi_diag",
        "opts": ["Dictiosomas", "Centriolos", "Tilacoides", "Grana"],
        "correct": 0,
        "expl": "El aparato de Golgi está formado por dictiosomas, que son apilamientos de sacos discoidales delimitados por membrana lisa."
    },
    {
        "sec": 4,
        "cat": "Aparato de Golgi",
        "q": "En el aparato de Golgi, ¿qué cara recibe las vesículas de transición procedentes del RER?",
        "img": None,
        "opts": [
          "Cara Cis (o de formación)",
          "Cara Trans (o de maduración)",
          "Cresta mitocondrial",
          "Matriz amorfa"
        ],
        "correct": 0,
        "expl": "La cara Cis está orientada hacia el retículo y recibe sus vesículas de transición; la cara Trans libera vesículas de secreción."
    },
    {
        "sec": 4,
        "cat": "Aparato de Golgi",
        "q": "Observa la micrografía: ¿Qué orgánulo modifica proteínas (glucosilación) y origina los lisosomas?",
        "img": "golgi_micro",
        "opts": ["Aparato de Golgi", "Mitocondria", "Ribosoma", "Centrosoma"],
        "correct": 0,
        "expl": "El aparato de Golgi modifica lípidos y proteínas procedentes del retículo, empaqueta vesículas y forma los lisosomas."
    },
    {
        "sec": 4,
        "cat": "Lisosomas",
        "q": "Observa la micrografía: ¿Qué orgánulos (en azul) contienen enzimas hidrolíticas para la digestión celular?",
        "img": "lisosomas_micro",
        "opts": ["Lisosomas", "Vacuolas", "Ribosomas", "Mitocondrias"],
        "correct": 0,
        "expl": "Los lisosomas son vesículas digestivas ácidas formadas por el Golgi que digieren desechos, bacterias y orgánulos viejos (autofagia)."
    },
    {
        "sec": 4,
        "cat": "Vacuolas",
        "q": "¿Qué orgánulo de membrana simple ocupa gran parte del volumen de las células VEGETALES y mantiene su turgencia?",
        "img": None,
        "opts": ["Vacuola central", "Centrosoma", "Lisosoma", "Dictiosoma"],
        "correct": 0,
        "expl": "Las vacuolas vegetales son de gran tamaño, almacenan agua y sales, y generan la presión de turgencia que da firmeza a la planta."
    },

    # SECCIÓN 5: MITOCONDRIAS, CLORO雇LASTOS Y TEORÍA ENDOSIMBIÓTICA (Págs 16 - 17)
    {
        "sec": 5,
        "cat": "Mitocondrias",
        "q": "Observa el diagrama: ¿Qué orgánulo de DOBLE membrana genera ATP mediante la respiración celular?",
        "img": "mitoc_diag",
        "opts": ["Mitocondria", "Cloroplasto", "Aparato de Golgi", "Lisosoma"],
        "correct": 0,
        "expl": "La mitocondria tiene doble membrana, crestas internas y matriz; en ella tiene lugar la respiración celular aeróbica generadora de ATP."
    },
    {
        "sec": 5,
        "cat": "Mitocondrias",
        "q": "Observa la micrografía: ¿Cómo se llaman los repliegues de la membrana interna mitocondrial?",
        "img": "mitoc_micro",
        "opts": ["Crestas mitocondriales", "Tilacoides", "Dictiosomas", "Centriolos"],
        "correct": 0,
        "expl": "La membrana interna de la mitocondria se pliega formando crestas mitocondriales para aumentar la superficie de producción de energía."
    },
    {
        "sec": 5,
        "cat": "Mitocondrias",
        "q": "¿Cuál es la ecuación química general de la respiración celular aeróbica en las mitocondrias?",
        "img": None,
        "opts": [
          "Glucosa + 6 O₂ ➔ 6 CO₂ + 6 H₂O + Energía (ATP)",
          "6 CO₂ + 6 H₂O + Luz ➔ Glucosa + 6 O₂",
          "Glucosa ➔ 2 Ácido láctico + ATP",
          "6 O₂ + 6 H₂O ➔ Glucosa + ATP"
        ],
        "correct": 0,
        "expl": "La respiración celular combina glucosa y oxígeno para producir dióxido de carbono, agua y gran cantidad de energía química (ATP)."
    },
    {
        "sec": 5,
        "cat": "Cloroplastos",
        "q": "Observa el diagrama: ¿Cómo se llaman los sacos aplanados membranosos del cloroplasto apilados en grana?",
        "img": "cloro_diag",
        "opts": ["Tilacoides", "Crestas", "Centriolos", "Dictiosomas"],
        "correct": 0,
        "expl": "Los tilacoides son sacos membranosos que contienen clorofila; cuando se apilan forman estructuras denominadas grana."
    },
    {
        "sec": 5,
        "cat": "Cloroplastos",
        "q": "Observa la micrografía: ¿En qué orgánulo exclusivo vegetal se realiza la fotosíntesis?",
        "img": "cloro_micro",
        "opts": ["Cloroplasto", "Mitocondria", "Lisosoma", "Centrosoma"],
        "correct": 0,
        "expl": "El cloroplasto es el orgánulo vegetal responsable de la fotosíntesis, capturando la energía solar para fijar CO₂ y formar glucosa."
    },
    {
        "sec": 5,
        "cat": "Cloroplastos",
        "q": "¿Dónde ocurre la fase dependiente de la luz (luminosa) de la fotosíntesis dentro del cloroplasto?",
        "img": None,
        "opts": [
          "En la membrana de los tilacoides",
          "En el estroma",
          "En el espacio intermembrana",
          "En la pared celular"
        ],
        "correct": 0,
        "expl": "La fase luminosa ocurre en los tilacoides (donde está la clorofila), mientras que la fase oscura (fijación de CO₂) tiene lugar en el estroma."
    },
    {
        "sec": 5,
        "cat": "Teoría Endosimbiótica",
        "q": "Observa el esquema: ¿Qué prestigiosa bióloga formuló la Teoría Endosimbiótica sobre el origen de mitocondrias y cloroplastos?",
        "img": "endosimbiotica",
        "opts": ["Lynn Margulis", "Rosalind Franklin", "Jane Goodall", "Marie Curie"],
        "correct": 0,
        "expl": "Lynn Margulis demostró que mitocondrias y cloroplastos proceden de bacterias procariotas fagocitadas por células ancestrales."
    },
    {
        "sec": 5,
        "cat": "Teoría Endosimbiótica",
        "q": "Según la teoría endosimbiótica, ¿qué bacteria primitiva fue fagocitada para originar los CLOROPLASTOS?",
        "img": None,
        "opts": [
          "Bacterias fotosintéticas (cianobacterias)",
          "Bacterias aerobias heterótrofas",
          "Arqueas metanógenas",
          "Virus bacteriófagos"
        ],
        "correct": 0,
        "expl": "En la endosimbiosis secundaria, la ingestión simbiótica de cianobacterias fotosintéticas dio origen a los cloroplastos vegetales."
    },
    {
        "sec": 5,
        "cat": "Teoría Endosimbiótica",
        "q": "¿Cuál de las siguientes es una prueba irrefutable de que mitocondrias y cloroplastos fueron bacterias libres?",
        "img": None,
        "opts": [
          "Tienen doble membrana, ADN circular propio y se dividen por fisión binaria",
          "Tienen una pared celular gruesa de celulosa",
          "Carecen de ribosomas en su interior",
          "Están formados exclusivamente por actina y miosina"
        ],
        "correct": 0,
        "expl": "Ambos orgánulos conservan su propio ADN circular bacteriano, ribosomas 70S y se dividen por fisión binaria de manera autónoma."
    },

    # SECCIÓN 6: ORGÁNULOS SIN MEMBRANA: RIBOSOMAS Y CENTROSOMA (Pág 18)
    {
        "sec": 6,
        "cat": "Ribosomas",
        "q": "Observa el diagrama: ¿Qué orgánulo sin membrana está formado por dos subunidades (mayor y menor)?",
        "img": "ribos_diag",
        "opts": ["Ribosoma", "Centrosoma", "Mitocondria", "Lisosoma"],
        "correct": 0,
        "expl": "Los ribosomas están formados por dos subunidades (grande y pequeña) de ARNr y proteínas, y carecen de envoltura membranosa."
    },
    {
        "sec": 6,
        "cat": "Ribosomas",
        "q": "Observa la micrografía: ¿Cuál es la función vital de los ribosomas (a los que Blanca llamó 'los obreros')?",
        "img": "ribos_micro",
        "opts": [
          "Sintetizar proteínas a partir de la información genética",
          "Destruir toxinas y fármacos",
          "Fabricar glucosa mediante fotosíntesis",
          "Mantener la turgencia de la célula"
        ],
        "correct": 0,
        "expl": "Los ribosomas traducen el mensaje genético del ARN mensajero para sintetizar cadenas de proteínas."
    },
    {
        "sec": 6,
        "cat": "Ribosomas",
        "q": "¿En cuál de los siguientes lugares NO encontramos ribosomas?",
        "img": None,
        "opts": [
          "En el interior de los lisosomas",
          "Libres en el citoplasma",
          "Adheridos a la cara externa del RER",
          "En la matriz mitocondrial y estroma de cloroplastos"
        ],
        "correct": 0,
        "expl": "Los lisosomas contienen enzimas digestivas ácidas, no ribosomas. Los ribosomas están libres en el citosol, en el RER, en mitocondrias y cloroplastos."
    },
    {
        "sec": 6,
        "cat": "Centrosoma",
        "q": "Observa el diagrama: ¿Qué orgánulo sin membrana, exclusivo de células ANIMALES, contiene el diplosoma?",
        "img": "centro_diag",
        "opts": ["Centrosoma", "Aparato de Golgi", "Cloroplasto", "Vacuola"],
        "correct": 0,
        "expl": "El centrosoma es exclusivo de animales; contiene el diplosoma (dos centriolos perpendiculares rodeados de material pericentriolar y áster)."
    },
    {
        "sec": 6,
        "cat": "Centrosoma",
        "q": "Observa la micrografía: ¿Cómo están organizados los microtúbulos de tubulina en la pared de cada centriolo?",
        "img": "centro_micro",
        "opts": [
          "9 tripletes de microtúbulos (9 x 3)",
          "Bicapa de fosfolípidos",
          "Doble hélice de actina",
          "Fibras paralelas de celulosa"
        ],
        "correct": 0,
        "expl": "Cada centriolo cilíndrico está formado por 9 tripletes de microtúbulos de tubulina dispuestos en círculo (estructura 9x3)."
    },
    {
        "sec": 6,
        "cat": "Centrosoma",
        "q": "¿Qué estructura esencial para la división celular (mitosis y meiosis) se origina a partir del centrosoma?",
        "img": None,
        "opts": [
          "El huso acromático / mitótico",
          "La pared celular de celulosa",
          "La bicapa lipídica de la membrana",
          "Los dictiosomas del Golgi"
        ],
        "correct": 0,
        "expl": "El centrosoma organiza el huso mitótico durante la división celular para separar y repartir equitativamente los cromosomas."
    },
    {
        "sec": 6,
        "cat": "Centrosoma",
        "q": "¿Qué estructuras móviles de la superficie celular se forman también a partir de los microtúbulos del centrosoma?",
        "img": None,
        "opts": [
          "Cilios y flagelos",
          "Paredes celulares y plasmodesmos",
          "Mitocondrias y cloroplastos",
          "Lisosomas y vacuolas"
        ],
        "correct": 0,
        "expl": "Los cilios (cortos y numerosos) y los flagelos (largos y escasos) están formados por microtúbulos originados a partir de los centriolos."
    },
    {"sec": 7, "cat": "4.1 Estructura del Cromosoma", "q": "¿Cómo se denominan los extremos redondeados de las cromátidas que protegen al cromosoma de la degradación?", "img": None, "opts": ["Centrómeros", "Telómeros", "Cinetocoros", "Satélites"], "correct": 1, "expl": "Los telómeros son secuencias protectoras situadas en los extremos de las cromátidas esenciales para la estabilidad del cromosoma."},
    {"sec": 7, "cat": "4.1 Científicos Españoles", "q": "¿Qué prestigiosa científica española es pionera mundial en el estudio de los telómeros y el envejecimiento desde el CNIO?", "img": "maria_blasco", "opts": ["Margarita Salas", "María Antonia Blasco", "Elena García Armada", "Josefina Castellví"], "correct": 1, "expl": "María Antonia Blasco lidera las investigaciones internacionales sobre telómeros y cáncer en el CNIO."},
    {"sec": 7, "cat": "4.2 Tipos de Cromosomas", "q": "¿Cómo se clasifica un cromosoma cuyo centrómero está en el centro exacto y sus brazos tienen la misma longitud?", "img": "cromo_tipos", "opts": ["Submetacéntrico", "Acrocéntrico", "Metacéntrico", "Telocéntrico"], "correct": 2, "expl": "En los cromosomas metacéntricos el centrómero está en el punto medio exacto y los brazos p y q son de igual longitud."},
    {"sec": 7, "cat": "4.2 Tipos de Cromosomas", "q": "¿Cuál de las siguientes morfologías cromosómicas NO existe en la especie humana?", "img": None, "opts": ["Metacéntrico", "Acrocéntrico", "Submetacéntrico", "Telocéntrico"], "correct": 3, "expl": "Los seres humanos no poseemos ningún cromosoma telocéntrico (con el centrómero en el extremo terminal absoluto)."},
    {"sec": 7, "cat": "4.3 Cariotipo y Ploidía", "q": "¿Cuál es la dotación cromosómica normal de las células somáticas de la especie humana?", "img": None, "opts": ["n = 23 cromosomas", "2n = 46 cromosomas", "2n = 48 cromosomas", "4n = 92 cromosomas"], "correct": 1, "expl": "Las células somáticas humanas son diploides con 2n = 46 cromosomas (22 pares de autosomas y 1 par de heterocromosomas sexuales)."},
    {"sec": 7, "cat": "4.3 Cariotipo Humano", "q": "¿En cuántos grupos morfológicos (del A al G) se ordenan los cromosomas en el cariotipo humano?", "img": "cariotipo_real", "opts": ["5 grupos", "7 grupos", "10 grupos", "23 grupos"], "correct": 1, "expl": "Los cromosomas humanos se clasifican en 7 grupos (de la A a la G) según su tamaño decreciente y la posición del centrómero."},
    {"sec": 7, "cat": "4.3 Cromosomas Sexuales", "q": "¿Cómo se denominan los cromosomas que determinan el sexo biológico en los mamíferos?", "img": None, "opts": ["Autosomas", "Heterocromosomas (o sexuales)", "Histonas", "Cinetocoros"], "correct": 1, "expl": "Los heterocromosomas o cromosomas sexuales (X e Y) determinan el sexo: XX en hembras y XY en machos."},
    {"sec": 8, "cat": "5.1 División Procariota", "q": "¿Mediante qué mecanismo asexual se dividen las células procariotas como las bacterias?", "img": "fision_binaria", "opts": ["Mitosis", "Meiosis", "Fisión binaria (o bipartición)", "Esporulación meiótica"], "correct": 2, "expl": "Las bacterias se reproducen asexualmente por fisión binaria o amitosis, duplicando su ADN circular y dividiéndose por un septo central."},
    {"sec": 8, "cat": "5.2 Mitosis", "q": "A partir de una célula madre diploide (2n = 4), ¿qué células se obtienen al terminar la mitosis?", "img": "mitosis_diag", "opts": ["4 células haploides (n = 2)", "2 células hijas idénticas (2n = 4)", "1 célula con 4 núcleos", "2 células haploides (n = 4)"], "correct": 1, "expl": "La mitosis es una división ecuacional que genera 2 células hijas con el mismo número de cromosomas e idéntica información genética (2n -> 2n)."},
    {"sec": 8, "cat": "5.2 Meiosis", "q": "¿Cuál es la función biológica principal de la meiosis en organismos con reproducción sexual?", "img": "meiosis_diag", "opts": ["El crecimiento del cuerpo", "Reparar heridas en tejidos", "Formar 4 gametos haploides (n) y aportar variabilidad genética", "Duplicar el número de cromosomas"], "correct": 2, "expl": "La meiosis reduce a la mitad el número de cromosomas para formar gametos (n) y genera variabilidad genética mediante recombinación."},
    {"sec": 8, "cat": "5.3 Ciclos Biológicos", "q": "¿En qué tipo de ciclo biológico el organismo adulto es diploide (2n) y la meiosis solo produce gametos?", "img": "ciclo_diplonte", "opts": ["Ciclo haplonte", "Ciclo diplonte", "Ciclo haplodiplonte", "Ciclo esporofítico puro"], "correct": 1, "expl": "El ciclo diplonte es típico de los animales: el individuo adulto es 2n y únicamente fabrica gametos haploides mediante meiosis."},
    {"sec": 8, "cat": "5.3 Ciclos Biológicos", "q": "En el ciclo haplodiplonte de las plantas, ¿cómo se denomina el adulto diploide (2n) que produce esporas por meiosis?", "img": "ciclo_diplohaplo", "opts": ["Gametofito", "Esporofito", "Zigoto", "Cariotipo"], "correct": 1, "expl": "El esporofito es la fase adulta diploide (2n) de las plantas formadora de meiosporas, mientras que el gametofito es la fase haploide (n)."},
    {"sec": 8, "cat": "5.3 Reproducción Comparada", "q": "¿Cuál es la principal ventaja evolutiva de la reproducción sexual frente a la asexual?", "img": None, "opts": ["No necesita buscar pareja", "Aporta variabilidad genética para adaptarse a cambios ambientales", "Requiere menos energía", "Genera millones de clones idénticos rápidamente"], "correct": 1, "expl": "La variabilidad genética generada por la meiosis y la fecundación es la base de la adaptación y la evolución biológica."},
]

print(f"Total de preguntas en el banco: {len(questions_bank)}")

# Template HTML
html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Kahoot! Master Challenge: Tema 2 La Célula (4º ESO)</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@600;700;800;900&family=Plus+Jakarta+Sans:wght@500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {{
      --k-red: #e21b3c;
      --k-blue: #1368ce;
      --k-yellow: #d89e00;
      --k-green: #26890c;
      --k-purple: #46178f;
      --k-dark: #12072b;
      --k-card: #200d43;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: 'Montserrat', sans-serif;
      background: radial-gradient(circle at 50% 20%, #46178f 0%, #12072b 100%);
      color: #ffffff;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 1rem;
      overflow-x: hidden;
    }}

    .game-container {{
      width: 100%;
      max-width: 950px;
      background: rgba(32, 13, 67, 0.9);
      backdrop-filter: blur(14px);
      border: 2px solid rgba(255, 255, 255, 0.15);
      border-radius: 1.5rem;
      padding: 2rem;
      box-shadow: 0 25px 60px rgba(0, 0, 0, 0.6);
      text-align: center;
      position: relative;
    }}

    /* SCREEN 1: SETUP SCREEN */
    .setup-screen {{
      display: block;
    }}

    .logo-badge {{
      display: inline-block;
      background: linear-gradient(135deg, #ffd700, #ff8c00);
      color: #12072b;
      font-weight: 900;
      font-size: 0.9rem;
      padding: 0.4rem 1.2rem;
      border-radius: 999px;
      margin-bottom: 0.8rem;
      letter-spacing: 0.05em;
      text-transform: uppercase;
      box-shadow: 0 4px 15px rgba(255, 215, 0, 0.3);
    }}

    h1 {{
      font-size: 2.2rem;
      font-weight: 900;
      margin-bottom: 0.5rem;
      letter-spacing: -0.02em;
    }}

    .setup-desc {{
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-size: 1rem;
      color: #cbd5e1;
      max-width: 650px;
      margin: 0 auto 1.5rem;
      line-height: 1.5;
    }}

    .section-selector {{
      background: rgba(18, 7, 43, 0.7);
      border: 1.5px solid rgba(255, 255, 255, 0.12);
      border-radius: 1rem;
      padding: 1.25rem;
      margin-bottom: 1.5rem;
      text-align: left;
    }}

    .sec-sel-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 1rem;
      flex-wrap: wrap;
      gap: 0.5rem;
    }}

    .sec-sel-title {{
      font-weight: 800;
      font-size: 1.1rem;
      color: #ffd700;
    }}

    .btn-quick-sel {{
      background: rgba(255, 255, 255, 0.15);
      border: none;
      color: #ffffff;
      padding: 0.3rem 0.8rem;
      border-radius: 999px;
      font-family: inherit;
      font-size: 0.8rem;
      font-weight: 700;
      cursor: pointer;
      transition: background 0.2s;
    }}

    .btn-quick-sel:hover {{
      background: rgba(255, 255, 255, 0.3);
    }}

    .checkbox-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 0.75rem;
    }}

    @media (max-width: 650px) {{
      .checkbox-grid {{
        grid-template-columns: 1fr;
      }}
    }}

    .check-label {{
      display: flex;
      align-items: center;
      gap: 0.65rem;
      background: rgba(255, 255, 255, 0.05);
      padding: 0.65rem 0.9rem;
      border-radius: 0.65rem;
      cursor: pointer;
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-size: 0.92rem;
      font-weight: 600;
      color: #f1f5f9;
      border: 1px solid rgba(255, 255, 255, 0.08);
      transition: all 0.2s;
    }}

    .check-label:hover {{
      background: rgba(255, 255, 255, 0.12);
      border-color: #ffd700;
    }}

    .check-label input[type="checkbox"] {{
      width: 18px;
      height: 18px;
      accent-color: #ffd700;
      cursor: pointer;
    }}

    .options-row {{
      display: flex;
      justify-content: center;
      gap: 1.5rem;
      margin-bottom: 1.75rem;
      flex-wrap: wrap;
    }}

    .option-group {{
      display: flex;
      align-items: center;
      gap: 0.5rem;
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-size: 0.95rem;
      font-weight: 600;
    }}

    .select-input {{
      background: #12072b;
      color: #ffffff;
      border: 1.5px solid rgba(255, 255, 255, 0.25);
      border-radius: 0.5rem;
      padding: 0.4rem 0.8rem;
      font-family: 'Montserrat', sans-serif;
      font-weight: 700;
      font-size: 0.9rem;
      cursor: pointer;
    }}

    .btn-start-game {{
      background: linear-gradient(135deg, #10b981, #059669);
      border: none;
      color: #ffffff;
      padding: 1rem 3rem;
      border-radius: 999px;
      font-family: 'Montserrat', sans-serif;
      font-size: 1.3rem;
      font-weight: 900;
      cursor: pointer;
      box-shadow: 0 8px 25px rgba(16, 185, 129, 0.4);
      transition: all 0.2s ease;
      letter-spacing: 0.02em;
    }}

    .btn-start-game:hover {{
      transform: scale(1.04);
      filter: brightness(1.1);
    }}

    /* SCREEN 2: GAME SCREEN */
    .game-screen {{
      display: none;
    }}

    .top-bar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 1rem;
      padding-bottom: 0.75rem;
      border-bottom: 2px solid rgba(255, 255, 255, 0.1);
      font-size: 1.05rem;
      font-weight: 800;
    }}

    .q-counter {{
      background: rgba(255, 255, 255, 0.15);
      padding: 0.35rem 1rem;
      border-radius: 999px;
    }}

    .score-badge {{
      background: linear-gradient(135deg, #ffd700, #ff8c00);
      color: #000;
      padding: 0.35rem 1.2rem;
      border-radius: 999px;
      font-weight: 900;
      box-shadow: 0 4px 15px rgba(255, 215, 0, 0.3);
    }}

    .question-category {{
      font-size: 0.85rem;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: #ffd700;
      font-weight: 800;
      margin-bottom: 0.4rem;
    }}

    .question-box {{
      background: #ffffff;
      color: #12072b;
      padding: 1.25rem 1.5rem;
      border-radius: 1rem;
      font-size: 1.25rem;
      font-weight: 800;
      line-height: 1.35;
      margin-bottom: 1rem;
      box-shadow: 0 8px 25px rgba(0, 0, 0, 0.25);
      min-height: 80px;
      display: flex;
      align-items: center;
      justify-content: center;
    }}

    /* OPTIONAL QUESTION IMAGE */
    .q-img-wrap {{
      max-width: 420px;
      margin: 0 auto 1.25rem;
      border-radius: 0.85rem;
      overflow: hidden;
      border: 2px solid rgba(255, 255, 255, 0.2);
      box-shadow: 0 6px 20px rgba(0, 0, 0, 0.4);
      background: #000;
      display: none;
    }}

    .q-img-wrap img {{
      width: 100%;
      max-height: 220px;
      object-fit: contain;
      display: block;
    }}

    /* ANSWERS GRID */
    .answers-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 0.85rem;
      margin-bottom: 1.25rem;
    }}

    @media (max-width: 600px) {{
      .answers-grid {{
        grid-template-columns: 1fr;
      }}
    }}

    .btn-ans {{
      border: none;
      border-radius: 0.85rem;
      padding: 1.1rem 1.2rem;
      font-family: 'Montserrat', sans-serif;
      font-size: 1rem;
      font-weight: 800;
      color: #ffffff;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 0.85rem;
      text-align: left;
      transition: all 0.15s ease;
      box-shadow: 0 5px 0 rgba(0, 0, 0, 0.25);
    }}

    .btn-ans:hover {{
      transform: translateY(-2px);
      box-shadow: 0 7px 0 rgba(0, 0, 0, 0.25);
      filter: brightness(1.1);
    }}

    .btn-ans:active {{
      transform: translateY(3px);
      box-shadow: 0 2px 0 rgba(0, 0, 0, 0.25);
    }}

    .shape-icon {{
      font-size: 1.4rem;
      display: inline-block;
      line-height: 1;
    }}

    .opt-red {{ background: var(--k-red); }}
    .opt-blue {{ background: var(--k-blue); }}
    .opt-yellow {{ background: var(--k-yellow); }}
    .opt-green {{ background: var(--k-green); }}

    /* FEEDBACK BANNER */
    .feedback-banner {{
      display: none;
      padding: 1.1rem 1.25rem;
      border-radius: 0.85rem;
      margin-bottom: 1.25rem;
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-size: 0.95rem;
      line-height: 1.4;
      font-weight: 600;
      text-align: left;
    }}

    .feedback-banner.correct {{
      background: rgba(38, 137, 12, 0.35);
      border: 2px solid var(--k-green);
      color: #a3e635;
    }}

    .feedback-banner.incorrect {{
      background: rgba(226, 27, 60, 0.35);
      border: 2px solid var(--k-red);
      color: #fca5a5;
    }}

    .btn-next {{
      background: linear-gradient(135deg, #10b981, #059669);
      border: none;
      color: #ffffff;
      padding: 0.85rem 2.5rem;
      border-radius: 999px;
      font-family: 'Montserrat', sans-serif;
      font-size: 1.15rem;
      font-weight: 900;
      cursor: pointer;
      display: none;
      margin: 0 auto;
      box-shadow: 0 6px 20px rgba(16, 185, 129, 0.4);
      transition: all 0.2s;
    }}

    .btn-next:hover {{
      transform: scale(1.05);
      filter: brightness(1.1);
    }}

    /* SCREEN 3: RESULTS SCREEN */
    .results-screen {{
      display: none;
      padding: 1.5rem 0.5rem;
    }}

    .results-title {{
      font-size: 2.3rem;
      font-weight: 900;
      margin-bottom: 0.5rem;
    }}

    .final-score {{
      font-size: 3.8rem;
      font-weight: 900;
      color: #ffd700;
      margin-bottom: 0.5rem;
      text-shadow: 0 0 30px rgba(255, 215, 0, 0.5);
    }}

    .results-desc {{
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-size: 1.1rem;
      color: #e2e8f0;
      max-width: 600px;
      margin: 0 auto 1.5rem;
      line-height: 1.5;
    }}

    .review-list {{
      background: rgba(18, 7, 43, 0.7);
      border-radius: 1rem;
      padding: 1.25rem;
      max-height: 280px;
      overflow-y: auto;
      margin-bottom: 1.5rem;
      text-align: left;
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-size: 0.9rem;
    }}

    .review-item {{
      padding: 0.6rem 0;
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    }}
    .review-item:last-child {{
      border-bottom: none;
    }}
  </style>
</head>
<body>

  <div class="game-container">

    <!-- SCREEN 1: SETUP SCREEN -->
    <div id="setupScreen" class="setup-screen">
      <div class="logo-badge">Biología 4º ESO • Banco Dinámico de Preguntas</div>
      <h1>KAHOOT! LA CÉLULA</h1>
      <p class="setup-desc">
        Personaliza tu test seleccionando las partes del tema que deseas repasar. Las preguntas y opciones saldrán de forma totalmente aleatoria con imágenes reales del libro.
      </p>

      <div class="section-selector">
        <div class="sec-sel-header">
          <span class="sec-sel-title">Selecciona los bloques temáticos a evaluar:</span>
          <div>
            <button class="btn-quick-sel" onclick="selectAll(true)">Seleccionar Todo</button>
            <button class="btn-quick-sel" onclick="selectAll(false)">Deseleccionar</button>
          </div>
        </div>

        <div class="checkbox-grid">
          <label class="check-label">
            <input type="checkbox" class="sec-check" value="1" checked>
            <span>Bloque 1: Teoría Celular y Modelos (Págs 10 - 11)</span>
          </label>
          <label class="check-label">
            <input type="checkbox" class="sec-check" value="2" checked>
            <span>Bloque 2: Membrana, Transporte y Pared (Págs 12 - 13)</span>
          </label>
          <label class="check-label">
            <input type="checkbox" class="sec-check" value="3" checked>
            <span>Bloque 3: Citoplasma y Citoesqueleto (Pág 14)</span>
          </label>
          <label class="check-label">
            <input type="checkbox" class="sec-check" value="4" checked>
            <span>Bloque 4: RE, Golgi, Lisosomas y Vacuolas (Págs 15 - 16)</span>
          </label>
          <label class="check-label">
            <input type="checkbox" class="sec-check" value="5" checked>
            <span>Bloque 5: Mitocondrias, Cloroplastos y Margulis (Págs 16 - 17)</span>
          </label>
          <label class="check-label">
            <input type="checkbox" class="sec-check" value="6" checked>
            <span>Bloque 6: Ribosomas y Centrosoma (Pág 18)</span>
          </label>
        </div>
      </div>

      <div class="options-row">
        <div class="option-group">
          <span>Número de preguntas:</span>
          <select id="selectNumQ" class="select-input">
            <option value="10">10 preguntas (Rápido)</option>
            <option value="15" selected>15 preguntas (Estándar)</option>
            <option value="20">20 preguntas (Profundo)</option>
            <option value="999">Todas las disponibles</option>
          </select>
        </div>
      </div>

      <button class="btn-start-game" onclick="startGame()">¡Comenzar Kahoot! 🚀</button>
    </div>

    <!-- SCREEN 2: GAMEPLAY SCREEN -->
    <div id="gameScreen" class="game-screen">
      <div class="top-bar">
        <div class="q-counter" id="qCounter">Pregunta 1 de 15</div>
        <div class="score-badge" id="scoreBadge">0 pts</div>
      </div>

      <div class="question-category" id="qCategory">2.1 TEORÍA CELULAR</div>
      <div class="question-box" id="qText">
        Cargando pregunta...
      </div>

      <div class="q-img-wrap" id="qImgWrap">
        <img id="qImg" src="" alt="Imagen de la pregunta">
      </div>

      <div class="feedback-banner" id="feedbackBanner"></div>

      <div class="answers-grid" id="answersGrid">
        <button class="btn-ans opt-red" onclick="handleAnswer(0)">
          <span class="shape-icon">▲</span>
          <span id="optText0">Opción 1</span>
        </button>
        <button class="btn-ans opt-blue" onclick="handleAnswer(1)">
          <span class="shape-icon">◆</span>
          <span id="optText1">Opción 2</span>
        </button>
        <button class="btn-ans opt-yellow" onclick="handleAnswer(2)">
          <span class="shape-icon">●</span>
          <span id="optText2">Opción 3</span>
        </button>
        <button class="btn-ans opt-green" onclick="handleAnswer(3)">
          <span class="shape-icon">■</span>
          <span id="optText3">Opción 4</span>
        </button>
      </div>

      <button class="btn-next" id="btnNext" onclick="nextQuestion()">Siguiente Pregunta ➔</button>
    </div>

    <!-- SCREEN 3: RESULTS SCREEN -->
    <div id="resultsScreen" class="results-screen">
      <div class="results-title">🏆 ¡TEST COMPLETADO!</div>
      <div class="final-score" id="finalScoreText">1500 pts</div>
      <div class="results-desc" id="resultsFeedback">
        ¡Enhorabuena, Blanca! Dominas completamente la citología.
      </div>

      <div class="review-list" id="reviewList">
        <div style="font-weight:700; margin-bottom:0.5rem; color:#ffd700;">Resumen de tu sesión:</div>
      </div>

      <button class="btn-start-game" onclick="restartToSetup()">Jugar Otra Partida 🔄</button>
    </div>

  </div>

  <script>
    // Embedded images dictionary
    const imgData = {json.dumps(images)};

    // Master Question Bank
    const masterBank = {json.dumps(questions_bank)};

    let activeQuestions = [];
    let currentIdx = 0;
    let score = 0;
    let answered = false;
    let sessionResults = [];

    // Web Audio Sound Synthesizer
    const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    function playSound(isCorrect) {{
      if (!audioCtx) return;
      if (audioCtx.state === 'suspended') audioCtx.resume();
      const osc = audioCtx.createOscillator();
      const gain = audioCtx.createGain();
      osc.connect(gain);
      gain.connect(audioCtx.destination);

      if (isCorrect) {{
        osc.type = 'triangle';
        osc.frequency.setValueAtTime(523.25, audioCtx.currentTime);
        osc.frequency.setValueAtTime(659.25, audioCtx.currentTime + 0.1);
        osc.frequency.setValueAtTime(783.99, audioCtx.currentTime + 0.2);
        gain.gain.setValueAtTime(0.3, audioCtx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.45);
        osc.start();
        osc.stop(audioCtx.currentTime + 0.45);
      }} else {{
        osc.type = 'sawtooth';
        osc.frequency.setValueAtTime(240, audioCtx.currentTime);
        osc.frequency.setValueAtTime(160, audioCtx.currentTime + 0.15);
        gain.gain.setValueAtTime(0.3, audioCtx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.4);
        osc.start();
        osc.stop(audioCtx.currentTime + 0.4);
      }}
    }}

    function selectAll(val) {{
      document.querySelectorAll('.sec-check').forEach(cb => cb.checked = val);
    }}

    // Fisher-Yates shuffle
    function shuffle(arr) {{
      for (let i = arr.length - 1; i > 0; i--) {{
        const j = Math.floor(Math.random() * (i + 1));
        [arr[i], arr[j]] = [arr[j], arr[i]];
      }}
      return arr;
    }}

    function startGame() {{
      const checkedSecs = Array.from(document.querySelectorAll('.sec-check:checked')).map(cb => parseInt(cb.value));
      if (checkedSecs.length === 0) {{
        alert("¡Por favor, selecciona al menos un bloque de contenidos!");
        return;
      }}

      // Filter questions by selected sections
      let pool = masterBank.filter(q => checkedSecs.includes(q.sec));
      if (pool.length === 0) {{
        alert("No hay preguntas disponibles para los bloques seleccionados.");
        return;
      }}

      // Shuffle question pool
      pool = shuffle([...pool]);

      // Slice to selected count
      const numQ = parseInt(document.getElementById('selectNumQ').value);
      activeQuestions = pool.slice(0, Math.min(numQ, pool.length));

      // Reset state
      currentIdx = 0;
      score = 0;
      sessionResults = [];

      document.getElementById('setupScreen').style.display = 'none';
      document.getElementById('resultsScreen').style.display = 'none';
      document.getElementById('gameScreen').style.display = 'block';

      renderCurrentQuestion();
    }}

    function renderCurrentQuestion() {{
      answered = false;
      const q = activeQuestions[currentIdx];

      document.getElementById('qCounter').textContent = `Pregunta ${{currentIdx + 1}} de ${{activeQuestions.length}}`;
      document.getElementById('scoreBadge').textContent = `${{score}} pts`;
      document.getElementById('qCategory').textContent = q.cat;
      document.getElementById('qText').textContent = q.q;

      // Handle image
      const imgWrap = document.getElementById('qImgWrap');
      const imgElem = document.getElementById('qImg');
      if (q.img && imgData[q.img]) {{
        imgElem.src = imgData[q.img];
        imgWrap.style.display = 'block';
      }} else {{
        imgWrap.style.display = 'none';
      }}

      // Prepare options: create array of objects to shuffle options while preserving which one is correct
      let optionsList = q.opts.map((opt, idx) => ({{
        text: opt,
        isCorrect: (idx === q.correct)
      }}));
      optionsList = shuffle(optionsList);

      // Render options to buttons
      for (let i = 0; i < 4; i++) {{
        const btn = document.querySelectorAll('.btn-ans')[i];
        btn.dataset.correct = optionsList[i].isCorrect ? "true" : "false";
        document.getElementById('optText' + i).textContent = optionsList[i].text;
        btn.style.opacity = '1';
        btn.style.pointerEvents = 'auto';
      }}

      // Reset feedback banner and next button
      const fb = document.getElementById('feedbackBanner');
      fb.style.display = 'none';
      fb.className = 'feedback-banner';
      document.getElementById('btnNext').style.display = 'none';
    }}

    function handleAnswer(btnIdx) {{
      if (answered) return;
      answered = true;

      const btn = document.querySelectorAll('.btn-ans')[btnIdx];
      const isRight = (btn.dataset.correct === "true");
      const q = activeQuestions[currentIdx];
      const fb = document.getElementById('feedbackBanner');

      document.querySelectorAll('.btn-ans').forEach(b => b.style.pointerEvents = 'none');

      sessionResults.push({{
        qText: q.q,
        isRight: isRight,
        correctText: q.opts[q.correct]
      }});

      if (isRight) {{
        score += 100;
        document.getElementById('scoreBadge').textContent = `${{score}} pts`;
        fb.className = 'feedback-banner correct';
        fb.innerHTML = `🎉 <strong>¡CORRECTO! ¡Excelente trabajo!</strong><br>${{q.expl}}`;
        playSound(true);
      }} else {{
        fb.className = 'feedback-banner incorrect';
        fb.innerHTML = `❌ <strong>INCORRECTO.</strong> La respuesta correcta era: <strong>${{q.opts[q.correct]}}</strong>.<br>${{q.expl}}`;
        playSound(false);
      }}

      fb.style.display = 'block';
      document.getElementById('btnNext').style.display = 'inline-block';
    }}

    function nextQuestion() {{
      currentIdx++;
      if (currentIdx < activeQuestions.length) {{
        renderCurrentQuestion();
      }} else {{
        showFinalResults();
      }}
    }}

    function showFinalResults() {{
      document.getElementById('gameScreen').style.display = 'none';
      const resScreen = document.getElementById('resultsScreen');
      resScreen.style.display = 'block';

      const maxScore = activeQuestions.length * 100;
      document.getElementById('finalScoreText').textContent = `${{score}} / ${{maxScore}} pts`;

      const desc = document.getElementById('resultsFeedback');
      const correctCount = score / 100;
      const pct = (score / maxScore) * 100;

      if (pct === 100) {{
        desc.textContent = "🌟 ¡PERFECTO, BLANCA! ¡100% de aciertos! Tienes un dominio total de este bloque.";
      }} else if (pct >= 80) {{
        desc.textContent = `👏 ¡SOBRESALIENTE! Has acertado ${{correctCount}} de ${{activeQuestions.length}} preguntas. Repasa abajo las pocas que hayas fallado.`;
      }} else if (pct >= 60) {{
        desc.textContent = `👍 ¡BIEN JUGADO! Has conseguido un ${{Math.round(pct)}}%. Revisa el esquema de los puntos errados para afianzarlos.`;
      }} else {{
        desc.textContent = `💪 ¡Buen esfuerzo! Has acertado ${{correctCount}} de ${{activeQuestions.length}}. Te sugerimos repasar la guía antes de volver a intentarlo.`;
      }}

      // Build review list
      const listElem = document.getElementById('reviewList');
      listElem.innerHTML = '<div style="font-weight:700; margin-bottom:0.6rem; color:#ffd700;">Desglose de tus respuestas:</div>';
      sessionResults.forEach((r, idx) => {{
        const div = document.createElement('div');
        div.className = 'review-item';
        div.innerHTML = `
          <div><strong>${{idx + 1}}. ${{r.qText}}</strong></div>
          <div style="color: ${{r.isRight ? '#4ade80' : '#f87171'}}; margin-top:2px;">
            ${{r.isRight ? '✅ Correcto (+100 pts)' : '❌ Incorrecto. Correcta: ' + r.correctText}}
          </div>
        `;
        listElem.appendChild(div);
      }});
    }}

    function restartToSetup() {{
      document.getElementById('resultsScreen').style.display = 'none';
      document.getElementById('setupScreen').style.display = 'block';
    }}
  </script>
</body>
</html>
"""

with open("Kahoot_Tema_2_La_Celula.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Kahoot interactivo dinámico generado con éxito.")
