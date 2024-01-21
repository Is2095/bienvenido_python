
# Modulos

# Es como una librería, algo que usamos fuera de nuestro código
# Es el lugar donde guardo código 
# cada archivo puede ser es como un módulo
# Un módulo es una serie de operaciones y utilidades que intenten resolver problemas con una relación

import modulo # de esta manera traemos todo lo que tiene este modulo (archivo) y desde acá se podrá acceder
# los nombres de los módulos no deben empezar con números
modulo.sumValue(4, 5, 1) # para acceder al código del archivo modulo se deberá poner el nombre del archivo un . y el nombre de la función


from modulo import printValue, sumValue # en este caso del módulo (modulo) sólo importar la función printValue.
printValue('importando solo una parte del módulo')
sumValue(3, 98, 34)

import math # módulo que trae Python
import random 

print(math.pi)
print(math.pow(2,4))
print(random.random())

from math import pi as PI_VALUE
print(PI_VALUE)