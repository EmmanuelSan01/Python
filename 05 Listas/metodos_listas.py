from itertools import count


print("")
#append
lista=[10,"Emmanuel",30,"Sánchez"]
lista.append(40)
print(lista)

#extend
lista2=["Estepa",50]
#lista.append(lista2)
lista.extend(lista2)
print(lista)

#insert
lista.insert(1,20)
print(lista)

#pop
lista.pop()
print(lista)

lista.pop(4)
print(lista)

#remove
lista.remove("Estepa")
print(lista)

print("")

#min
lista=[40,30,5,90,20]
print(min(lista))

#len
print("Tamaño lista: ",len(lista))

#sorted
print(sorted(lista))
print(sorted(lista,reverse=True))

lista=[40,30,5,90,20,1,20,50,60,20]

#count
print(lista.count(20))

#del
del(lista[3])
print(lista)

#limpiar listas
lista.clear()
print(lista)
print(type(lista))

#eliminar lista de la memoria
# del lista
# print(type(lista))
# print(lista)