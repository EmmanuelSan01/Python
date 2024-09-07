A=int(input("Ingrese un número (1/3)\n"))
B=int(input("\nIngrese un número (2/3)\n"))
C=int(input("\nIngrese un número (3/3)\n"))
print("\nEl orden de los números de mayor a menor es\n")
if A>=B and B>=C:
    print(A)
    print(B)
    print(C)
elif A>=C and C>=B:
    print(A)
    print(C)
    print(B)
elif B>=A and A>=C:
    print(B)
    print(A)
    print(C)
elif B>=C and C>=A:
    print(B)
    print(C)
    print(A)
elif C>=A and A>=B:
    print(C)
    print(A)
    print(B)
elif C>=B and B>=A:
    print(C)
    print(B)
    print(A)