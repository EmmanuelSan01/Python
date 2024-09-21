import io

fd=open("Ciclo 2 Phyton/Codigo/08 Archivos/data.txt","r")

cad=fd.read()
print(cad)

fd.seek(0)
cad=fd.read(5)
print(cad)

fd.close()