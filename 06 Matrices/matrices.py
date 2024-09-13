#Matrices

def ingresarDatosMat(m):
    for f in range(len(m)):
        print(f"Ingrese datos de la fila {f+1}: ")
        for c in range(len(m[f])):
            m[f][c]=int(input(f"mat[{f+1}][{c+1}]? "))

def imprimirMat(m):
    for f in range(len(m)):
        for c in range(len(m[f])):
            print(m[f][c],end="\t")
        print("")


def crearMatriz(fil,col):
    m=[]
    for f in range(fil):
        m.append([None]*col)
    return m

m=[# 0 1 2
    [1,2,3], #0
    [1,5,6]  #1
            ]#2x3

print(m[0])

#imprimir el 5
print(m[1][1])

mat=[]
mat=crearMatriz(3,5)
#mat[2][2]=15
ingresarDatosMat(mat)
imprimirMat(mat)