fd=open("Ciclo 2 Phyton/Codigo/08 Archivos/mbox.txt","r")

cont=0
for linea in fd:
    if linea.startswith("From:"):
        cont+=1
print(cont)