print("Ingrese la hora del día (formato 24 horas)")
h=int(input("Ingrese las horas\n"))
m=int(input("Ingrese los minutos\n"))
print("Hora ingresada: ",h,":",m)
if h>21 and m>-1:
    print("Es hora de dormir")
elif h>17 and m>-1:
    print("Buenas noches")
elif h>11 and m>-1:
    print("Buenas tardes")
elif h>4 and m>-1:
    print("Buenos días")
else:
    print("Es hora de dormir")