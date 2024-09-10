print("Ingrese la fecha (DIA-MES-AÑO)")
d=int(input("Ingrese el día\n"))
m=int(input("Ingrese el mes\n"))
y=int(input("Ingrese el año\n"))
print("Fecha ingresada: ",d,"-",m,"-",y)
if m==1 or m==3 or m==5 or m==7 or m==8 or m==10:
    if d>30:
        print("Mañana será 1 -",m+1,"-",y)
    else:
        print("Mañana será: ",d+1,"-",m,"-",y)
elif m==4 or m==6 or m==9 or m==11:
    if d>29:
        print("Mañana será 1 -",m+1,"-",y)
    else:
        print("Mañana será: ",d+1,"-",m,"-",y)
elif m==12:
    if d>30:
        print("Mañana será 1 -",m-11,"-",y+1)
    else:
        print("Mañana será: ",d+1,"-",m,"-",y)
elif m==2:
    if y%4==0:
        if d>28:
            print("Mañana será 1 -",m+1,"-",y)
        else:
            print("Mañana será: ",d+1,"-",m,"-",y)
    else:
        if d>27:
            print("Mañana será 1 -",m+1,"-",y)
        else:
            print("Mañana será: ",d+1,"-",m,"-",y)