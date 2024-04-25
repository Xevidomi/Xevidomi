""" 
EJERCICIO
Crea una clase TAREA que permita establecer un nombre y una prioridad
 
Crear una instancia de la clase tarea.
 
Pide al usuario que introduzca el nombre de la tarea y asignáselo a el 
 atributo nombre 

Pide al usuario que introduzca la prioridad de la tarea y asignáselo a 
el atributo prioridad 

Muestra la tarea 1 utilizando la función print()
 
 Crea una tarea 2 siguiendo los mismos pasos que has realizado para crear 
 la tarea 1
     """
#Crea una clase TAREA que permita establecer un nombre y una prioridad
class tarea:
    def nombre(self):
        print("Vamos a definir el nombre de la tarea:")
    def prioridad(self):
        print("Vamos a definir la prioridad:")
#crear una instancia
tarea1 = tarea()
tarea1.nombre()
tarea1.prioridad()

#Pide al usuario que introduzca el nombre de la tarea y asignáselo al atributo
nombre = input("Introduce el nombre de la tarea: ")
tarea1.nombre = nombre
#Pide al usuario que introduzca la prioridad de la tarea y asignáselo al atributo
prioridad = input("Introduce la prioridad de la tarea: ")
tarea1.prioridad = prioridad
#Muestra la tarea 1 utilizando la función print()
print("La tarea es: ", tarea1.nombre, "y su prioridad es: ", tarea1.prioridad)
        