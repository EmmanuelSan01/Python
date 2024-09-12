def posElemMayList(lst):
    mayor=lst[0]
    pos=[0]
    for i in range(len(lst)):
        if lst[i]>mayor:
            mayor=lst[i]
            pos=i
    return [mayor, pos]

def posMayList(lst):
    mayor=lst[0]
    pos=[0]
    for i in range(len(lst)):
        if lst[i]>mayor:
            mayor=lst[i]
            pos=i
    return pos

def menorLista(lst):
    menor=lst[0]
    for e in lst:
        if e<menor:
            menor=e
    return menor

def mayorLista(lst):
    mayor=lst[0]
    for e in lst:
        if e>mayor:
            mayor=e
    return mayor

def sumaLista(list):
    suma=0
    for e in list:
        suma+=e
    return suma

def imprimeLista(lst):
    for i in lst:
        print(i, end="|")

lista_numeros=[10, 15, 20, 30, 40]
print(type(lista_numeros))
print(lista_numeros)
print(lista_numeros[3])
print(lista_numeros[-1])
print(lista_numeros[-5])

#Recorrer una lista

#1. por sus posiciones

for i in range(len(lista_numeros)):
    print(lista_numeros[i], end=", ")
print("")

for i in range(-1, -len(lista_numeros)-1,-1):
    print(lista_numeros[i], end="* ")
print("")

for i in range(len(lista_numeros)-1,-1,-1):
    print(lista_numeros[i], end="; ")
print("\n"+"-"*30)

#2. por sus elementos

for e in lista_numeros:
    print(e, end="|")
print("")

imprimeLista(lista_numeros)

#funcióm que devuelva la lista de los elementos de la lista
print("La suma de los elementos de la lista es: ", sumaLista(lista_numeros))

#imprimir el mayor elemento de la lista
print("El mayor elemento de la lista es: ",mayorLista(lista_numeros))

#imprimir el menor elemento de la lista
print("El menor elemento de la lista es: ",menorLista(lista_numeros))

#imprimir la posición del mayor elemento de la lista
print("El elemento mayor se encuentra en la posición:",posMayList(lista_numeros)+1)

#imprimir el mayor elemento de la lista y su posición
print("El elemento mayor se encuentra en la posición: ",posElemMayList(lista_numeros)[1]+1)
print("El elemento mayor es: ",posElemMayList(lista_numeros)[0])

lstResult=posElemMayList(lista_numeros)
print("El elemento mayor y su posición es: ",lstResult[0],lstResult[1])

#Modificar una lista

lista_numeros[-1]=35 #lista_numeros[4]=35
print(lista_numeros)

#operadores de las listas

lista_numeros_2=[1,2]

#operador de concatenación
lstrst=lista_numeros+lista_numeros_2
print(lstrst)

#operador (*)  de repetición
lstrst=lista_numeros_2*3
print(lstrst)