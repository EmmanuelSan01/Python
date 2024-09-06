#Dado una cantidad de segundos
#indique cuantas horas, minutos y segundos correspondientes

segundos=float(input("Ingrese la cantidad de sedundos "))

minutos=segundos/60
horas=minutos/60
minutosFinal=minutos%60
segundosFinal=segundos%60

print(f"Hora = {horas:.0f}")
print(f"Minutos = {minutosFinal:.0f}")
print(f"Segundos = {segundosFinal:.0f}")