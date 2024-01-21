
# Manejo de errores

# print(3 + '4') # en este caso el programa se corta largando el error por consola, la idea es controlar esas fallas para que no se pare la aplicación, es decir controlar y manejar los posibles errores que pueden surgin en un código

numero_uno = 4
numero_dos = 34
numero_dos = '34'

#try except
try:
    print(numero_uno + numero_dos)
except: 
    print('se a producido un error')

#try except else
try:
    print(numero_uno + numero_dos)
except: 
    print('se a producido un error')
# lo siguiente es opcional
else: # este else se ejecutará si dentro de try a salido todo correctamente, sino se ejecuta el except
    print('la ejecución continúa correctamente')
finally: # se ejecuta siempre 
    print('la ejecución sigue normalmente')

# Captura de errores por Tipo
    
    # la idea es hacer una captura de errores personalizadas
try: 
    print(numero_uno + numero_dos)
except ValueError: # en este caso decimos que sólo capture el error si es de tipo ValueError
    print('se a producido un error de tipo ValueError')
except TypeError: # en este caso decimos que sólo capture el error si es de tipo TypeError
    print('se a producido un error de tipo TypeError')

# Captura de la información del Error 
    

try:
    print(numero_uno + numero_dos)
    print('hemos logrado hacer la operación')
except ValueError as error_value:  # al capturar el error específico vamos a tener una variable (error_value), donde va a tener la información del error
    print('se a producido un error')
    print()
    print(error_value)
except Exception as exception:
    print(exception)