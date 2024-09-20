from funciones_mat import *

matriz=crearMat(2,3)
printMat(matriz)

#inputMat(matriz)
randomMat(matriz,10,100)
printMat(matriz)

matrizI=crearMat(4,4)
matrizI=matrizIdentidad(matrizI)
printMat(matrizI)

print("")

matrizDS=crearMat(4,4)
matrizDS=matrizDiagonalS(matrizDS)
printMat(matrizDS)