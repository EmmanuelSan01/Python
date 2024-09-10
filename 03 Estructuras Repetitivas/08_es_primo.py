#Indicar si un nùmero es primo

num=int(input("Ingrese un número\n"))
if num>1:
    esPrimo=True
    for i in range(2,num):
        if num%i==0:
            esPrimo=False
            break
    if esPrimo: #esPrimo==True
        print("Es primo")
    else:
        print("No es primo")    
else:
    print("No es primo")