
# Manejo de paquetes - Python Package Manager-> gestor de paquetes para Python

# Manejo de dependencias. 

# herramienta para ello -> pip: ---> https://pypi.org/ (gestor) Es un repositorio de software para Python. Biblioteca de código abierto (dependencias)
# se comprueba en consola si esta instalado colocando pip --version
# para instalarlo: pip install pip
# por consola: pip muestra opciones

# pip list --> lista todos los módulos instalados con pip´
# pip uninstall nombre_modulo --> desinstala el módulo indicado
# pip show numpy --> da información detallada del módulo numpy

# pip install numpy
import numpy as np
print(np.version.version)
numpy_array = np.array([23, 545, 65, 757, 87, 232, 2345, 5])
print(type(numpy_array))
print(numpy_array * 2)

# pip install pandas
# import pandas 

# pip install requests
import requests

response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=151')
print(response)
print(response.status_code)
#print(response.json())

# Paquete Aritmético

# el archivo __init__.py es un archivo que permite inicializar el contexto y porder disponer de lo módulos

from miPaquetes import Aritmetica

print(Aritmetica.sumar_dos_valores(4, 6))

from miOtroPaquete import otroAritmetica
print(otroAritmetica.sumar_dos_valores(4, 6))


