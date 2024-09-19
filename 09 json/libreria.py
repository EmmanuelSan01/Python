import json

from click import option

def guardar(book):
    with open("09 json/libreria.json","w") as fd:
        json.dump(book,fd)
    if not fd.closed:
        fd.close()

def leerPrecio():
    while True:
        try:
            price=int(input("Precio del libro:\n"))
            if price<1000:
                print("\t>>>ERROR. Precio incorrecto.")
                continue
            return price
        except ValueError:
            print("\t>>>ERROR. Precio inválido.")

def leerAutor():
    while True:
        try:
            author=input("Autor del libro:\n")
            if len(author.strip())==0:
                print("\t>>>Autor inválido")
                continue
            return author
        except Exception as e:
            print("\tError al ingresar el autor.\n"+e)

def leerTitulo():
    while True:
        try:
            title=input("Título del libro:\n")
            if len(title.strip())==0:
                print("\t>>>Título inválido")
                continue
            return title
        except Exception as e:
            print("\tError al ingresar el título.\n"+e)

def leerCodigo():
    while True:
        try:
            code=input("Código del libro:\n")
            if len(code.strip())==0:
                print("\t>>>Código inválido")
                continue
            return code
        except Exception as e:
            print("\tError al ingresar el código.\n"+e)

def insertar(book):
    print("\n\n** 1. INSERTAR **")

    code=leerCodigo()
    if code not in book:
        title=leerTitulo()
        author=leerAutor()
        price=leerPrecio()

        data={
            "título":title,
            "autor":author,
            "precio":price
        }

        book[code]=data
        book=dict(sorted(book.items()))
    else:
        print("El código ya existe en la librería")

    input("Presione cualquier letra para volver al menu...")
    return book

def consultar(book):
    print("\n\n** 2. CONSULTAR **")
    input("Presione cualquier letra para volver al menu...")

    """
    libreria={
        codigo1(str):{
            título:(str)
            autor(str)
            precio:int
        },
        codigo2(str):{
            título:(str)
            autor(str)
            precio:int
        }
    }
    """

def menu():
    while True:
        print("** LIBRERÍA **")
        print("1. Insertar")
        print("2. Consultar")
        print("3. Salir")
        print("\n>> Opción?\n",end="")
        try:
            option=int(input())
            if option<1 or option>3:
                print("ERROR. Opción no válida.")
                input("Presione cualquier letra para volver al menu...")
                continue
            return option
        except ValueError:
            print("ERROR. Opción no válida.")
            input("Presione cualquier letra para volver al menu...")

#PROGRAMA PRINCIPAL
libreria={}
while True:
    op=menu()
    match op:
        case 1:
            libreria=insertar(libreria)
            guardar(libreria)
        case 2:
            consultar(libreria)
        case 3:
            print("\n\tGracias por usar el software.\n")
            break