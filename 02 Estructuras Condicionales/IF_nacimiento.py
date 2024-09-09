d=int(input("Ingrese su día de nacimiento (1/31)\n"))
if d<16:
    print("Naciste en la primera quincena")
elif d<31:
    print("Naciste en la segunda quincena")
else:
    print("Naciste al final del mes")