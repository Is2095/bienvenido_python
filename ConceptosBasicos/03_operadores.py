
# operadores aritméticos

print(3+3) #-> 6
print(3-3) #-> 0
print(3*3) #-> 9
print(3/3) #-> 1.0

print(10 % 3) #-> módulo, da el resto = 1

print (10 // 3) # flor división, el resultado siempres en un entero, aproximado

print (2 ** 3) # exponente, 2 elevado a la 3 -> 8

print('hola' + 'python') # concatena los string sin espacios
print('numero ' + str(5)) # no puede sumar tipos diferentes
print('hola ' * 5) # imprime 5 veces la palabra hola
print('hola' * (2**3)) # imprime 8 veces la palabra hola. SOLO ADMITE INT(números enteros)

# operadors comparativos

print(3 > 4) # false
print(3 < 4) # verdadero
print(3 >= 4) # F
print(3 <= 4) # V
print(3 == 4) # F
print(3 != 4) # V

print()

print('hola' > 'python') # false
print('hola' < 'python') # verdadero  -- comprueva una ordenación alfabética y distingue mayúsculas y minúsculas
print('hola' >= 'python') # F
print('hola' <= 'python') # V
print('hola' == 'hola') # V
print('hola' != 'python') # V

# Operadores lógicos

print(3 > 4 and 'hola' > 'python') # -> falso
print(3 > 4 or 'hola' > 'python') # -> falso
print(3 < 4 and 'hola' < 'python') # -> verdadero
print(3 < 4 or 'hola' > 'python') # -> verdadero
print(3 < 4 or ('hola' > 'python' and 4 == 4)) # -> verdadero Esta forma le damos la prioridad para la comparación
print(not(3 < 4)) # solo niega el resultado de lo que hay entre () -> falso
