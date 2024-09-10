#Función que valide si una contraseña es aceptable
#es aceptable cuando tenga de 3 a 20 caracteres

def validPassword(password):
    lenght=len(password)
    if lenght>=3 and lenght<=20:
        return True
    else:
        return False
    
#Programa que valide una contraseña

pswd=input("Ingrese una contraseña\n")
while not validPassword(pswd):
    pswd=input("\nIngrese una contraseña\n")
print("\nContraseña válida")