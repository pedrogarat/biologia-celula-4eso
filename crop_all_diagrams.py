from PIL import Image

def crop_box(img_path, box, out_path):
    im = Image.open(img_path)
    w, h = im.size
    crop_area = (int(w * box[0]), int(h * box[1]), int(w * box[2]), int(h * box[3]))
    cropped = im.crop(crop_area)
    cropped.save(out_path)
    print(f"Saved {out_path}: {cropped.size}")

# Page 3 (p.12): Membrana plasmática
# Membrane 3D diagram at the bottom
crop_box("fotos/page_03.jpg", (0.04, 0.72, 0.94, 0.94), "fotos/membrana_mosaico_fluido.png")

# Page 4 (p.13): Transporte y Pared celular
# Small substance transport (left)
crop_box("fotos/page_04.jpg", (0.04, 0.13, 0.47, 0.35), "fotos/transporte_membrana.png")
# Endocytosis & Exocytosis (right)
crop_box("fotos/page_04.jpg", (0.49, 0.15, 0.93, 0.35), "fotos/endocitosis_exocitosis.png")
# Cell wall potato micrograph (bottom left/center)
crop_box("fotos/page_04.jpg", (0.03, 0.75, 0.62, 0.97), "fotos/pared_celular_microscopio.png")

# Page 5 (p.14): Citoesqueleto
# Cytoskeleton 3D diagram (bottom left)
crop_box("fotos/page_05.jpg", (0.05, 0.67, 0.65, 0.94), "fotos/citoesqueleto_diagrama.png")
# Cytoskeleton micrograph (bottom right)
crop_box("fotos/page_05.jpg", (0.66, 0.67, 0.97, 0.88), "fotos/citoesqueleto_micrografia.png")

# Page 6 (p.15): Retículo y Golgi
# ER diagram
crop_box("fotos/page_06.jpg", (0.10, 0.36, 0.63, 0.54), "fotos/reticulo_endoplasmatico.png")
# ER micrograph
crop_box("fotos/page_06.jpg", (0.64, 0.34, 0.92, 0.49), "fotos/reticulo_micrografia.png")
# Golgi diagram
crop_box("fotos/page_06.jpg", (0.45, 0.74, 0.96, 0.90), "fotos/golgi_diagrama.png")
# Golgi micrograph
crop_box("fotos/page_06.jpg", (0.68, 0.55, 0.95, 0.70), "fotos/golgi_micrografia.png")

# Page 7 (p.16): Lisosomas y Mitocondria
# Lysosomes micrograph
crop_box("fotos/page_07.jpg", (0.38, 0.08, 0.64, 0.22), "fotos/lisosomas_micrografia.png")
# Mitochondria diagram
crop_box("fotos/page_07.jpg", (0.05, 0.75, 0.61, 0.94), "fotos/mitocondria_diagrama.png")
# Mitochondria micrograph
crop_box("fotos/page_07.jpg", (0.62, 0.75, 0.95, 0.94), "fotos/mitocondria_micrografia.png")

# Page 8 (p.17): Cloroplasto y Teoría Endosimbiótica
# Chloroplast diagram
crop_box("fotos/page_08.jpg", (0.05, 0.44, 0.56, 0.60), "fotos/cloroplasto_diagrama.png")
# Chloroplast micrograph
crop_box("fotos/page_08.jpg", (0.57, 0.44, 0.91, 0.57), "fotos/cloroplasto_micrografia.png")
# Endosymbiotic theory diagram
crop_box("fotos/page_08.jpg", (0.54, 0.64, 0.95, 0.92), "fotos/teoria_endosimbiotica.png")

# Page 9 (p.18): Ribosomas y Centrosoma
# Ribosome diagram
crop_box("fotos/page_09.jpg", (0.43, 0.09, 0.65, 0.23), "fotos/ribosoma_diagrama.png")
# Ribosomes micrograph
crop_box("fotos/page_09.jpg", (0.69, 0.07, 0.99, 0.22), "fotos/ribosomas_micrografia.png")
# Centrosome diagram
crop_box("fotos/page_09.jpg", (0.08, 0.40, 0.62, 0.64), "fotos/centrosoma_diagrama.png")
# Centrosome micrograph
crop_box("fotos/page_09.jpg", (0.69, 0.40, 0.99, 0.67), "fotos/centriolos_micrografia.png")

print("All diagrams cropped successfully!")
