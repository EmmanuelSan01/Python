import io

fd=open("Ciclo 2 Phyton/Codigo/08 Archivos/data.txt","r")

#RECORRIDO DE ARCHIVOS

for linea in fd:
    print(linea.strip().title())

fd.seek(0)

for car in fd.read():
    print(car,end=",")
    #print(car.strip(),end=",")

fd.close()