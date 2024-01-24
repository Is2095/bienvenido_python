
# REGex - Expresiones Regulares

# inspeccionan una cadena de texto

import re

# match

mi_string = 'Esta es la lección número 3: lección 25 de Expresiones Regulares ='
mi_otra_string = 'Esta no es la lección número 14: Manejo de ficheros'

print(re.match('Esta es la lección', mi_string)) # <re.Match object; span=(0, 18), match='Esta es la lección'>
print(re.match('Esta es la lección', mi_otra_string)) # None
print(re.match('Expresiones Regulares', mi_string)) # None -> ya que empieza desde el inicio del string
print(re.match('es la lección', mi_string)) # None
print(re.match('Esta es la lección', mi_string, re.I)) # el re.I hace que no sea sensible, es decir que no diferencia mayúsculas de minúsculas

match = re.match('Es ta es la lección', mi_string)

# if not(match == None):
# if match != None:

if match is not None:
    print(match, '-')
    span = match.span()
    inicio, final = span
    print(span, inicio, final)
    print(mi_string[inicio:final])

print()

# search --> busca la primera coincidencia 

search = re.search('Lección', mi_string, re.I)
print(search)
span = search.span()
inicio, final = span
print(span, inicio, final)
print(mi_string[inicio:final])

print()

# findall --> en una lista coloca todas las veces que se encuentra

findall = re.findall('lección', mi_string, re.I)
print(findall)

print()

# split --> a través del patrón que se coloca divide al string en una lista por tantas veces aparezca ese patrón, en el siguiente caso en dos elementos

print(re.split(':', mi_string))

print()

# sub --> si encuentra la expresión (primer parámetro), la reemplaza por el segundo parámetro, del archivo ...

print(re.sub('Expresiones', 'expresiones', mi_string))
print(re.sub('[L|l]ección', 'LECCIÓN', mi_string)) # busca las palabra igual a lección Ó Lección y reemplazarla por LECCIÓN
print(re.sub('lección|Lección', 'LECCIÓN', mi_string)) # busca las palabra igual a lección Ó Lección y reemplazarla por LECCIÓN
print()

# Patrones RegEx

patron = r'[Ll]ección' # forma de hacer una expresión regular
print(re.findall(patron, mi_string))

patron = r'[Ll]ección|Expresiones' # en cuentra la palabra lección con l o L, y la palabra Expresiones
print(re.findall(patron, mi_string))

patron =r'[a-z]' # encuentra las letras de la 'a' a la 'z'
print(re.findall(patron, mi_string))
patron =r'[0-9]' # encuentra los números del 0 al 9
print(re.findall(patron, mi_string))
print(re.search(patron, mi_string))

patron =r'\d' # encuentra los decimales
print(re.findall(patron, mi_string))
patron =r'\D' # encuentra los no decimales
print(re.findall(patron, mi_string))

patron =r'[l].' # encuentra los pares de letras que empiecen con l
print(re.findall(patron, mi_string))

patron =r'[l].*' # encuentra todo lo que hay después de la primera letra l
print(re.findall(patron, mi_string))

email = 'micorreo@gmail.com.ar'
patron_email = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+$' # el +$ indica todo lo que sigue y finaliza la expresión. ^ empieza con...
print(re.findall(patron_email, email))
print(re.match(patron_email, email))
print(re.search(patron_email, email))

email = 'micorreo@gmail'
print(re.findall(patron_email, email)) # []
email = 'micorreo@gmail.'
print(re.findall(patron_email, email)) # []
email = 'micorreo@gmail.9'
print(re.findall(patron_email, email)) # []
email = 'micorreo@gmail.e'
print(re.findall(patron_email, email)) # []