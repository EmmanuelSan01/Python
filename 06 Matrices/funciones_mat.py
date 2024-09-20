import random
from re import M

"""
mat(2,3)

#     col_1 col_2 col_3
mat=[[None, None, None], #fila_0
     [None, None, None]  #fila_1
    ]
"""

def crearMat(fil,col):
    matriz=[]
    for f in range(fil):
        matriz.append([None]*col) #se crea una lista con una longitud igual a la cantidad de columnas
    return matriz

def printMat(mat):
    for f in range(len(mat)): #devuelve la cantidad de filas
        for c in range(len(mat[f])): #devuelve la cantidad columnas
            print(mat[f][c],end="\t") #imprime el contenido de cada lista
        print("") #cuando termina de imprimir cada lista cambia de línea

def inputMat(mat):
    for f in range(len(mat)):
        print("Fila",f+1)
        for c in range(len(mat[f])):
            mat[f][c]=int(input(f"mat[{f+1}][{c+1}]?\n"))
        print("-"*10,"\n")
   
def randomMat(mat,ini,fin):
    for f in range(len(mat)):
        for c in range(len(mat[f])):
            mat[f][c]=random.randrange(ini,fin)

def matrizIdentidad(mat):
    tamf=len(mat)
    tamc=len(mat[0])
    if tamf==tamc: #la matriz identidad es cuadrada
        for f in range(tamf):
            for c in range(tamc):
                if f!=c:
                    mat[f][c]=0
                else:
                    mat[f][c]=1 #crea la diagonal de 1
        return mat
    else:
        return None
    
def matrizDiagonalS(mat):
    tamf=len(mat)
    tamc=len(mat[0])
    if tamf==tamc: #la matriz identidad es cuadrada

        for f in range(tamf):
            for c in range(tamc):
                mat[f][c]=0
                for c in range((len(mat)-1),-1,-1):
                    if c==len(mat)-1:
                        mat[f][c]=1
                        c-=1
        return mat
    else:
        return None