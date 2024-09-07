nom=input("Nombre del trabajador\n")
sal=int(input("Salario del trabajador\n$"))

sub=0

if sal<=1_200_000:
    sub=120_000

print(f"El subsidio de transporte es ${sub:,}")