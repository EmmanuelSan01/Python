articulos={1:"Lapiz",2:"Cuadernos",3:"Borrador",4:"Calculadora",5:"Escuadra"}
valores={1:2500,2:3800,3:1200,4:35000,5:3700}
n=int(input("Ingrese la cantidad de artículos\n"))
for i in range(0,n):
    code=int(input(f"\nIngrese el código del artículo {i+1}\n"))
    amount=int(input(f"\nIngrese la cantidad del artículo {i+1}\n"))
    for k in articulos.keys():
        informe=valores[code]*amount
        print(informe)
