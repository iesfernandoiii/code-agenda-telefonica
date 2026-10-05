"""Pruebas de la agenda (versión 1) con pytest."""

from src.contactos import (
    normalizar_nombre,
    nombre_es_valido,
    telefono_es_valido,
    nombre_ya_existe,
    crear_agenda,
    anadir_contacto,
    buscar_por_nombre,
    buscar_por_telefono,
    eliminar_contacto,
    mostrar_contactos,
    guardar_contactos,
    cargar_contactos,
)


def test_normalizar_nombre_pasa_a_minusculas_y_quita_espacios():
    assert normalizar_nombre("  Ana ") == "ana"


def test_nombre_no_vale_vacio_espacios_o_none():
    assert nombre_es_valido("") is False
    assert nombre_es_valido("   ") is False
    assert nombre_es_valido(None) is False
    assert nombre_es_valido("Ana") is True


def test_telefono_valido():
    assert telefono_es_valido("612345678") is True


def test_telefono_invalido():
    assert telefono_es_valido("12345678") is False  # 8 dígitos
    assert telefono_es_valido("6123456789") is False  # 10 dígitos
    assert telefono_es_valido("61a345678") is False  # letras
    assert telefono_es_valido("012345678") is False  # empieza por 0
    assert telefono_es_valido("612 45678") is False  # espacios
    assert telefono_es_valido("612-45678") is False  # guiones
    assert telefono_es_valido(None) is False


def test_anadir_contacto_ok():
    agenda = crear_agenda()
    assert anadir_contacto(agenda, "Ana", "612345678") is True
    assert len(agenda) == 1
    assert agenda[0] == {"nombre": "ana", "telefono": "612345678"}


def test_anadir_no_permite_nombre_duplicado():
    agenda = crear_agenda()
    anadir_contacto(agenda, "Ana", "612345678")
    assert anadir_contacto(agenda, "ANA", "623456789") is False
    assert len(agenda) == 1


def test_anadir_si_permite_telefono_duplicado():
    agenda = crear_agenda()
    anadir_contacto(agenda, "Ana", "612345678")
    assert anadir_contacto(agenda, "Luis", "612345678") is True
    assert len(agenda) == 2


def test_anadir_rechaza_datos_invalidos():
    agenda = crear_agenda()
    assert anadir_contacto(agenda, "   ", "612345678") is False
    assert anadir_contacto(agenda, "Ana", "123") is False
    assert len(agenda) == 0


def test_nombre_ya_existe():
    agenda = crear_agenda()
    anadir_contacto(agenda, "Ana", "612345678")
    assert nombre_ya_existe(agenda, "ANA") is True
    assert nombre_ya_existe(agenda, "Luis") is False


def test_buscar_por_nombre_exacta_sin_mayusculas():
    agenda = crear_agenda()
    anadir_contacto(agenda, "Ana", "612345678")
    assert len(buscar_por_nombre(agenda, "ANA")) == 1
    assert buscar_por_nombre(agenda, "an") == []
    assert buscar_por_nombre(agenda, "Luis") == []


def test_buscar_por_telefono_exacta():
    agenda = crear_agenda()
    anadir_contacto(agenda, "Ana", "612345678")
    anadir_contacto(agenda, "Luis", "612345678")
    assert len(buscar_por_telefono(agenda, "612345678")) == 2
    assert buscar_por_telefono(agenda, "699999999") == []


def test_eliminar_sin_confirmacion():
    agenda = crear_agenda()
    anadir_contacto(agenda, "Ana", "612345678")
    assert eliminar_contacto(agenda, "ANA") is True
    assert len(agenda) == 0
    assert eliminar_contacto(agenda, "Ana") is False


def test_mostrar_contactos():
    agenda = crear_agenda()
    assert mostrar_contactos(agenda) == "Agenda vacía."
    anadir_contacto(agenda, "Ana", "612345678")
    assert mostrar_contactos(agenda) == "ana;612345678"


def test_guardar_y_cargar(tmp_path):
    ruta = str(tmp_path / "contactos.txt")
    agenda = crear_agenda()
    anadir_contacto(agenda, "Ana", "612345678")
    guardar_contactos(agenda, ruta)
    cargada = cargar_contactos(ruta)
    assert cargada == agenda


def test_cargar_sin_fichero_crea_vacio(tmp_path):
    ruta = str(tmp_path / "nuevo.txt")
    agenda = cargar_contactos(ruta)
    assert agenda == []


def test_cargar_ignora_lineas_rotas_y_duplicados(tmp_path):
    ruta = str(tmp_path / "contactos.txt")
    with open(ruta, "w", encoding="utf-8") as f:
        f.write("ana;612345678\n")
        f.write("linea rota sin separador\n")
        f.write("ANA;623456789\n")
        f.write("\n")
        f.write("luis;maltelefono\n")
    agenda = cargar_contactos(ruta)
    assert agenda == [{"nombre": "ana", "telefono": "612345678"}]
