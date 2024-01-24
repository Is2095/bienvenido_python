
# Manedo de Archivos

import os

# .txt file

texto_archivo = open('./ConceptosIntermedios/mi_fichero.txt', 'w+', encoding='utf-8') # 'r' es para leer el archivo, 'w' es para escribir el archivo, 'w+' permite sobreescribir el archivo 'r+' leer y escribir el archivo
texto_archivo.write('Mi nombre es Pepe\n' 'Mi apellido es Tito\n' '48 años\n' 'Y mi lenguaje preferido es Python')

#print(texto_archivo.read()) # lee todo el archivo
print(texto_archivo.read(11), '--') # lee los primeros 11 caracteres del archivo
print(texto_archivo.read(7), '--') # lee los próximos 7 caracteres del archivo
print(texto_archivo.readline()) # lee la primer línea del archivo
print(texto_archivo.readline()) # lee la siguiente línea del archivo
print(texto_archivo.readline()) # lee la siguiente línea del archivo
print(texto_archivo.readlines()) # lee todas las líneas del archivo y lo pone en una lista ['Mi nombre es Pepe\n', 'Mi apellido es Tito\n', '48 aÃ±os\n', 'Y mi lenguaje preferido es Python']

for lineas in texto_archivo.readlines():
    print(lineas)

texto_archivo.write('\nmi profesión es carpintero')
print(texto_archivo.read())

with open('./ConceptosIntermedios/mi_fichero.txt', 'a') as mi_otro_archivo: # esta línea maneja la apertura del archivo .txt (con with), y lo abre de forma append (agregar), le agrega datos y se cierra (gracias al with)
    mi_otro_archivo.write('\nY Swift')
with open('./ConceptosIntermedios/mi_fichero.txt', 'r') as mi: # esta línea maneja la apertura del archivo .txt (con with), y lo abre de forma append (agregar), le agrega datos y se cierra (gracias al with)
    print(mi.read())

texto_archivo.close()

# os.remove('./ConceptosIntermedios/mi_fichero.txt') # borra el archivo que le indicamos en el path en el ()

# Archivos .JSON

import json # para trabajar con archivos .json debemos importar el módulo json de python

json_archivo = open('./ConceptosIntermedios/mi_archivo_json.json', 'w+')

json_test = { 
    'nombre': 'Pepe', 
    'apellido': 'Tito', 
    'edad': 59, 
    'lenguaje': ['Python', 'Swift', 'Kotlin', 'Dart', 'JavaScript'],
    'website': 'http:/misitio.com'
}
json.dump(json_test, json_archivo, indent=3)

json_archivo.close()

#with open('./ConceptosIntermedios/mi_archivo_json.json') as mi_otro_archivo_json:
    # for lineas in mi_otro_archivo_json.readlines():
    #     print(lineas)

json_dict = json.load(open('./ConceptosIntermedios/mi_archivo_json.json')) # lee el archivo y coloca los datos en json_dict, con modo diccionario
print(json_dict)
print(type(json_dict))
print(json_dict['lenguaje'])

# csv archivos
import csv
csv_archivo = open('./ConceptosIntermedios/mi_archivo_csv.csv', 'w+') # si no está creado, crea el archivo .csv

csv_writer = csv.writer(csv_archivo) # creamos un objeto csv.writer de csv_archivo para poder escribir un archivo .csv
csv_writer.writerow(['nombre', 'apellido', 'edad', 'lenguajes', 'website']) # escribimos la primera fila
csv_writer.writerow(['Pepe', 'Tito', 59, 'Python', 'http:/misitio.com']) # escribimos la segunda fila
csv_writer.writerow(['Tete', 'Tato', '', 'Python', '']) # escribimos la tercer fila
 # para visulizarlo en un Excel, cambiar en el archivo las , por ;


# .xlsx archivos
# import xlrd # debe instalarse el módulo

# .xml archivos

import xml