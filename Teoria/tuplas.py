# COLECCIONES DE DATOS: TUPLAS ***************************
"""Tipo de estructura de datos que nos permite almacenar datos y que además son INMUTABLES, lo que las hace más rápidas a la hora de acceder a ellas"""
mi_primera_tupla = (10, "Hola", True) 
mi_tupla = 1, 2, 3, "oso", False #Puedo crear una tupla sin utilizar los ()
print( "El tipo de datos de mi tupla es:", type(mi_tupla), mi_primera_tupla)

#Acceder a los elementos de mi tupla
tupla_acceso = 0, 1, 2, "Pepe", 4
print("Accediendo a mi tupla:", tupla_acceso)
tupla_dentro_tupla = 1, 5, 8, ("y", "w", "z"), 5, 6
print("Tupla dentro de otra tupla:", tupla_dentro_tupla[3])

#Modificar los elementos de mi tupla --> ERROR: TypeError: 'tuple' object does not support item assignment
modificar_tupla = 1, 2, 3, 4, [5, 6]
print("Tupla antes de modificación:", modificar_tupla)
#modificar_tupla[2] = 2
#print("Intentando modificar la tupla: ", modificar_tupla)



#Asignar el valor de los elementos de una tupla a variables
tupla_asigna = 3, 4, 5
x, y , z = tupla_asigna
print("Asignación múltiple:",x, y, z)



#Método count(): Este método nos devuelve el número de veces que aparece un valor en la tupla

tupla_count = 1, 2, 3, 1, 2, 3, 1, 2, 3
veces_dos = tupla_count.count(2)
print("\nNúmero de veces que aparece el valor 2: ",veces_dos)

#Método index(valor, [inicio], [fin]): Devuelve el índice de la primera ocurrencia de un valor en la tupla
tupla_index = 10, 20, 30 , 40, 10, 20, 30, 40
indice = tupla_index.index(10, 1, 6)
print("\nPrimer índice del valor 10: ", indice)


#Método len(): Devuelve la longitud (número de elementos) de mi tupla
tupla_longitud = (1, 2, 2, 2, 1, 1, 2, 2, 1, 1, 12, 2, 1, 2)
print("La longitud de la tupla es:", len(tupla_longitud))
longitud = len(tupla_longitud)
print(f"La longitud es {longitud}")


#Operar con tuplas: Puedo realizar operaciones de concatenación (+) y de multiplicación (*)

tupla_uno = 1, 7, 3
tupla_dos = 4, 2, 6
concatenacion_tuplas = tupla_uno + tupla_dos
repetir_tuplas = tupla_uno * 3
print(repetir_tuplas)

