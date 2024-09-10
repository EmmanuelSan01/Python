#INSTRUCCIÓN BREAK
#break: rompe o termina satisfactoriamente el ciclo más cercano

#Sumar los nùmero del 1 al 50
suma=0
for i in range(1,51):
    suma+=i #suma=suma+i
    if i==20:
        break
print(suma)