def busquedaLineal(lst, elem):
    for i in range(len(lst)):
        if lst[i]==elem:
            return [True,i]
    return[False, None]

lista=["Mateo","Marcos","Lucas","Juan","Hugo","Paco","Luis"]

existe,pos=busquedaLineal(lista,"Juan")
if existe: #existe==True
    print("Pasa al ciclo 3")
    print("Posición:",pos)
else:
    print("Muchas gracias por estar en Campus")