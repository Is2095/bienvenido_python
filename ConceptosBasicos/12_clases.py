
# Clases

# Todo lo que está dentro de una clase va a responder ante una misma lógica
# Identificar nuestro código dentro de un ámbito de actuación

class MiPersona:  # definimos una clase (class) con el nombre Persona, la forma de escribir el nombre es Camel Case ej; MiClase
    pass # esto hace que pase el código y que se ejecute el código

print(MiPersona)
print(MiPersona())

class Persona:
    def __init__(self, nombre, apellido, alias = 'sin alias') -> None: # esto nos daría la capacidad de que la clase Persona reciba parámetros (constructor de clase) donde se colocaran ciertos valores de la clase 
        self.__nombre = nombre # el self es obligatoria para crear una clase, se refiere a él mismo, es decir a la instancia de Persona que acabamos de crear por lo que decimos que en persona va a ver una propiedad nombre = al nombre que viene por parámetro, por lo que empiezan a existir fuera de la clase, por eso, fuera podemos hacer mi_persona.nombre
        self.__apellido = apellido # propiedad privada
        self.full_nombre = f'{nombre} {apellido} ({alias})' # propiedad pública

    def get_nombre (self):
        return self.__nombre
    def caminar(self): # acá definimos una función dentro de la clase, lleva el self, es para poder acceder a los parámetros definidos en la clase
        print(f'{self.full_nombre} está caminando')

mi_persona = Persona('Pepe', 'Tito')
print(mi_persona)
# print(mi_persona.nombre) no se puede acceder a nombre ya que se definió como parámetro privado self.__nombre
# print(f'{mi_persona.nombre} {mi_persona.apellido}')
print()
print(mi_persona.get_nombre()) # al ser privado el parámetro debemos acceder por un médodo que lea el valor, por fuera no es posible leer parámetros privados

mi_persona.caminar()
mi_persona.full_nombre = 'Tata Lico (el Pibe)'
print(mi_persona.full_nombre)
