# esto es un comentario

'''esto es un comentario'''
""" otro comentario """
print("Hola")  
# este es el código que se va a ejecutar

numero = 42
print(numero)
type(numero)


#Puedo declarar varias variables a la vez
nombre, edad, altura = "Juan", 30, 1.

print(nombre)

#namning de las variables --> Minúscula + snake_case

mi_nombre_es = "Xavi"

dato_numero = 2888
dato_decimal = 345.234
dato_cadena_de_caracteres = "esto es una cadena"
dato_cadena_de_caracteres_dos = 'esto es una cadena'

edad = 31
nombre = "Xavi"
peso = 88.5

print(edad, nombre, peso)
#concatenar
print("Mi nombre es " + nombre, "Mi edad es " + str(edad))
cadena = "Hola estoy programando en Python"
print(cadena[0])
print(cadena[-1])
print(cadena[1:4])
print(cadena[5:7])
print(cadena[3:])

"""   CONVERSION DE DATOS  """

numero_entero =  float(3.44567)
numero_entero2 = "el numero entero guai es " + str(numero_entero)

print(numero_entero2)

name = "Xavi"
year = 31
message = "Mi nombre es {} y tengo  {} anos".format(name, year)
print(message)
message = f'Mi nombre es {name} y tengo {year} anos'
print(f"Mi nombre es {name} y tengo {year} anos")
print("Mi nombre es {} y tengo  {} años".format(name, year))

""" Entrada de datos """

entrada = str(input("¿Cual es tu nombre? "))

print("Bienvenido " + entrada + " a este programa. ")

3- 'Ejercicio 3'

name = input("¿Cuál es tu nombre? ")
year = int(input("¿En que año naciste? "))
print(f'Tu nombre es {name} y naciste en el ano {year}.')

#division

result = 8 / 2

print(f"El resultado es " + result)
print(f"El resultado es ,{result}")
print(f"El resultado es " + int(result))