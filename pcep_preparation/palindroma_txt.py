def is_palindrome(word):
  """Verifica se una parola è un palindromo.

  Args:
    word: La parola da controllare.

  Returns:
    True se la parola è un palindromo, False altrimenti.
  """
  return word == word[::-1]

def find_palindromes(file_path):
  """Trova tutte le palindromi in un file .txt.

  Args:
    file_path: Il percorso del file .txt.

  Returns:
    Una lista contenente tutte le palindromi trovate.
  """
  
  palindromes = []
  with open(file_path, 'r') as file:
    for line in file:
      words = line.split()
      for word in words:
        if len(word) > 3 and is_palindrome(word):
          palindromes.append(word)
  return palindromes

# Esempio d'uso:
file_path = "mio_file.txt"  # Sostituisci con il percorso del tuo file
result = find_palindromes(file_path)
print(result)
