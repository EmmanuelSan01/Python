from datetime import datetime

def leerFecha(msg):
    while True:
        try:
            fecha=datetime.strptime(input(msg),"%d/%m/%Y") #dd/mm/aaaa
            year,month,day=str(fecha).split()[0].split("-")
            return f"{day}/{month}/{year}"
        except ValueError:
            print("Error. Formato de fecha inválido.\n")

def leerFloat(msg):
    while True:
        try:
            num=float(input(msg))
            return num
        except ValueError:
            print("Error. Ingrese un número decimal válido.\n")

def leerEnteroPositivo(msg):
    while True:
        try:
            num=int(input(msg))
            if num<0:
                print("Error. Ingrese un número positivo.\n")
            else:
                return num
        except ValueError:
            print("Error. Ingrese un número entero válido.\n")

def leerEntero(msg):
    while True:
        try:
            num=int(input(msg))
            break
        except ValueError:
            print("Error. Ingrese un número entero válido.\n")
    return num

# edad=leerEnteroPositivo("Ingrese la edad\n")
# print(edad,type(edad))

# temp=leerFloat("Ingrese la temperatura\n")
# print(temp,type(temp))

fecnac=leerFecha("Ingrese la fecha de nacimiento\n")