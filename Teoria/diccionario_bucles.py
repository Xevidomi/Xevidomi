""" 
#------------ITERANDO UN DICCIONARIO------------

Bucle for: En Python se utiliza para iterar sobre una secuencia (listas, tuplas o diccionarios), con el objetivo de ejecutar un bloque de código una vez para cada uno de los elementos de esa secuencia. Sintaxis:


for elemento in secuencia:
    # Bloque de código a ejecutar
"""

#Ejemplo de iteración básica sobre un diccionario
diccionario = {
    'perro': 'animal que ladra',
    'gato': 'animal que maulla',
    'pájaro': 'animal que pia'
    }

for i in diccionario: #Cuando estoy iterando sobre un diccionario, el bucle for de forma predeterminada itera sobre las claves
    print(i, ":", diccionario[i]) 

#Iterando diccionarios con el método items(): Este método devuelve cada uno de los elementos del diccionario como una tupla. 
for clave, valor in diccionario.items():
    print(clave, ":", valor)

    
#Iterando diccionarios con el método keys(): Este método en iteraciones sobre diccionarios nos va a devolver las claves del diccionario. 
for clave in diccionario.keys():
    print("\nLa clave es: ", clave)
    print("El valor es:", diccionario[clave]) #Como no estoy iterando sobre los valores en el bucle for, para poder acceder a ellos necesitaré hacerlo a través de la clave

#Iterando diccionarios con el método values(): Este método en iteraciones sobre diccionarios nos va a devolver los valores del diccionario. 
for valor in diccionario.values():
    print("\n-El valor es: ", valor)


    