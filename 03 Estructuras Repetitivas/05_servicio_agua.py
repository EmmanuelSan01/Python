code=int(input("Ingrese el código del usuario\n"))
name=input("Ingrese el nombre del usuario\n")
vigen=input("Ingrese el estado del usuario. Vigente (V) o Suspendido(S)\n")
stat=int(input("ingrese el estrato del uasuario\n"))
cons=float(input("Ingrese el consumo del mes en cm3\n"))
#Agregar FOR
#Agregar error estrato
if vigen=="V" or vigen=="v":
    vCons=200*cons
    if stat==1:
        basic=10000
        total=basic+vCons
    elif stat==2:
        basic=20000
        total=basic+vCons
    elif stat==3:
        basic=30000
        total=basic+vCons
    elif stat==4:
        basic=45000
        total=basic+vCons
    elif stat==5:
        basic=60000
        total=basic+vCons
    elif stat==6:
        basic=70000
        total=basic+vCons
    print("Nombre: ",name)
    print(f"Tarifa básica: ${basic:,.0f}")
    print(f"Tatifa por consumo: ${vCons:,.0f}")
    print(f"Valor a pagar: ${total:,.0f}")
elif vigen=="S" or vigen=="s":
    print("Su servicio se encuentra suspendido")
else:
    print("ERROR. Valor incorrecto ingresado para 'Estado'")