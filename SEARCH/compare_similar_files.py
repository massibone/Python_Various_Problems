import os



def compare_similar_files(directory):
    """Confronta file con nomi simili all'interno di una directory"""
    similar_files = []
    filenames = os.listdir(directory)
    for filename in filenames:
        base_name, ext = os.path.splitext(filename)
        pair_name = base_name + '_pair' + ext
        pair_path = os.path.join(directory, pair_name)
        if pair_name in filenames:
            similar_files.append((filename, pair_name))
    return similar_files

# Esempio di utilizzo

directory_path = '/percorso/alla/cartella'
similar_files = compare_similar_files(directory_path)

# Stampa dei file con nomi simili
for file1, file2 in similar_files:
    print(f"I file {file1} e {file2} hanno nomi simili.")
