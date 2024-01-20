
# Listas

# una lista es una estructura, es algo diferente a un array ya que admite un para de operaciones más, tiene más flexibilidad que un array. Un superconjunto de un array
# es como una caja que le vamos a ir ingresando elementos -> el primero en posición 0, 2° en posición 1, etc.
# es una forma de agrupar datos

mi_lista = list() # definimos una lista
mi_otra_lista = []

print(len(mi_lista))

mi_lista = [12, 582, 69, 87, 36, 36, 25, 81]
print(mi_lista)
print(len(mi_lista))



mi_otra_lista = [20, 2.45, 'Pepe', 'Tito']
print(mi_otra_lista)

print(type(mi_lista))
print(type(mi_otra_lista))

print(mi_lista[6]) # accedo al valor de la posición 6

print(mi_otra_lista[0])
print(mi_otra_lista[-1])
print(mi_otra_lista[-3])
# print(mi_otra_lista[-5]) IndexError -> el índice no existe
# print(mi_otra_lista[4]) IndexError -> el índice no existe

edad, altura, nombre, apellido = mi_otra_lista # requiere la misma cantidad de variables que de elementos
print(edad)

print(mi_lista + mi_otra_lista) # concatena las dos listas

mi_otra_lista.append('constructor') # agrega el elemento 'constructor' a la lista en la última posición
print(mi_otra_lista)

mi_otra_lista.insert(1, 'Rojo') # ingresa en la posición 1 el elemento 'Azul'
print(mi_otra_lista)

mi_otra_lista[1] = 'Azul' # se le asigna el valor Azul a la posición 1.
print(mi_otra_lista)

mi_otra_lista.remove('Azul') # elimina el elemento Azul (por elemento)
print(mi_otra_lista)

del mi_otra_lista[2] # elimina el elemento de la posición 2 (por posición)

mi_lista.remove(36) # elimina un el primer elemento 36
print(mi_lista)

print(mi_lista.pop()) # saca el último elemento de la lista
print(mi_lista.pop(2)) # desapila el elemento de la posición 2+

mi_lista_pop = mi_lista.pop() # saca el último elemento y lo guardo en la variable mi_lista_pop
print(mi_lista_pop)

mi_lista_copia = mi_lista.copy() # copia el contenido de mi_lista y lo guarda en mi_lista_copia

print(mi_lista)
mi_lista.clear() # limpia por completo la lista mi_lista

print(mi_lista)
print(mi_lista_copia)

mi_lista_copia.reverse() # invierte los elemento de la lista
print(mi_lista_copia)

mi_lista_copia.sort() # por defecto ordena la lista de menor a mayor
print(mi_lista_copia)

print(mi_lista_copia[0:3]) # mostrará los elemento de la lista del elemento de la posición 0 al elemento anterior a la posición 3

mi_lista_copia.sort(reverse=True) # ordena la lista de mayor a menor

mi_lista_copia_dos = ['truco', 'América', 'te', 'empanada']
mi_lista_copia_dos.sort(key=len) # la key acepta una función que utiliza como clave para la comparación y así el ordenamiento, en este caso usa la longitud del elemento, por lo que va a ordenar los elemento más cortos a los elemento más largos
print(mi_lista_copia_dos)
print(mi_lista_copia_dos.index('te')) # da el índice donde se encuentra el elemento, en este caso va a dar 0 ya que la lista ya está ordenada
