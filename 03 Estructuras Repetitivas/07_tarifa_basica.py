name=input("Nombre\n")
stat=int(input("Estrato\n"))
cont=True
while cont: #cont==True
    basic=0
    if stat==1:
        basic=10000
    elif stat==2:
        basic=15000
    elif stat==3:
        basic=30000
    elif stat==4:
        basic=50000
    elif stat==5:
        basic=65000
    print("\n", "="*40)
    print("Numbre: ",name)
    print("Tarifa básica: $",basic)
    print("\n", "="*40)
    option=input("\n¿Desea continuar? SI(S) o NO(N)?\n")

    #cont=option=="N" or option=="n"
    if option=="N" or option=="n":
        cont=False
    else:
        print("\n", "-"*40)
        name=input("\nNombre\n")
        stat=int(input("Estrato\n"))