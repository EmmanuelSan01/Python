def imprimirLista(lst):
    for i in lst:
        print(i, end="|")
    print("")

n=int(input("¿Cantidad de letras a ingresar?\n"))

lstvowels=[0]*5 #[0,0,0,0,0]

for i in range(n):
    letter=input(f"Ingrese la letra {i+1}\n")

    letter=letter.strip()
    if len(letter)>0:
        letter=letter[0]
        # if letter.lower()=="a":
        #     lstvowels[0]+=1
        # elif letter.lower()=="e":
        #     lstvowels[1]+=1
        # elif letter.lower()=="i":
        #     lstvowels[2]+=1
        # elif letter.lower()=="o":
        #     lstvowels[3]+=1
        # elif letter.lower()=="u":
        #     lstvowels[4]+=1

        match letter:
            case "a":
                lstvowels[0]+=1
            case "e":
                lstvowels[1]+=1
            case "i":
                lstvowels[2]+=1
            case "o":
                lstvowels[3]+=1
            case "u":
                lstvowels[4]+=1
            case _:
                pass

imprimirLista(lstvowels)