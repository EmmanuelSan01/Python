v=0
idProduct={}
products = {
    idProduct ("string"): {
        "name" : ("string"),
        "price" : float (f"{v:.2f}"),
        "quantity" : int (1),#greater equal to 0)
        "discountList" : [ float (f"{v:.2f}"), float (f"{v:.2f}"), ..., float (f"{v:.2f}") ]
    }
}

def menu():
    print("*** PRODUCTOS ACME ***".center(40))
    print("MENU".center(40))
    print("1. Agregar producto")
    print("2. Buscar producto")
    print("3. Listar productos")
    print("4. Listar producto con menor inventario")
    print("5. Listar producto con mayor porcentaje de descuento")
    print("6. Listar producto con menor precio de descuento")
    print("7. Listar producto con mayor precio en inventario")
    print("8. Salir")

option=int(input("   >>Escoja una opción (1-8)"))
match option:
    case "1":
        n=int(input("Cantidad de productos? "))
        idProduct={}
        for i in range(n):
            products=input("Código? ")
            idProduct={}
            idProduct["nombre"]=input("Nombre? ")
            idProduct["precio"]=int(input(""))
            idProduct["cantidad"]=int(input(""))
            idProduct["Descuento"]=produts{[idProduct["categoría"]]}
            