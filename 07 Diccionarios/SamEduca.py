d_categoria={1:25000,2:30000,3:40000,4:45000,5:60000}
n=int(input("Cantidad de docentes? "))
docentes={}
suma=0
for i in range(n):
    print(f"\nDocente {i+1}")
    cedula=input("Cédula? ")
    dDatos={}
    dDatos["nombre"]=input("Nombre? ")
    dDatos["categoría"]=int(input("Categoría (1-5)? "))
    dDatos["horas_lab"]=int(input("Horas laboradas? "))
    dDatos["honorarios"]=d_categoria[dDatos["categoría"]]*dDatos["horas_lab"]
    docentes[cedula]=dDatos
    suma+=dDatos["honorarios"]

#informe
print("")
print("** IMFORME **".center(40))
print("")

#recorrer el diccionario para imprimir el informe
for k in docentes.keys():
    print("Nombre:",docentes[k]["nombre"].title())
    print(f"Honorarios: ${docentes[k]['honorarios']:,}") #comillas simples dentro de comillas dobles
    print("-"*40,"\n")
# for k,v in docentes.items():
#     print("Nombre:",docentes[v]["nombre"].title())
#     print(f"Honorarios: ${v['honorarios']:,}") #comillas simples dentro de comillas dobles
#     print("-"*40,"\n")

print("")
print("="*40)
print(f"Valor total de los honorarios ${suma:,}")
print("="*40)