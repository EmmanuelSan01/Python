import random

def simulacion(veces):
    lanzamientos=[0]*13
    for i in range(veces):
        dado1=random.randrange(1,7)
        dado2=random.randrange(1,7)
        suma=dado1+dado2
        #print(suma)
        lanzamientos[suma]+=1
        #print(lanzamientos)
    return lanzamientos.index(max(lanzamientos))

print("El número que más cae al lanzar dos dado es: ",simulacion(1000000))