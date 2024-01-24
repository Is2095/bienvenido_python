
# Tipos de errores

# SyntaxError

# print 'hola gente' # SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
print('hola gente')
# ---------------------------------------------------------------------

# NameError

nombre = 'Pepe' # comentar para ver el error
print(nombre) # NameError: name 'nombre' is not defined
# ---------------------------------------------------------------------

# IndexError

mi_lista = ['Python', 'Swift', 'Kotlin', 'Dart', 'JavaScript']

print(mi_lista[0])
print(mi_lista[4])
print(mi_lista[-1])
# print(mi_lista[5]) # IndexError: list index out of range
# ---------------------------------------------------------------------

# ModuleNotFoundError

# import maths # ModuleNotFoundError: No module named 'maths'
import math
# ---------------------------------------------------------------------

# AttributeError

# print(math.pe) # AttributeError: module 'math' has no attribute 'pe'. Did you mean: 'e'?
print(math.pi)
# ---------------------------------------------------------------------

# KeyError

mi_otro_dict = { 'nombre': 'Pepe', 'apellido': 'Tito', 'edad': 59, 1: 'Python' }
print(mi_otro_dict['edad'])
# print(mi_otro_dict['nommbre']) # KeyError: 'nommbre'
print(mi_otro_dict['apellido'])

#TypeError

# print(mi_lista['0']) # TypeError: list indices must be integers or slices, not str
print(mi_lista[0])
# ---------------------------------------------------------------------

# ImportError

# from math import pe # ImportError: cannot import name 'pe' from 'math' (unknown location). Did you mean: 'e'?
from math import pi
print(pi)
# ---------------------------------------------------------------------

# ValueError

mi_entero = int('10')
# mi_entero = int('10 Años') # ValueError: invalid literal for int() with base 10: '10 Años'
print(mi_entero)
# ---------------------------------------------------------------------

# ZeroDivisionError
# print(3/0) # ZeroDivisionError: division by zero
print(3/2)
