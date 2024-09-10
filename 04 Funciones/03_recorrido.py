#RECORRIDO DE CADENAS

#1. Por sus elementos (caracteres)
str="Hola mundo!"
for c in str:
    print(c)

#ejemplo: cuántas vocales hay en la cadena
vowels=0
for c in str:
    if c=="a" or c=="A" or\
       c=="e" or c=="E" or\
       c=="i" or c=="I" or\
       c=="o" or c=="O" or\
       c=="u" or c=="U":
        vowels+=1
print("\nCantidad de vocales: ",vowels)

print("="*40)

#2 por su INDICE

for i in range(len(str)):
    print(str[i]) #la cadena str en la pocisión i

#ejemplo: cuántas vocales hay en la cadena
vowels=0
for i in range(len(str)):
    if str[i]=="a" or str[i]=="A" or\
       str[i]=="e" or str[i]=="E" or\
       str[i]=="i" or str[i]=="I" or\
       str[i]=="o" or str[i]=="O" or\
       str[i]=="u" or str[i]=="U":
        vowels+=1
print("\nCantidad de vocales: ",vowels)

#ejemplo: En qué pocisión está el primer espacio

for i in range(len(str)):
    if str[i]==" ":
        break
print("\nEl primer _ está en la pocisión ",i)