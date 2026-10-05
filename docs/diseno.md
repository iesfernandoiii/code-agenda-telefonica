# Diseño — Agenda Telefónica (versión 1)

Explicación sencilla: este documento cuenta cómo está organizado el programa por dentro, para que cualquier compañero lo entienda.

## 1. Idea general

- Programa de consola con programación estructurada (sin clases).
- Dos partes: `src/contactos.py` sabe de contactos, `src/agenda.py` habla con el usuario.
- Las funciones son pequeñas y tienen nombres claros.

## 2. Datos en memoria

Una lista de diccionarios. Ejemplo:

```text
[
  {"nombre": "ana", "telefono": "612345678"},
  {"nombre": "luis", "telefono": "623456789"}
]
```

Se eligió así porque es fácil de leer en 2.º de Bachillerato y no necesita clases.

## 3. Constantes

En `src/contactos.py`, arriba del todo:

- `RUTA_DATOS = "data/contactos.txt"`: dónde se guarda.
- `SEPARADOR = ";"`: qué separa nombre y teléfono.

Si cambian, solo se tocan estas dos líneas.

## 4. Funciones de `src/contactos.py`

- `normalizar_nombre(nombre)`: quita espacios de fuera y pasa a minúsculas.
- `nombre_es_valido(nombre)`: falso si es `None`, vacío o solo espacios.
- `telefono_es_valido(telefono)`: verdadero si son 9 dígitos y no empieza por `0`.
- `nombre_ya_existe(agenda, nombre)`: compara ya normalizado, para impedir duplicados.
- `crear_agenda()`: devuelve `[]`.
- `anadir_contacto(agenda, nombre, telefono)`: valida, comprueba duplicado y añade. Devuelve `True` o `False`.
- `buscar_por_nombre(agenda, nombre)`: búsqueda exacta en minúsculas.
- `buscar_por_telefono(agenda, telefono)`: búsqueda exacta de dígitos.
- `eliminar_contacto(agenda, nombre)`: borra sin confirmación. Devuelve `True` o `False`.
- `mostrar_contactos(agenda)`: devuelve texto listo para imprimir.
- `guardar_contactos(agenda, ruta)`: escribe todo el fichero.
- `cargar_contactos(ruta)`: lee el fichero, crea uno vacío si no existe, ignora líneas rotas y duplicados (se queda con el primero).

## 5. Funciones de `src/agenda.py`

- `mostrar_menu()`: imprime las 6 opciones.
- `pedir_opcion()`: solo acepta `1` a `6`.
- `pedir_nombre()`, `pedir_telefono()`: piden datos con `strip()`.
- `main()`: carga al inicio, repite el menú, guarda tras añadir/eliminar y al salir.

## 6. Decisiones tomadas

1. Nombres duplicados: no se permiten (sin distinguir mayúsculas).
2. Teléfonos duplicados: sí se permiten.
3. Búsqueda: exacta en ambos casos.
4. Eliminar: sin confirmación.
5. Carga con duplicados: se queda con el primero.
6. Teléfono: se guarda como texto (`str`), sin `+34`, espacios ni guiones.

## 7. Pruebas

En `tests/test_contactos.py` hay 16 pruebas con `pytest`, una por comportamiento: validaciones, añadir (incluido duplicado), buscar por nombre y teléfono, eliminar, mostrar, guardar/cargar, fichero inexistente y líneas rotas.
