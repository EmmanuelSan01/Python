#Escriba un programa que envíe un mensaje "Vota por mi mascota" a todos los correos que aparecen en el From:
#Su programa debe mostrar un mensaje como el siguiente por cada correo:
#cwen@iupi.edu --> "Vota por mi mascota" :::> [CORREO ENVIADO]
fd=open("Ciclo 2 Phyton/Codigo/08 Archivos/mbox.txt","r")

email=set()
for linea in fd:
    if linea.startswith("From:"):
        correo=linea.split()[1]
        if correo not in email:
            print("\nTo:",correo,"\n\t--> Vota por mi mascota\n:::> [CORREO ENVIADO]")
            email.add(correo)
print("")

fd.close()