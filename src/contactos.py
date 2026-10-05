"""Lógica de la agenda telefónica (versión 1).

Guarda los contactos como una lista de diccionarios:
[{"nombre": "ana", "telefono": "612345678"}]

No usa clases, solo funciones sencillas.
"""

RUTA_DATOS = "data/contactos.txt"
SEPARADOR = ";"


def normalizar_nombre(nombre):
    """Quita espacios de fuera y pasa a minúsculas."""
    if nombre is None:
        return ""
    return nombre.strip().lower()


def nombre_es_valido(nombre):
    """Dice si el nombre vale: no vacío ni solo espacios."""
    if nombre is None:
        return False
    texto = nombre.strip()
    if texto == "":
        return False
    return True


def telefono_es_valido(telefono):
    """Dice si el teléfono vale: 9 dígitos, sin empezar por 0."""
    if telefono is None:
        return False
    texto = telefono.strip()
    if len(texto) != 9:
        return False
    if not texto.isdigit():
        return False
    if texto.startswith("0"):
        return False
    return True


def nombre_ya_existe(agenda, nombre):
    """Dice si ese nombre ya está en la agenda (sin mayúsculas)."""
    buscado = normalizar_nombre(nombre)
    for contacto in agenda:
        if contacto["nombre"] == buscado:
            return True
    return False


def crear_agenda():
    """Devuelve una agenda vacía."""
    return []


def anadir_contacto(agenda, nombre, telefono):
    """Añade un contacto si los datos valen y el nombre no existe.

    Devuelve True si lo añade, False si no.
    Los teléfonos duplicados sí se permiten, los nombres no.
    """
    if not nombre_es_valido(nombre):
        return False
    if not telefono_es_valido(telefono):
        return False
    nombre_final = normalizar_nombre(nombre)
    telefono_final = telefono.strip()
    if nombre_ya_existe(agenda, nombre_final):
        return False
    agenda.append({"nombre": nombre_final, "telefono": telefono_final})
    return True


def buscar_por_nombre(agenda, nombre):
    """Busca por nombre exacto (da igual mayúsculas). Devuelve lista."""
    buscado = normalizar_nombre(nombre)
    encontrados = []
    for contacto in agenda:
        if contacto["nombre"] == buscado:
            encontrados.append(contacto)
    return encontrados


def buscar_por_telefono(agenda, telefono):
    """Busca por teléfono exacto. Devuelve lista."""
    if telefono is None:
        return []
    buscado = telefono.strip()
    encontrados = []
    for contacto in agenda:
        if contacto["telefono"] == buscado:
            encontrados.append(contacto)
    return encontrados


def eliminar_contacto(agenda, nombre):
    """Borra el contacto con ese nombre. Sin pedir confirmación.

    Devuelve True si lo borró, False si no existía.
    """
    buscado = normalizar_nombre(nombre)
    for i in range(len(agenda)):
        if agenda[i]["nombre"] == buscado:
            del agenda[i]
            return True
    return False


def mostrar_contactos(agenda):
    """Devuelve el texto con todos los contactos para imprimir."""
    if len(agenda) == 0:
        return "Agenda vacía."
    lineas = []
    for contacto in agenda:
        lineas.append(contacto["nombre"] + SEPARADOR + contacto["telefono"])
    return "\n".join(lineas)


def guardar_contactos(agenda, ruta=RUTA_DATOS):
    """Guarda toda la agenda en el fichero de texto."""
    with open(ruta, "w", encoding="utf-8") as fichero:
        for contacto in agenda:
            fichero.write(contacto["nombre"] + SEPARADOR + contacto["telefono"] + "\n")


def cargar_contactos(ruta=RUTA_DATOS):
    """Lee el fichero y devuelve la agenda.

    Si no existe, crea uno vacío y devuelve lista vacía.
    Las líneas rotas se ignoran. Si hay nombres duplicados,
    se queda con el primero.
    """
    agenda = []
    try:
        with open(ruta, "r", encoding="utf-8") as fichero:
            lineas = fichero.readlines()
    except FileNotFoundError:
        with open(ruta, "w", encoding="utf-8") as fichero:
            pass
        return agenda
    for linea in lineas:
        linea = linea.strip()
        if linea == "":
            continue
        partes = linea.split(SEPARADOR)
        if len(partes) != 2:
            continue
        nombre = partes[0]
        telefono = partes[1]
        # Reutiliza anadir_contacto para validar y evitar duplicados.
        anadir_contacto(agenda, nombre, telefono)
    return agenda
