
from functools import reduce

# Funciones de orden superior

# Básicamente son funciones que llaman funciones

def suma_uno(valor):
    return valor + 1
def suma_cinco(valor):
    return valor + 5

def suma_dos_valores_y_suma_uno(primer_valor, segundo_valor):
    return suma_uno(primer_valor + segundo_valor)

print(suma_dos_valores_y_suma_uno(7, 3))

def suma_dos_valores_y_suma_uno(primer_valor, segundo_valor, funcion_suma_uno): # acá la función se recibe como parámetro, enviada desde la llamada de la función
    return funcion_suma_uno(primer_valor + segundo_valor) # por lo que nos permite pasar cualquier función y la función la va a ejecutar dentro de sí, 

print(suma_dos_valores_y_suma_uno(7, 3, suma_uno)) # acá llamamos a la misma función enviando como parámetro dos funciones diferentes, por lo que con la misma llamada a la función, tendremos resultados diferentes dependiendo de la función que enviamos como parámetro
print(suma_dos_valores_y_suma_uno(7, 3, suma_cinco))
print()

# Closures ----> es una función que define una función y retorna una función

def sumar_diez(valor_función):
    def sumar(value):
        return value + 10 + valor_función
    return sumar

sumar_closures = sumar_diez(3)
print(sumar_closures(5))

print(sumar_diez(5)(2))

# Built-in -- funciones de orden superior del sistema

numeros = [2, 5, 32, 54, 1, 78]

# Map ----> va mapeando una lista y en cada elemento se llamará a la función (parámetro)

def multiplicar_dos(numero):
    return numero * 2

print(list(map(multiplicar_dos, numeros))) # resultado [4, 10, 64, 108]
print(list(map(lambda numero: numero * 2, numeros)))

# filter

def filtrado_valor(numero):
    if numero > 10:
        return True
    return False

print(list(filter(filtrado_valor,numeros))) # va a ir iterando cada elemento de la lista y cada elemento lo filtrará según la función (parámetro), quedan todos los elementos que pasaron true en la función de filtrado
print(list(filter(lambda numero: numero > 10, numeros)))

# Reduce

def suma_dos_valores(primer_valor, segundo_valor):
    return primer_valor + segundo_valor

print(reduce(suma_dos_valores, numeros)) # reduce va a reducir todos los valores numéricos de una lista, según lo indique la función que se llama (parámetro)