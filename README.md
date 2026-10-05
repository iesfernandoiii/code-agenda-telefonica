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

## Ejecución
```bash
python -m src.agenda
```