import string

def is_palindrome(word):
  """Verifica se una parola è un palindromo, ignorando punteggiatura e maiuscole/minuscole."""
  word = word.lower()
  word = word.translate(str.maketrans('', '', string.punctuation))
  return word == word[::-1]

def find_palindromes(file_path, min_length=3, output_file=None):
  """Trova tutte le palindromi in un file .txt.

  Args:
    file_path: Il percorso del file .txt.
    min_length: La lunghezza minima delle parole da considerare.
    output_file: Il percorso del file di output (opzionale).

  Returns:
    Una lista contenente tutte le palindromi trovate.
  """

  palindromes = []
  with open(file_path, 'r') as file:
    for line in file:
      words = line.split()
      for word in words:
        if len(word) >= min_length and is_palindrome(word):
          palindromes.append(word)

  if output_file:
    with open(output_file, 'w') as output:
      for palindrome in palindromes:
        output.write(palindrome + '\n')

  return palindromes
