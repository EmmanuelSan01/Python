import json

def leerUsuario():
    while True:
        try:
            nickname=input("\nUSUARIO:\t")
            if len(nickname.strip())==0:
                print("\tERROR. Usuario no válido")
                continue
            return nickname
        except Exception as e:
            print("\tError al ingresar el usuario.\n"+e)

def leerPassword():
        try:
            password=input("\nCONTRASEÑA:\t")
            if len(password.strip())==0:
                print("\tERROR. contraseña no válida")
                #continue
            return password
        except Exception as e:
            print("\tError al ingresar la contraseña.\n"+e)

def guardar(users,arch):
    with open(arch,"w") as fd:
        json.dump(users,fd)
    if not fd.closed:
        fd.close()

def login(users,arch):
    user=leerUsuario()
    if user not in users:
        user=leerUsuario()
        password=leerPassword()

        credentials={
            "usuario":user,
            "contraseña":password,
        }

        users[user]=credentials
        users=dict(sorted(users.items()))
        guardar(users,arch)
    else:
        print("El código ya existe en la librería")

    input("Presione cualquier letra para volver al menu...")
    return users

def menu():
    while True:
        print("")
        print("BIENVENIDO A SISGESA".center(46))
        print("")
        print("* Menú de Opciones *".center(46))
        print("")
        print("\t1. Registro de grupos")
        print("\t2. Registro de módulos")
        print("\t3. Registro de estudiantes")
        print("\t4. Registro de docentes")
        print("\t5. Registro de asistencia")
        print("\t6. Consultas de información")
        print("\t7. Generación de informes")
        print("\t8. Cambio de contraseña")
        print("\t9. Salida del sistema")
        print("\nIngrese el número correspondiente a la función\n",end="> ")
        try:
            option=int(input())
            if option<1 or option>9:
                print("ERROR. Opción no válida.")
                input("Presione cualquier letra para volver al menu...")
                continue
            return option
        except ValueError:
            print("ERROR. Opción no válida.")
            input("Presione cualquier letra para volver al menu...")

users={}
credentials="PROYECTO/crecenciales.json"
leerUsuario()
leerPassword()
guardar(users,credentials)



while True:
    op=menu()
    match op:
        case 1:
            #registroGrupos()
            pass
        case 2:
            #registroModulos()
            pass
        case 3:
            #registroEstudiantes()
            pass
        case 4:
            #registroDocentes()
            pass
        case 5:
            #registroAsistencia()
            pass
        case 6:
            #consultar()
            pass
        case 7:
            #informes()
            pass
        case 8:
            #changePassword()
            pass
        case 9:
            print("\n\tGracias por usar el software.\n")
            break