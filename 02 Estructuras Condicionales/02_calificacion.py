nom=input("Nombre del estudiante\n")
cuan=float(input("calificación cuantitativa\n"))

cual=""
if cuan>=0 and cuan<60:
    cual="D"
elif cuan>=60 and cuan<80:
    cual="C"
elif cuan>=80 and cuan<90:
    cual="B"
elif cuan>=90 and cuan<100:
    cual="A"
else:
    cual=""

if cual!="":
    print("Nombre: ",nom)
    print(f"Calificación cuantitativa: {cuan:.2f}")
    print("Calificación cualitativa: ",cual)
else:
    print(">>ERROR. Calificación inválida")