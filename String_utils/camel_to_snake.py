import re

def camel_to_snake(name):
  # Utilizza una regex per inserire un underscore tra le lettere maiuscole e minuscole
  snake_case = re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()
  return snake_case

# Test della funzione
print(camel_to_snake("MySampleText")) # Output: "my_sample_text"

