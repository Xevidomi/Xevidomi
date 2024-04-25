#operador in

a ='manzana'
b = "e" in a
print('resultado in', a)

c =  [1,2,3,4,5]
d= 6
resultado_in_enumerado = d in c
print("resultado in enumerado", resultado_in_enumerado)

# operador not in   
lista_de_palabras = ['perro','gato','elefante']
palabra_no_existe = 'perro'
resultado_not_in = palabra_no_existe not in lista_de_palabras
print ("resultado no en", resultado_not_in) 