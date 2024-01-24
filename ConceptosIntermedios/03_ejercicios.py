
# Ejercicios 1

'''
Escribe un programa que muestre por consola los números de 1 a 100 (ambos incluidos y con un salto de línea entre cada impresión), sustituyendo los siguientes:
* Múltiplos de 3 por la palabra 'fizz'
* Múltiplos de 5 por la palabra 'buzz'
* Múltiplos de 3 y 5 por la palabra 'fizzbuzz'
'''

# ejemplo 1

def multiplo (numero):
    tres = numero % 3
    cinco = numero % 5
    if tres == 0 and cinco == 0:
        return 'fizzbuzz'
    elif tres == 0:
        return 'fizz'
    elif cinco == 0:
        return 'buzz'
    else:
        return numero

i = 1
while i < 101:
    print(multiplo(i), '\n')
    i += 1

# ejemplo 2  "FIZZ BUZZ"
    
def con_for():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print('fizzbuzz')
        elif i%5 == 0:
            print('buzz')
        elif i%3 == 0:
            print('fizz')
        else: 
            print(i)   

con_for()
    
# Ejercicios 2 "ANAGRAMA"

'''
Escribe una función que reciba dos palabras (string) y retorne verdadero o falso (bool) según sean o no anagramas.
* Un Anagrama consiste en formar una palabra reordenando todas las letras de otra palabra inicial.
* No hace falta comprobar que ambas palabras existan.
* Dos palabras exactamente iguales no son anagrama
'''

# ejemplo 1


def anagrama(texto_uno, texto_dos):
    if texto_dos.lower() == texto_uno.lower(): 
        return False
    else: 
        for i in texto_uno.lower():
            if (texto_dos.lower()).count(i) == 0:
                return False
    return True

print(anagrama('Amor', 'amor'))

# ejemplo 2

def anagrama_dos(texto_uno, texto_dos):
    if texto_uno.lower() == texto_dos.lower():
        return False
    return sorted(texto_uno.lower()) == sorted(texto_dos.lower())
    
print(anagrama_dos('amor', 'amor'))

# ejercicio 3 Sucesión de Fibonacci

'''
Escribe un programa que imprima los 50 primeros números de la sucesión de Fibonacci empezando en 0
* La serie Fibonacci se compone por una sucesión de números en la que el siguiente siempre es la suma de los dos anteriores.
0, 1, 2, 3, 5, 8, 13, ...
'''
def fibonacci():
    previo = 0
    proximo = 1
    for i in range(0,9):
        print(previo)
        fivo = previo + proximo
        previo = proximo
        proximo = fivo

fibonacci()

# ejercicio 4 Número primo

'''
Escribe un programa que se encargue de comprobar si un número es o no primo. Hecho esto, imprime los números primos entre 1 y 100
'''

def es_primo():
    for numero in range(1, 101):
        if numero >= 2:
            es_divisible = False       
            for i in range(2, numero):
                if numero % i == 0:
                   es_divisible = True
                   break
            if not es_divisible:
                print(numero)
es_primo()

# ejercicio 5 Invertir una cadena de texto

'''
Crea un programa que invierta el orden de una cadena de texto sin usar funciones propias del lenguaje que lo hagan de forma automática.
* Si le pasamos 'Hola mundo?' nos retornaría 'odnum aloh'
'''

def invertir_texto (texto):
    longitud_texto = len(texto)
    texto_inverso = ''
    for i in range(0, longitud_texto):
        texto_inverso += texto[longitud_texto - i - 1]
        
    return texto_inverso

print(invertir_texto('hola mundo'))