#función que reciba un número y devuelva True si es primo o False si no lo es

def esprimo(num):
    if num>1:
        esPrimo=True
        for i in range(2,num):
            if num%i==0:
                esPrimo=False
                break
        if esPrimo: #esPrimo==True
            return True
        else:
            return False
    else:
        return False
    
def esprimo2(num):
    if num>1:
        esPrimo=True
        for i in range(2,num):
            if num%i==0:
                return False
        return True
    else:
        return False

#Programa que reciba números hastab que se ingrese un primo

n=int(input("Ingrese un número\n"))
while not esprimo(n):
    n=int(input("\nIngrese un número\n"))