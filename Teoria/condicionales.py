""" Escribe un programa en Python que solicite al usuario ingresar su edad y luego determine en qué rango de edad se encuentra. El programa debe seguir los siguientes pasos:

Solicitar al usuario que ingrese su edad como un número entero.
Utilizar un condicional if para evaluar la edad ingresada y mostrar un mensaje dependiendo del rango de edad:
Si la edad está entre 0 y 12 años (inclusive), mostrar el mensaje "Eres un niño".
Si la edad está entre 13 y 19 años (inclusive), mostrar el mensaje "Eres un adolescente".
Si la edad está entre 20 y 64 años (inclusive), mostrar el mensaje "Eres un adulto".
Si la edad es 65 o mayor, mostrar el mensaje "Eres un adulto mayor".
Mostrar el mensaje correspondiente al rango de edad detectado.
 

edad = int(input("Cual es tu edad? "))

if  edad <= 12:
    print("Eres un niño")
elif edad >= 13 and edad <= 19:
    print("Eres un adolescente")
elif edad >= 20 and edad <= 64:
    print("Eres un adulto")
elif edad >= 65:
    print("Eres un adulto mayor")
else:
    print("Error en la edad")
"""
""" VERSIÓN B - Versión compleja
Solicitar al usuario que ingrese la cantidad de personas cuyas edades desea evaluar.
Utilizar un bucle for para iterar sobre cada persona y solicitar su edad.
Utilizar un condicional if dentro del bucle para evaluar la edad de cada persona y mostrar un mensaje dependiendo del rango de edad:
Si la edad está entre 0 y 12 años (inclusive), mostrar el mensaje "Eres un niño".
Si la edad está entre 13 y 19 años (inclusive), mostrar el mensaje "Eres un adolescente".
Si la edad está entre 20 y 64 años (inclusive), mostrar el mensaje "Eres un adulto".
Si la edad es 65 o mayor, mostrar el mensaje "Eres un adulto mayor".
Mostrar el mensaje correspondiente al rango de edad detectado para cada persona.

personas = int(input("Cuantas personas vamos a evaluar la edad? "))
for i in range(personas):
    edad_persona=int(input("Ingrese la edad de la persona "+str(i+1)+": "))
    if  edad_persona <= 12:
        print("La",str(i+1),"es un niño.")  
    elif edad_persona >= 13 and edad_persona <= 19:
        print("La",str(i+1),"es un adolescente.")  
    elif edad_persona >= 20 and edad_persona <= 64:
        print("La",str(i+1),"es un adulto.")  
    elif edad_persona >= 65:
        print("La",str(i+1),"es un adulto mayor.")  

 """
"""
Crea un programa en Python que solicite al usuario ingresar dos números enteros positivos, **`inicio`** y **`fin`**, donde **`inicio`** sea menor que **`fin`**. El programa deberá imprimir todos los números pares en el rango desde **`inicio`** hasta **`fin`**, ambos inclusive. Si no hay números pares en el rango dado, el programa debe imprimir un mensaje indicando que no se encontraron números pares. ¡¡Rápido, rápido..!!

1. Solicitar al usuario que ingrese el número inicial del rango y almacenarlo en la variable 
**`inicio`**.
2. Solicitar al usuario que ingrese el número final del rango y almacenarlo en la variable 
**`fin`**.
3. Verificar si **`inicio`** es menor o igual que **`fin`** y si ambos son números positivos. 
Si no lo son, mostrar un mensaje de error y volver al paso 1.
4. Utilizar un bucle **`for`** y la función **`range()`** para iterar sobre los números en el 
rango desde **`inicio`** hasta **`fin`**, inclusive.
5. Dentro del bucle, verificar si cada número es par utilizando un condicional **`if`** y el 
operador **`%`**. Si un número es par, imprimirlo.
6. Si no se encuentran números pares en el rango, imprimir un mensaje indicando que no se 
encontraron números pares.
    
"""

inicio = int(input("Indica un numero inicial de la secuencia: "))
fin = int(input("Indica otro numero final de la secuencia: "))
if inicio  > fin or inicio < 0 or fin < 0 :
    print ("Error con los numeros")
else:
    for i in range(inicio , fin + 1) :
        if i % 2 == 0 :
            print (i)
    else:
        print ("No hay ningun numero par entre estos dos numeros")
