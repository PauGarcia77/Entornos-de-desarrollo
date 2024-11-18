Agenda = {}


def mostrar_menu():
    print("\n1 - Buscar un contacto")
    print("2 - Insertar un contacto")
    print("3 - Actualizar un contacto")
    print("4 - Eliminar un contacto")
    print("5 - Finalizar el programa")
    return input("Elige una opción: ")

def telefono_valido(telefono):
    if 1 <= len(telefono) <= 11:
        return True
    else:
        print("Introduce un número de telefono valido")
        return False

def buscar_contacto():
    print("\nHas elegido la opción de buscar un contacto ")
    nombre = input("Introduce el nombre del contacto que quieres buscar ")
    if nombre in Agenda:
        print(f"He encontrado el contacto que buscas con nombre {nombre} y telefono {Agenda[nombre]} ")
    else:
        print("No he encontrado el contacto que buscas en la agenda ")


def insertar_contacto():
    print("\nHas elegido la opción de insertar un contacto ")
    nombre = input("Introduce el nombre del contacto que quieras guardar ")
    telefono = input("Introduce el número de teléfono: ")
    if telefono_valido(telefono):
        Agenda[nombre] = telefono
        print(f"Contacto {nombre} y numero {telefono} se ha guardado en la agenda ")
    else:
        print("El contacto no se ha guardado ya que ha introducido mas digitos de los posibles ")




def actualizar_contacto():
    print("\nHas elegido la opción de actualizar un contacto ")
    nombre = input("Introduce el nombre del contacto que quieres actualizar ")
    if nombre in Agenda:
        telefono = input("Introduce el nuevo número de teléfono que quieres insertar ")
        if telefono_valido(telefono):
            Agenda[nombre] = telefono
            print(f"Contacto {nombre}  y numero {telefono} se ha actualizado de la agenda ")
    else:
        print("El contacto que quieres actualizar no está en la agenda ")


def eliminar_contacto():
    print("\nHas elegido la opción de eliminar un contacto")
    nombre = input("Introduce el nombre del contacto que quieres eliminar ")
    if nombre in Agenda:
        telefono=Agenda[nombre]
        del Agenda[nombre]
        print(f"Contacto {nombre} y  numero {telefono} se ha eliminado correctamente ")
    else:
        print("El contacto que quieres eliminar no está en la agenda ")



def ejecutar_programa():
    while True:
        opcion = mostrar_menu()
        if opcion == "1":
            buscar_contacto()
        elif opcion == "2":
            insertar_contacto()
        elif opcion == "3":
            actualizar_contacto()
        elif opcion == "4":
            eliminar_contacto()
        elif opcion == "5":
            print("Has elegido acabar el programa")
            break
        else:
            print("Elige una opción válida")


ejecutar_programa()

