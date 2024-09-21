import json
from pathlib import Path

def guardar(book,arch):
    with open(arch,"w") as fd:
        json.dump(book,fd)
    if not fd.closed:
        fd.close()

def cargar(arch):
    archivo=Path(arch)
    book={}
    if archivo.is_file(): #True si exixte y es un archivo
        try:
            with open(arch,"r") as fd:
                book=json.load(fd)
            if not fd.closed:
                fd.close()
        except Exception as e:
            print("\t>>Error al abrir el archivo.\n"+e)
    else:
        print("\tERROR. El archivo no existe.\n")
        input("Presione cualquier tecla para continuar")
    return book