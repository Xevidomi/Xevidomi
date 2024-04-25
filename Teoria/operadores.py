#operadores de comparacion

#+=
c = 10
c += 2
print(f"El valor de c es {c}")

#-=
a = 5
a -= 1

print(f"el valor de a es: {a}")

#*=
b = 2
b *= 3
print(f"el valor de b es: {b}")

##/=
d = 8
d /= 4
print(f"el valor de d es: {d}")
#//=
e = 7
e //= 2
print(f"el valor de e es: {e}")

#operadores de igualdad

# ==

x = 5
y = 6
result = x == y
print(f"¿Son iguales? {result}")

# =!
z = 5
y = 8
result_2  = z != y
print(f"¿No son iguales? {result_2}")

#Operador de mayor o menor que < > <=
g = 5
h = 6
if g < h :
    print("g es menor que h")
elif g == h:
    print("g es igual que h")
else:
    print("g es mayor que h")
