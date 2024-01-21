
# dicts

# es una estructura clave-valor, como el objeto en JS, o un JSON

mi_dict = dict()
mi_otro_dict = {}

print(type(mi_dict))
print(type(mi_otro_dict))

mi_otro_dict = { 'nombre': 'Pepe', 'apellido': 'Tito', 'edad': 59, 1: 'Python' }
print(mi_otro_dict)

mi_dict = {
    'nombre': 'Pepe', 
    'apellido': 'Tito', 
    'edad': 59, 
    'lenguajes': {'Python', 'Swift', 'Kotlin'},
    1: 1.89
}

print()
print(mi_otro_dict)
print(mi_dict)
print(len(mi_otro_dict)) # mostrará 4, que son la cantidad de claves-valor que hay, no importa si el valor de alguna clave tiene más de un valor
print(len(mi_dict))
print()
print(mi_dict['nombre']) # imprime el valor de la clave que colocamos entre []

mi_dict['nombre'] = 'Chacho' # cambia el valor de la clave nombre, a Chacho
print(mi_dict['nombre'])

print()
print(mi_dict[1])

mi_dict['calle'] = 'calle Tito' # agrega una nueva clave-valor, calle: 'calle Tito'
print(mi_dict)

del mi_dict['calle'] # elimina la clave-valor, con la clave igual a calle
print(mi_dict)

print('Pepe' in mi_dict) # esto da false, ya que está buscando en las claves
print('nombre' in mi_dict) # esto da true, ya que hay una clave denominada nombre

print()

print(mi_dict.items()) # nos brinda el listado de lo que tiene el diccionario, en forma de lista
print(mi_dict.keys()) # nos da todas las claves que tiene el diccionario, en forma de lista
print(mi_dict.values()) # nos da todos los valores que tiene el diccionario, en forma de lista

mi_nuevo_dict = dict.fromkeys(mi_dict) # creará un nuevo diccionario con todas las claves que tiene el diccionario que se le coloca entre (), en este caso mi_dict
print(mi_nuevo_dict)

# mi_nuevo_dict = dict.fromkeys(mi_dict, ('Kiko', 'Coco')) # en este caso le va a asignar ('Kiko', 'Coco') en todas las claves
print()

print( list(mi_otro_dict)) # un diccionario se puede transformar en una lista, almacenando todas las claves 
print(tuple(mi_otro_dict)) # un diccionario se puede transformar en una tupla, almacenando todas las claves 
print(set(mi_otro_dict)) # un diccionario se puede transformar en un set, almacenando todas las claves 
# print(dict(list(mi_otro_dict))) # pero una lista no puede convertirse en un diccionario
# print(pruebau)

print(list(dict.fromkeys(list(mi_otro_dict.values())).keys()))