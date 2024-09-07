#mostrar si un número es perfecto o no
#un número es perfecto si la suma de sus divisores menores al mismo número dan el mismo número

n=int(input("Ingrese un número entero positivo mayor que 1\n"))

if n>1:
    suma=0
    for d in range(1,n):
        if n%d==0:
            suma=suma+d #TAMBIÉN: suma+=d
    if suma==n:
        print("El número es perfecto")
    else:
        print("El número no es perfecto")
else:
    print(">>ERROR. El número debe ser mayor que 1")