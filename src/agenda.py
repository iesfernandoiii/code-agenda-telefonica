"""Programa principal: menú de consola de la agenda (versión 2)."""

from src.contactos import (
    crear_agenda,
    anadir_contacto,
    buscar_por_nombre,
    buscar_por_telefono,
    eliminar_contacto,
    mostrar_contactos,
    guardar_contactos,
    cargar_contactos,
)


def mostrar_menu():
    """Imprime las opciones del menú."""
    print("--- Agenda Telefónica ---")
    print("1. Añadir contacto")
    print("2. Buscar por nombre")
    print("3. Buscar por teléfono")
    print("4. Eliminar contacto")
    print("5. Mostrar todos")
    print("6. Mostrar todos (A-Z)")
    print("7. Mostrar todos (Z-A)")
    print("8. Salir")


def pedir_opcion():
    """Pide un número del 1 al 8 y lo valida."""
    texto = input("Elige una opción (1-8): ").strip()
    if texto in ("1", "2", "3", "4", "5", "6", "7", "8"):
        return texto
    print("Opción no válida, escribe un número del 1 al 8.")
    return ""


def pedir_nombre():
    """Pide el nombre por teclado."""
    return input("Nombre: ").strip()


def pedir_telefono():
    """Pide el teléfono por teclado."""
    return input("Teléfono (9 dígitos): ").strip()


def main():
    """Arranca la agenda: carga, muestra el menú y guarda los cambios."""
    agenda = cargar_contactos()
    if len(agenda) == 0:
        agenda = crear_agenda()
    salir = False
    while not salir:
        mostrar_menu()
        opcion = pedir_opcion()
        if opcion == "1":
            nombre = pedir_nombre()
            telefono = pedir_telefono()
            if anadir_contacto(agenda, nombre, telefono):
                guardar_contactos(agenda)
                print("Contacto añadido.")
            else:
                print("No se pudo añadir (nombre vacío, duplicado o teléfono inválido).")
        elif opcion == "2":
            nombre = pedir_nombre()
            encontrados = buscar_por_nombre(agenda, nombre)
            if len(encontrados) == 0:
                print("No encontrado.")
            else:
                for contacto in encontrados:
                    print(contacto["nombre"] + ";" + contacto["telefono"])
        elif opcion == "3":
            telefono = pedir_telefono()
            encontrados = buscar_por_telefono(agenda, telefono)
            if len(encontrados) == 0:
                print("No encontrado.")
            else:
                for contacto in encontrados:
                    print(contacto["nombre"] + ";" + contacto["telefono"])
        elif opcion == "4":
            nombre = pedir_nombre()
            if eliminar_contacto(agenda, nombre):
                guardar_contactos(agenda)
                print("Contacto eliminado.")
            else:
                print("No existe ese contacto.")
        elif opcion == "5":
            print(mostrar_contactos(agenda))
        elif opcion == "6":
            print(mostrar_contactos(agenda, "az"))
        elif opcion == "7":
            print(mostrar_contactos(agenda, "za"))
        elif opcion == "8":
            guardar_contactos(agenda)
            print("Agenda guardada. ¡Adiós!")
            salir = True


if __name__ == "__main__":
    main()
