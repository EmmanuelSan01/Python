#Dado la base y la altura de un triángulo
#calcular y mostrar su área
#a través de la fórmula área=(base*altura)/2

#ENTRADA
#b:base : float
#h:altura : float

b=float(input("Introduzca la base del triángulo: "))
h=float(input("Introduzca la altura del triángulo: "))

#PROCESO
#a=b*h/2

a=b*h/2

#SALIDA
#a:área : float

#Formateando la salida con format()
print("El área del triángulo es: {:.2f}".format(a))

#Formateando la salida con cadenas f-string
print(f"El área del triángulo es: {a:.3f}")