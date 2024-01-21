
# Funciones

# una función va a resolver un problema concreto

def mi_funcion (): # def palabra reservada para crear la función, luego va el nombre de la función más ()
    print('esto es una función')

mi_funcion () # llamada de la función mi_funcion

def suma_dos_valores (x, y): # en este caso la función recibe dos parámetros, los cuales serán usados para hacer algo
    print(x + y)

suma_dos_valores(13, 89)

def retorna_sum_dos_valores (x, y):
    return x + y # retorna el resultado de la función

valor = retorna_sum_dos_valores(18,82) # el valor de la función en guardada en una función
print(valor)

def imprime_nombre (nombre, apellido):
    print(f'{nombre} {apellido}')

imprime_nombre('Tito', 'Pepe')
imprime_nombre(nombre = 'Pepe', apellido = 'Tito') # en este caso asignamos a cada parámetro su valor, 

def imprime_nombre_con_defecto  (nombre, apellido, alias = 'sin alias'): # le da valores por defecto, es decir si no llega el valor toma el valor por defecto
    print(f'{nombre} {apellido} {alias}')

imprime_nombre_con_defecto('Pepe', 'Tito', 'el chiquito')
imprime_nombre_con_defecto('Pepe', 'Tito')

def imprime_texto (*texto): # con el aterisco le indicamos que pueden venir un número n de parámetros- función con parámetros arbitrarios
    print(texto)

imprime_texto('hola', 'mundo', 'amante', 'de', 'Python')
imprime_texto('Python')

def imprime_texto_mayuscula (*texto):
    print(type(texto)) # el tipo de *texto es una Tupla
    for ele in texto:   # con esta iteración logramos ir imprimiendo elemento por elemento que llega en el parámetro dinámico texto y lo imprime en mayúsculas
        print(ele.upper())

imprime_texto_mayuscula('hola', 'mundo', 'amante', 'de', 'Python') # al tener *texto, implica que los parámetro que enviemos separados con ,
