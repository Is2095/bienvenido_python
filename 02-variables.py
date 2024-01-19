
# variables

# el nombre es todo con minúsculas, con _

mi_variable = 'Mi primer variable string'
print(mi_variable)

mi_variable_int = 15
print(mi_variable_int)

mi_variable_str = str(mi_variable_int)
print(mi_variable_str)
print(type(mi_variable_str))

mi_variable_boolean = False
print(mi_variable_boolean)

print(mi_variable, mi_variable_boolean, mi_variable_int, mi_variable_str) # imprime todo como una cadena de texto concatenado
print('este es el valor de la variable boolean:', mi_variable_boolean)

# funciones del sistema
print(len(mi_variable)) # cuenta la cantidad de caracteres

# variables en una sola línea
nombre, apellido, edad, profesion = 'Pepe', 'Tito', 57, 'carpintero' # se puede hacer pero no es una buena práctica
print('el nombre es:', nombre, 'con el apellido:', apellido, 'la edad es', edad, 'y trabaja en:', profesion)

# la función Inputs (función que detiene la ejecución y pide ingresar por consola entradas)
'''
nombre = input('¿Cuál es tu nombre?: ') # le dará un nuevo valor a nombre
edad = input('¿Cuál es tu edad?: ')
print(nombre, edad)
nombre = 2323
print(nombre)
'''

# PYTHON NO ES DE TIPADO FUERTE, PUEDE CAMBIAR EL TIPO DE DATOS DE LA VARIABLE. tipado dinámico

variable_modificar = 'empiezo como string'
variable_modificar = 15
print(variable_modificar)

# ¿forzado de tipado?

variable_modificar_tipado : str = 'estoy tipado como string'
variable_modificar_tipado = 34
variable_modificar_tipado = True
variable_modificar_tipado = 2.8
print(type(variable_modificar_tipado))