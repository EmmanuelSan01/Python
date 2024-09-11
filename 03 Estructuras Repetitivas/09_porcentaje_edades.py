adults=0
underAges=0
for i in range(1,11):
    print("\nIngrese la edad de la persona",i)
    age=int(input(">"))
    if age>17:
        adults+=1
    elif age>-1:
        underAges+=1
    else:
        print("\n>>ERROR. La edad ingresada no es un número válido")
percAdults=(adults/10)*100
percUnderAges=(underAges/10)*100
print(f"\nLa cantidad de mayores de edad corresponde al {percAdults:.2f}% del total")
print(f"\nLa cantidad de menores de edad corresponde al {percUnderAges:.2f}% del total\n")