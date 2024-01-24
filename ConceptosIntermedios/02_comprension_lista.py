
# Comprensión de lista

mi_lista_original = [0, 1, 2, 3, 4, 5, 6, 7] # creo una lista en forma manual
print(mi_lista_original)


mi_rango = range(8) # creamos un rango y luego creamos la lista con ese rango
print(list(mi_rango))

print(list(range(8))) # igual a la anterior reducido

mi_lista = [i for i in range(8)] # creo una lista con el bucle for-in dandole un rango de 8 (8 veces se va a repetir el for)
print(1, mi_lista)

mi_lista = [i + 1 for i in range(8)] 
print(2, mi_lista)

mi_lista = [i * 2 for i in range(8)] 
print(3, mi_lista)

mi_lista = [i * i for i in range(8)] 
print(4, mi_lista)

def sumar_cinco(numero):
    return numero + 5

mi_lista = [sumar_cinco(i) for i in range(8)] 
print(5, mi_lista)

