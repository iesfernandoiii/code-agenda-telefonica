# Diseño — Agenda Telefónica (versión 2)

Explicación sencilla: este documento cuenta cómo está organizado el programa por dentro, para que cualquier compañero lo entienda.

## 1. Idea general

- Programa de consola con programación estructurada (sin clases).
- Dos partes: `src/contactos.py` sabe de contactos, `src/agenda.py` habla con el usuario.
- Las funciones son pequeñas y tienen nombres claros.
- Novedad v2: nombres con `title()`, orden A-Z/Z-A y persistencia en `.xlsx` con `openpyxl`.

## 2. Datos en memoria

Una lista de diccionarios. Ejemplo:

```text
[
  {"nombre": "Ana Perez", "telefono": "612345678"},
  {"nombre": "Luis", "telefono": "623456789"}
]
```

Se eligió así porque es fácil de leer en 2.º de Bachillerato y no necesita clases.

## 3. Constantes

En `src/contactos.py`, arriba del todo:

- `RUTA_DATOS = "data/contactos.xlsx"`: dónde se guarda.
- `CABECERA_NOMBRE = "Nombre"` y `CABECERA_NUMERO = "Número"`: cabecera de la hoja.

Si cambian, solo se tocan estas dos líneas.

## 4. Funciones de `src/contactos.py`

- `normalizar_nombre(nombre)`: quita espacios y usa `title()` (`ana perez` → `Ana Perez`).
- `clave_nombre(nombre)`: pasa a minúsculas para comparar sin distinguir mayúsculas.
- `nombre_es_valido(nombre)`: falso si es `None`, vacío o solo espacios.
- `telefono_es_valido(telefono)`: verdadero si son 9 dígitos y no empieza por `0`.
- `nombre_ya_existe(agenda, nombre)`: usa `clave_nombre`, para impedir duplicados.
- `crear_agenda()`: devuelve `[]`.
- `anadir_contacto(agenda, nombre, telefono)`: valida, comprueba duplicado y añade. Devuelve `True` o `False`.
- `buscar_por_nombre(agenda, nombre)`: búsqueda exacta sin distinguir mayúsculas.
- `buscar_por_telefono(agenda, telefono)`: búsqueda exacta de dígitos.
- `eliminar_contacto(agenda, nombre)`: borra sin confirmación. Devuelve `True` o `False`.
- `ordenar_contactos(agenda, sentido)`: copia ordenada A-Z o Z-A por `clave_nombre`.
- `mostrar_contactos(agenda, orden)`: `llegada`, `az` o `za`; devuelve texto listo para imprimir.
- `guardar_contactos(agenda, ruta)`: escribe el `.xlsx` con cabecera.
- `cargar_contactos(ruta)`: lee el `.xlsx`, crea uno con cabecera si no existe, ignora filas rotas y duplicados (se queda con el primero).

## 5. Funciones de `src/agenda.py`

- `mostrar_menu()`: imprime las 8 opciones.
- `pedir_opcion()`: solo acepta `1` a `8`.
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

En `tests/test_contactos.py` hay 19 pruebas con `pytest`: validaciones, `title()`, añadir (incluido duplicado), buscar por nombre y teléfono, eliminar, ordenar A-Z/Z-A, mostrar, guardar/cargar `.xlsx`, fichero inexistente con cabecera y filas rotas.
