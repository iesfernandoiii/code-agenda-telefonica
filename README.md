# Agenda Telefónica

## Objetivo
Crear una aplicación de consola en Python para gestionar contactos.

## Funcionalidades de la versión 1
- Añadir contactos.
- Buscar contactos por nombre.
- Buscar contactos por teléfono.
- Eliminar contactos.
- Mostrar todos los contactos.
- Guardar y cargar contactos desde un fichero de texto plano (data/contactos.txt). Crearlo si no existe.
- Los campos a guardar son "nombre" y "teléfono". El separador de campos será ";".
- Se guardará el nombre del contacto en minúsculas. No se permite vacío, null (None en Python) o solo espacios en blanco.
- No se permiten nombres duplicados (sin distinguir mayúsculas). Los teléfonos duplicados sí se permiten.
- Un teléfono válido es un entero positivo de 9 dígitos. Se guardará como string sin espacios ni guiones.

## Funcionalidades de la versión 2

- Mostrar todos los contactos por orden alfabético (A a Z) según campo nombre.
- Mostrar todos los contactos por orden alfabético inverso (Z a A) según campo nombre.
- Guardar y cargar contactos desde una hoja de cálculo (data/contactos.xlsx). Crearlo si no existe.
- La primera fila del fichero .xlsx será la cabecera, con columnas A=`Nombre` B=`Número`, y si no existe se crea con cabecera.
- La versión con .xlsx sustituye a la versión con .txt. No se migrarán datos de una versión a otra ni conviven juntas.
- No se permite nombre vacío, `None` en Python ni solo espacios en blanco. Se guarda con `str.title()` (ej.: `ana perez` → `Ana Perez`), y la comparación de duplicados/búsqueda sigue sin distinguir mayúsculas.
- El resto de funcionalidades no cambian con respecto a la versión 1.

## Restricciones didácticas
- Programación estructurada.
- Funciones pequeñas y nombres descriptivos.
- No usar clases. No se han visto todavía.
- Código comprensible para alumnado de 2.º de Bachillerato.

## Estructura
- `src/`: código del programa.
- `tests/`: pruebas automáticas.
- `data/`: datos de ejecución.
- `docs/`: documentación adicional.

## Dependencias
- `openpyxl`: necesaria para leer y escribir `data/contactos.xlsx` (formato moderno de Excel). Se instala con `pip install openpyxl` y debe figurar en `requeriments.txt`.

## Ejecución
```bash
python -m src.agenda
```