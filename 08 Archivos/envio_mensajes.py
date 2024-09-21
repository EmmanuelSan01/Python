with open("Ciclo 2 Phyton/Codigo/08 Archivos/mbox.txt","r") as fd:
    lstEmail=[]
    for linea in fd:
        if linea.startswith("From:"):
            correo=linea.split()[1]+" enviado [OK]\n"
            if correo not in lstEmail:
                lstEmail.append(correo)
lstEmail.reverse()

with open("Ciclo 2 Phyton/Codigo/08 Archivos/correos_enviados","w") as fd:
    fd.writelines(lstEmail)