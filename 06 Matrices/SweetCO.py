def imprimirMat(m):
    for f in range(len(m)):
        for c in range(len(m[f])):
            print(m[f][c],end="\t")
        print("")

def transponerMat(m):
    filas = len(m)
    columnas = len(m[0])
    mTranspuesta=[]        
    for c in range(columnas):
        mTranspuesta.append([None] * filas)
    for f in range(filas):
        for c in range(columnas):
            mTranspuesta[c][f] = m[f][c]
    return mTranspuesta

def prodMayIngSem(mat,lst):
    lstIng=[]
    for f in range(len(mat)):
        #El siguiente proceso es igual a lstIng.append(sum(mat[f])*lst[f])
        suma=0
        for c in range(len(mat[f])):
            suma+=mat[f][c]#*lst[f]
        lstIng.append(suma*lst[f])#factorizado
    mayor=max(lstIng)
    prod=lstIng.index(mayor)+1
    return [prod,mayor]

#Productos: 1    2     3   4    5
lstPrecios=[1500,5000,6500,2500,22500]

#            Lu  Ma  Mi  Ju  Vi   Sa   Do
matVentas=[[100, 88, 92, 94, 85, 110, 100], #1
           [ 30, 42, 31, 32, 38,  40,  37], #2
           [ 23, 35, 39, 45, 55,  60,  61], #3
           [ 45, 50, 56, 65, 47,  57,  68], #4
           [ 18, 25, 33, 21, 22,  28,  32]] #5

prod,ingProd=prodMayIngSem(matVentas,lstPrecios)
print("El producto que genera más ingresos en la semana es:",prod,f"- Vendió: ${ingProd:,}")
mat=transponerMat(matVentas)
imprimirMat(mat)