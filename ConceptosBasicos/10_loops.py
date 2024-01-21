
# Loops

# loops = ciclos = bucles -> iterar, es pasar por un código varias veces

# While

mi_condicion = 0

while mi_condicion < 10: # mientras la condición mi_condicio < 10 se cumple realiza lo que está debajo dentado
    print(mi_condicion)
    mi_condicion += 2
else: # el while acepta poner else, cuando no se cumple la condición del while pasa por el else
    print('mi condición es mayor o igual a 10')

while mi_condicion < 20:
    mi_condicion += 1
    if mi_condicion == 15:
        print('el número es 15')
        break # cuando entra en esta condición el break detiene el while y lo salta
    print(mi_condicion)

print('la ejecución continúa')
print()

# For

mi_lista = [12, 23, 545, 5656, 73, 2232, 87, 2, 3, 90]

for ele in mi_lista: # itera la lista elemento por elemento
    print(ele)

print()
mi_tupla = (39, 1.55, 'Pepe', 'Tito', 'probando')
for ele in mi_tupla:
    print(ele)

print()
mi_set = {'Pepe', 'Tito', 58}
for ele in mi_set:
    print(ele)

print()
mi_dict = { 'nombre': 'Pepe', 'apellido': 'Tito', 'edad': 59, 1: 'Python' }
for ele in mi_dict: # en el diccionario el for itera sobre las claves
    print(ele)

print()
mi_dict = { 'nombre': 'Pepe', 'apellido': 'Tito', 'edad': 59, 1: 'Python' }
for ele in mi_dict.values(): # en este caso saca los valores
    print(ele)
else:
    print('el bucle del for terminó')

print()
mi_dict = { 'nombre': 'Pepe', 'apellido': 'Tito', 'edad': 59, 1: 'Python' }
for ele in mi_dict: # en este caso saca los valores
    print(ele)
    if ele == 'edad':
        print('llegamos a la clave edad')
        break # si llegó a éste punto salta el ciclo for, lo termina
else:
    print('el bucle del for terminó')

print()
mi_dict = { 'nombre': 'Pepe', 'apellido': 'Tito', 'edad': 59, 1: 'Python' }
for ele in mi_dict: # en este caso saca los valores
    print(ele)
    if ele == 'edad':
        print('llegamos a la clave edad')
        continue # si llegó a este punto vuelve al for, lo que hay después del continue no se ejecuta, no es muy buena práctica, lo mejor es colocar una condición
    print('ejecución después del if')
else:
    print('el bucle del for terminó')
