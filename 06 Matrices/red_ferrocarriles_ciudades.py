def crearMatriz(fil,col):
    m=[]
    for f in range(fil):
        m.append([None]*col)
    return m

def ingresarDatosMat(m):
    for f in range(len(m)):
        print(f"Ingrese datos de la fila {f+1}: ")
        for c in range(len(m[f])):
            m[f][c]=input(f"mat[{f+1}][{c+1}]? ")

print("\nIngrese las dimensiones de la matriz")
i=int(input("Ingrese la cantidad de filas\n"))
j=int(input("Ingrese la cantidad de columnas\n"))
matCiudades=crearMatriz(i,j)
ingresarDatosMat(matCiudades)





