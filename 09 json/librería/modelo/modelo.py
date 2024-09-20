from persistencia.persistencia import guardar

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

def insertar(book,arch):
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
        guardar(book,arch)
    else:
        print("El código ya existe en la librería")

    input("Presione cualquier letra para volver al menu...")
    return book

def consultar(book):
    print("\n\n** 2. CONSULTAR **")
    code=input("\nCódigo del libro:\n")
    if code in book:
        print("-> Código",code)
        print(f"-> Título:{book[code]['título']}")        #
        print(f"-> Autor:{book[code]['autor']}")          #Comillas simples dentro de comillas dobles
        print(f"-> Precio: ${book[code]['precio']:,.0f}") #
    else:
        print("\t>>ERROR. El código del libro no existe en la librería")
    input("Presione cualquier letra para volver al menu...")