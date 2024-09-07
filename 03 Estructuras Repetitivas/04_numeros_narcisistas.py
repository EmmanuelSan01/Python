#encontrar si un número es narcisista o no
#es narcisista si la suma de sus dígitos elevados a la cantidad de dígitos es igual al número

import math

n=int(input("Ingrese el número\n"))
if n>0:
    lnum=int(math.log10(n))+1

    suma=0
    temp=n
    for i in range(lnum): #TAMBIÉN: range(1,lnum+1)
        d=n%10
        suma+=d**lnum
        n=n//10
    
    if suma==temp:
        print("El número es narcisista")
    else:
        print("El número no es narcisista")
else:
    print(">>ERROR. El número debe ser positivo")