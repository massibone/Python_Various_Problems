'''
I namespaces in Python sono effettivamente simili a dizionari, 
ma con alcune differenze importanti. Un namespace è un insieme di nomi che sono associati a oggetti, come variabili, funzioni, classi, ecc. Si possono utilizzare i namespaces per esporre solo le funzioni e le variabili che si desidera rendere pubbliche, mentre si tengono private le altre.
'''
#Supponiamo di avere un modulo chiamato math_utils.py che contiene diverse funzioni matematiche:
# math_utils.py

def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

def multiply(x, y):
  return x * y

def divide(x, y):
  if y == 0:
    raise ValueError("Divisione per zero!")
    return x / y
def _private_function(x):
# Questa funzione non dovrebbe essere utilizzata dall'esterno
  return x * 2
# math_utils.py

__all__ = ['add', 'subtract', 'multiply', 'divide']

def add(x, y):
  return x + y

def subtract(x, y):
  return x - y
def multiply(x, y):
return x * y

def divide(x, y):
if y == 0:
raise ValueError("Divisione per zero!")
return x / y

def _private_function(x):
# Questa funzione non dovrebbe essere utilizzata dall'esterno
return x * 2
'''
n questo esempio, il namespace __all__ contiene solo i nomi delle funzioni pubbliche. Quando si importa il modulo math_utils, solo queste funzioni saranno disponibili:

>>> from math_utils import *
>>> add(2, 3)
5
>>> subtract(4, 2)
2
>>> multiply(5, 6)
30
>>> divide(10, 2)
5.0
>>> _private_function(2)
NameError: name '_private_function' is not defined
'''
