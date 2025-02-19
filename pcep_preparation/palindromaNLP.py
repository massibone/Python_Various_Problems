import string

def is_palindrome(word):
  """Verifica se una parola è un palindromo, ignorando punteggiatura e maiuscole/minuscole."""
  word = word.lower()
  word = word.translate(str.maketrans('', '', string.punctuation))
  return word == word[::-1]

