# Tuples

# es un conjunto de valores, solo admite count y index, los datos de la tupla es inmutable, no se puede cambiar

mi_tupla = tuple()
mi_otra_tupla = ()

mi_otra_tupla = (35, 65, 494, 99329)
mi_tupla = (39, 1.55, 'Pepe', 'Tito', 'probando')
print(mi_tupla)
print(type(mi_tupla))

print(mi_tupla[0])
print(mi_tupla[-1])
# print(mi_tupla[4]) IndexError
# print(mi_tupla[-6]) IndexError
print(mi_tupla.count(39)) # da la cantidad de veces que se repite el dato entre ()
print(mi_tupla.index('Pepe')) # da el índice donde se encuentra el dato puesto en ()

# mi_tupla[1] = 1.3 error: tuple object does not support item assignment

suma_tuplas = mi_tupla + mi_otra_tupla # las tuplas entre sí se puede sumar
print(suma_tuplas)

print(suma_tuplas[2: 6]) # muestra los datos comprendidos entre la posición 2 y la anterior a la posición 6

# si en el caso necesitamos modificar la tupla

mi_tupla = list(mi_tupla)
print(type(mi_tupla))
mi_tupla[4] = 'carpintero'
mi_tupla.insert(1, 'Azul')
print(mi_tupla)
mi_tupla = tuple(mi_tupla)
print(tuple(mi_tupla))
print(type(mi_tupla))

# del mi_tupla[1] TypeError: tuple object doesn't support item deletion 
del mi_tupla # borra por completo la tupla
# print(mi_tupla) por lo que esta orden da error ya que mi_tupla no existe

