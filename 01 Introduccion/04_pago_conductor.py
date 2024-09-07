from queue import LifoQueue


nombre=input("Introduzca el nombre del conductor: ")
placa=input("Introduzca la placa del vehículo: ")
pasajes=int(input("Introduzca el valor total por pasajes: $"))
encomiendas=int(input("Introduzca el valor total por encomiendas: $"))

pagoPasajes=pasajes*0.25
pagoEncomiendas=encomiendas*0.15
liquidacion=pagoPasajes+pagoEncomiendas

print("Nombre: ",nombre)
print("Placa: ",placa)
print(f"Valor total por pasajes: ${pasajes:,.0f}")
print(f"Valor total por encomiendas: ${encomiendas:,.0f}")
print(f"Pago por pasajes: ${pagoPasajes:,.0f}")
print(f"Pago por encomiendas: ${pagoEncomiendas:,.0f}")
print(f"VALOR TOTAL A PAGAR: ${liquidacion:,.0f}")