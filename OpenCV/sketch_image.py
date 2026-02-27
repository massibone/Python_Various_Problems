import cv2

# Caricamento dell'immagine
image = cv2.imread('foto_mia.png')

# Controllo se l'immagine è stata caricata correttamente
if image is None:
    print("Errore: Impossibile caricare l'immagine. Controlla il percorso.")
else:
    # Conversione in scala di grigi
    grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Inversione dell'immagine grigia
    invert = cv2.bitwise_not(grey_img)
    
    # Sfocatura Gaussiana (Blur)
    blur = cv2.GaussianBlur(invert, (31, 31), 0)
    
    # Creazione dello sketch (Divisione tra grigio e sfocatura invertita)
    # Nota: Usiamo 255 - blur direttamente per risparmiare un passaggio
    sketch = cv2.divide(grey_img, 255 - blur, scale=256.0)
    
    # Salvataggio del risultato
    cv2.imwrite('sketch.png', sketch)
    print("Sketch salvato con successo come 'sketch.png'")

