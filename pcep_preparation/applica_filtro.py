'''
Applica filtri a immagini di grandi dimensioni. Un filtro comune è un filtro di convoluzione, 
che coinvolge la moltiplicazione di una matrice di filtri con una matrice di pixel.

Matrici di grandi dimensioni: 
Le immagini ad alta risoluzione possono avere milioni di pixel, 
e le matrici di filtri possono essere di dimensioni considerevoli (ad esempio, 100x100).
Moltiplicazioni ripetute: Il filtro viene applicato a ogni pixel dell'immagine, 
quindi le moltiplicazioni vengono eseguite milioni di volte.
'''
import numpy as np
from PIL import Image

def applica_filtro(immagine_path, filtro):
    """
    Applica un filtro di convoluzione a un'immagine.

    Args:
        immagine_path: Percorso dell'immagine.
        filtro: Matrice del filtro (NumPy array).

    Returns:
        Immagine filtrata (NumPy array).
    """
    immagine = Image.open(immagine_path).convert('L')  # Converti in scala di grigi
    immagine_array = np.array(immagine)
    filtro_dimensioni = filtro.shape[0]
    padding = filtro_dimensioni // 2
    immagine_filtrata = np.zeros_like(immagine_array)

    for i in range(padding, immagine_array.shape[0] - padding):
        for j in range(padding, immagine_array.shape[1] - padding):
            area_immagine = immagine_array[i - padding:i + padding + 1, j - padding:j + padding + 1]
            immagine_filtrata[i, j] = np.sum(area_immagine * filtro)

    return immagine_filtrata

# Esempio: filtro di sfocatura
filtro_sfocatura = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]]) / 16

# Applica il filtro
immagine_filtrata = applica_filtro('immagine.jpg', filtro_sfocatura)

# Salva l'immagine filtrata
Image.fromarray(immagine_filtrata.astype(np.uint8)).save('immagine_filtrata.jpg')
