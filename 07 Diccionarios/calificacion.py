codigo=0
while codigo!=999:
    codigo=int(input("Código? "))
    dDatos={}
    dDatos["nombre"]=input("Nombre? ")
    dDatos["nota1"]=float(input("Nota 1? "))
    dDatos["nota2"]=float(input("Nota 2? "))
    dDatos["nota3"]=float(input("Nota 3? "))
    dDatos["definitiva"]=dDatos["nota1"]*0.3+dDatos["nota2"]*0.3+dDatos["nota3"]*0.4
    print(dDatos["definitiva"])
    if dDatos["definitiva"]>=3:
        print("APROBÓ")
    else:
        print("REPROBÓ")
