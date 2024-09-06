nombre=input("Introduzca el nombre del estudiante: ")
nota1=float(input("Introduzca la nota reto 1: "))
nota2=float(input("Introduzca la nota reto 2: "))
nota3=float(input("Introduzca la nota reto 3: "))
ingles=float(input("Introduzca la nota de inglés: "))

definitiva=nota1*0.2+nota2*0.25+nota3*0.35+ingles*0.2

print("La calificación definitiva de ",nombre,f" es: {definitiva:.2f}")