import cv2

# Percorso immagine (modifica se necessario)
img_path = 'Images/your_image.jpg'  # sostituisci con il tuo file

# Nuove dimensioni: puoi impostare width, height oppure scale (fattore)
# Opzione A: dimensioni esplicite (px)
new_width = 800
new_height = 600

# Opzione B: fattore di scala (es. 0.5 = 50%)
# scale_factor = 0.5

# Carica immagine
img = cv2.imread(img_path)
if img is None:
    print(f"Error: Unable to read image '{img_path}'.")
else:
    # Ridimensiona usando dimensioni esplicite
    resized = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_AREA)

    # Se preferisci usare il fattore di scala, usa invece:
    # resized = cv2.resize(img, (0, 0), fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_AREA)

    # Salva immagine ridimensionata (opzionale)
    out_path = 'Images/your_image_resized.jpg'
    cv2.imwrite(out_path, resized)
    print(f"Resized image saved to '{out_path}'")

    # Mostra immagine ridimensionata
    cv2.imshow('Resized Image', resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
