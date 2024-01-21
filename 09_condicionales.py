
# Condicionales

mi_condicion = False

if mi_condicion:  # si mi_condicion es verdadera hace lo que está en la indentación
    print('se ejecutó la condición')
print('la ejecución continúa')

mi_condicion = 5 * 2
if mi_condicion: # acá da verdadero porque hay algo en la variable
    print('se ejecuta la condición del segundo if')

if mi_condicion > 10: # si la condición es mayor que 10 realiza lo siguiente
    print('la variable es mayor que 10')
else: # sino realiza esto ->
    print('la variable es menor o igual de 10')

if mi_condicion > 10 and mi_condicion < 20: # la condición debe cumplir que la variables sea mayor que 10 Y menor que 20
    print('la variable es mayor que 10')
else:
    print('la variable es menor de 10 o mayor de 20')

if mi_condicion > 10 and mi_condicion < 20:
    print('la variable es mayor que 10')
elif mi_condicion == 1: # sino, si la variable es igual a 1 realizar lo siguiente
    print('la variable es igual que uno')
else:
    print('la variable es menor de 10 o mayor de 20')

print('la ejecución continúa')

mi_string = ''

if not mi_string:
    print('entré porque mi cadena está vacía')
else:
    print('mi cadena no está vacía')