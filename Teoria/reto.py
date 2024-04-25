print("\nBienvenidos a tu biblioteca\n")
usuario = str(input("\nNombre del usuario :\n ")) #sobra el print
contraseña_usuario = str(input("\nContrasenya\n")) #falta str
print(f"\nnombre:\n, usuario") #falta doble comilla #falta la f de string al print #sobra la comilla individual
print(f"\ncontraseña: \n", contraseña_usuario)




libros_historia = str(input("\nIngrese el nombre de los libros de historia separados por comas:\n ")) #orden input #falta espacio
libros_ficcion = str(input("\nIngrese el nombre de los libros de ciencia ficcion separados por comas:\n ")) #es string
libros_novela = str(input("\nIngrese el nombre de los libros de novela separados por comas:\n ")) #falta input
libros_ciencia = str(input("\nIngrese el nombre de los libros cientificos separados por comas:\n ")) #minuscula ciencia


lista_historia = libros_historia.split(",")
lista_ficcion = libros_ficcion.split(",")
lista_novela = libros_novela.split(".")
lista_ciencia = libros_ciencia.split(",")

print(lista_historia,lista_ficcion, lista_novela, lista_ciencia)

biblioteca = dict(historia=lista_historia, eficcion=lista_ficcion, novela=lista_novela, cientifico=lista_ciencia),
print(biblioteca)