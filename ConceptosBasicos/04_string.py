
# Strings 

un_string = "una forma de string"
otro_string = "otra forma de string"

print(len(un_string))
print(len(otro_string))

print(un_string + ' - ' + otro_string)

nuevo_string = 'Este es un string\ncon un salto de línea' # caracteres especiale \n salto de línea
print(nuevo_string)

nuevo_string_tabulacion = '\tEste es un string con una tabulación inicial' # caracteres especiale \t tabulación
print(nuevo_string_tabulacion)

nuevo_string_escape = '\tUn texto con tabulación\ntexto con escape'
print(nuevo_string_escape)

# Formateo

# esta es la mejor manera de imprimir una cadena de texto con variables 
nombre, apellido, edad = 'Pepe', 'Tito', 58
print('mi nombre es {} {} y mi edad es {}'.format(nombre, apellido, edad))
print('mi nombre es %s %s y mi edad es %d' %(nombre, apellido, edad))
print(f'mi nombre es {nombre} {apellido} y mi edad es {edad}') # inferencia de datos. la f es de formatear el texto y se infiere los datos entre{} 

# Desempaquetado de caracteres

lenguaje = 'python'
a, b, c, d, e, f = lenguaje # requiere la misma cantidad de variable que de elementos
print(a, e, c)

# División 

lenguaje_slice = lenguaje[1:4] # va a seleccionar desde la posición 1(incluido) hasta la 4(no incluido)
print(lenguaje_slice)

lenguaje_slice = lenguaje[1:] # va a seleccionar desde la posición 1(incluido) hasta el final
print(lenguaje_slice)

lenguaje_slice = lenguaje[-2] # va a mostrar la segunda posición de atrás para adelante en este caso la "o"
print(lenguaje_slice)
print()
lenguaje_slice = lenguaje[0:6:3] # va a mostrar pto 0:6 agarra todo y :2 muestra cada dos elementos
print(lenguaje_slice)

# Reverse

rever_variable = lenguaje[::-1] # da vuelta la cadena de texto
print(rever_variable)

# Funciones
print()
print(lenguaje.capitalize()) # la primer palabra la colocará en mayúsculas
print(lenguaje.upper()) # pone todas las letras en mayúsculas
print(lenguaje.count('t')) # cuenta la cantidad de veces que se repite lo que se le coloca en ()
print(lenguaje.isnumeric()) # pregunta si es un número
print('1'.isnumeric()) # pregunta si es un número
print(lenguaje.lower()) # pone todo en minúsculas
print(lenguaje.upper().isupper()) # pone todo en mayúsculas y pregunta si está en mayúsculas
print(lenguaje.startswith('Py')) # comprueba si el string empieza con lo que se pone entre (), distingue mayúsculas y minúsculas

print(sorted(lenguaje)) # hace una lista, separa las letras y las ordena alfabeticamente.
