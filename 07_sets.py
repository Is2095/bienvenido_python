
# Sets

# de base tiene un array
# un set no es una estructura ordenada
# un set no admite repetidos

mi_set = set()
mi_otro_set = {} # definido así, inicialmente apararece como tipo: diccionario

print(type(mi_set))
print(type(mi_otro_set)) # inicialmente marca que su tipo es un diccionario

mi_otro_set = {'Pepe', 'Tito', 58} # al ingresar los datos queda claro que es de tipo set
print(type(mi_otro_set)) 

print(len(mi_otro_set)) # imprime su longitud = 3

mi_otro_set.add('carpintero')
print(mi_otro_set) # un set no es una estructura ordenada. Es decir no tiene una posición fija

mi_otro_set.add('carpintero')
print(mi_otro_set) # un set no admite elementos repetidos

print('Pepe' in mi_otro_set) # comprueba si el elemento Pepe está dentro de mi_otro_set
print('Pape' in mi_otro_set) # comprueba si el elemento Pape está dentro de mi_otro_set

mi_otro_set.remove('carpintero') # remueve el elemento carpintero del set mi_otro_set
print(mi_otro_set) 

mi_otro_set.clear() # elimina todos los elementos del set, limpia el set
print(mi_otro_set)
print(type(mi_otro_set))
print(len(mi_otro_set))

del mi_otro_set # elimina el set mi_otro_set por completo
# print(mi_otro_set) NameError: name my_otro_set is not defined

mi_set = {'Pepe', 'Tito', 58}
mi_lista = list(mi_set) # no se debería usar ya que no sabremos las posiciones de cada elemento
print(mi_lista)

mi_otro_set = {'Kotlin', 'Swift', 'Python'}
mi_nuevo_set = mi_set.union(mi_otro_set) # une en una nueva variable, el set mi_set y mi_otro_set
print(mi_nuevo_set)

print(mi_nuevo_set.union(mi_nuevo_set).union(mi_set).union({'JavaScript', 'C#'})) # los dos primeros union los descarta ya que los elementos ya están y no admite repetidos, el tercer union si lo hace

print(mi_nuevo_set.difference(mi_set)) # muestra la diferencia que hay entre de mi_nuevo_set y mi_set, acá no aparecerá JS ni C# ya que fueron puestos sólo para la operación print, y no quedó dentro de la variable.
