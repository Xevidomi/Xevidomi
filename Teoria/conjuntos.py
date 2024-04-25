#*************** CONJUNTOS / SETS **********************
"""Colecciones de datos no ordenadas, a las que no voy a poder acceder a los elementos a través de su index y cuya sintaxis se construye utilizando el símbolo "{}". Admite cualquier tipo de datos. No pueden contener elementos duplicados. No aplica una forma específica para acceder a los elementos
"""
mi_primer_conjunto = {"elemento1", "elemento2", 3, 4, 4.1, False}
print(mi_primer_conjunto)

"""INCISO
Función: Bloque de código que realiza unao varias acciones específicas. Puede ser definido con la palabra reservada "def"
Método: Función predesarrollada dentro del propio lenguaje de programación, que se asocia a un objeto específico y que se llama directamente en ese objeto.
"""

mi_primer_set = set([2, 5, 6, 2, 3, 4]) #También podemos crear conjuntos utilizando el método de constructor set()
print(mi_primer_set) 


#------------OPERACIONES CON CONJUNTOS-----------------
#Conjuntos de referencia
conjunto_uno = {1, 2, 3, 4, 5}
conjunto_dos = {6, 7, 8, 9, 0}

#Union (|): Une los conjuntos, sin respetar el orden de inserción y también pudiendo mezclar los valores de ambos conjuntos en la salida del nuevo conjunto creado.
union = conjunto_uno | conjunto_dos
union_dos = conjunto_uno.union(conjunto_dos)
print("Unión con tubería: ", union, "\nUnión con método union()", union_dos)


#Intersección (&) o .intersection(): Devuelve un nuevo conjunto que contiene todos los elementos que estan en los dos conjuntos.
interseccion = conjunto_dos & conjunto_uno
interseccion_dos = conjunto_uno.intersection(conjunto_dos)
print("Interseccion con &:", interseccion, "\nIntersección con método intersection():", interseccion_dos)