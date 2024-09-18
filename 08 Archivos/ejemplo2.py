import io

fd=open("Ciclo 2 Phyton/Codigo/08 Archivos/data.txt","r")

cad=fd.readline().strip()
print(cad)

cad=fd.readline()
print(cad)

fd.close()