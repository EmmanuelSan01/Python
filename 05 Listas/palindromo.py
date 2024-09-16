string=input("Ingrese una cadena de caracteres (entre 1 y 50)")
while string!=(""):
    if len(string)>=1 and len(string)<=50:
        alphabetical=(sorted(string))
        print(alphabetical)
        if_equal = [alphabetical[i] == alphabetical[i+1] for i in range(0,(len(alphabetical)-1),2)]
        print(if_equal)
    else:
        print("cantidad inválida de caracteres ingresados")
        break
    string=input("Ingrese una cadena de caracteres (entre 1 y 50)")
        
