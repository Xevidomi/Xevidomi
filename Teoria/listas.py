""" #LISTAS EN PYTHON: Colecciones de datos mutables, a cuyos elementos accedemos
 a través de un index y que nos permiten incluir cualquier tipo de dato. 
 Pueden contener elementos duplicados """
#Sintaxix de las listas_
mi_lista = [1, 2, 3, 0.3, 'Hola', True]
print(mi_lista)

#Acceder a los elementos de la lista
primer_elemento = mi_lista[0]
print(primer_elemento)
print(mi_lista[3])

#Modificar un elemento de la lista
mi_lista[4] = "Adios"
print(mi_lista)

#--Métodos más habituales de las listas en Python

#Método append(): Agregar un elemento al final de nuestra lista. 
mi_lista.append("Nuevo elemento")
tipo_lista = type(mi_lista)
print(mi_lista, "El tipo de datos de la lista es:", tipo_lista)


#--> ¿Cómo hacer que el usuario añada elementos a la lista?
lista_usuario = [] #Creamos una lista vacia
nuevo_elemento = int(input("Introduce un número: "))
lista_usuario.append(nuevo_elemento)
tipo_de_datos = type(nuevo_elemento) #Comprobamos si es int o str...etc
print("lista actualizada:", lista_usuario, "El tipo de dato introducido es:", tipo_de_datos)


#Método sort() - Ordena la lista en su sitio, en la propia lista
lista_ordenada = ["Hola", "Adios", "Buenos días", "Adaia"]

lista_ordenada.sort()
print("La lista ordenada es:", lista_ordenada) #La misma variable, pero actulizada (ordenada)

#Método sorted(): Ordenar los elementos de una lista dando lugar a una nueva lista
nueva_lista_ordenada =  sorted([9, 8, 7, 6, 5, 4,  3, 2, 1])
nueva_lista_dos = [4, 6, 2, 7, 7, 2, 5, 7]
nueva_lista_ordenada_dos = sorted(nueva_lista_dos)
print("Lista ordenada uno: ", nueva_lista_ordenada, "Lista ordenada dos: ",
nueva_lista_ordenada_dos)
print(lista_ordenada, nueva_lista_dos)


#Ordenar de forma descendente
descendente_sort = [2, 9, 5, 7, 6, 8, 1, 3]
descendente_sorted = [2, 9, 5, 7, 6, 8, 1, 2]

print(descendente_sort.sort)
nueva_descendente_sorted = sorted(descendente_sorted)
print(nueva_descendente_sorted)