def is_palindrome(word):
  """Verifica se una parola è un palindromo.

  Args:
    word: La parola da controllare.

  Returns:
    True se la parola è un palindromo, False altrimenti.
  """
  return word == word[::-1]
