# --------- PROGRAMACIÓN ORIENTADA A OBJETOS (POO)--------------
"""from --archivo-- import --clase--"""

"""
Surge en los años '70. Utiliza las clases para organizar el código de tal forma que nos permita agrupar conjuntos de variables y funciones para posteriormente utilizarlas.
Un objeto es una entidad que combina datos (llamados atributos) y funciones especifícas de estas clases (llamados métodos)
Para definir clases, utilizaré el CamelCase en caso de el naming de mis clases incluyan dos o más palabras. Además está aceptado y normalizado el uso de mayúsculas para definir las clases. Debemos tener en cuenta que Python es keysensitive, es decir:

class Coche:
class coche:

--> No es lo mismo

"""
class Coche:
    def acelerar(self):
       print("El coche esta acelerando")
       
    def frenar(self):
        print("El coche esta frenando")
        
        
mi_coche = Coche()

mi_coche.frenar()

class Cliente:
    def establecer_nombre(self, nombre):
        self.nombre = nombre
        
    def obtener_nombre(self):
        return self.nombre
    
    def establecer_edad(self, edad):
        self.edad = edad
    
    def obtener_edad(self):
        return self.edad
    

cliente_uno = Cliente()
cliente_dos = Cliente()

cliente_uno.establecer_nombre("Pepe")
cliente_uno.establecer_edad(40)

print("El nombre del cliente es:", cliente_uno.obtener_nombre())
print("La edad del cliente es:", cliente_uno.obtener_edad())