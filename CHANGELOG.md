# Historial de cambios

## [Publicado]

- Estructura inicial del proyecto (sin git iniciado).
- Versión 1 de la agenda: añadir sin nombres duplicados, buscar por nombre y por teléfono (búsqueda exacta), eliminar sin confirmación, mostrar todos, guardar y cargar en `data/contactos.txt` con separador `;`.
- Pruebas con pytest en `tests/test_contactos.py` (16 pruebas).
- Documentación básica en `docs/uso.md` y `docs/diseno.md`.

## [Sin publicar]
### Añadido
- Versión 2: nombre con `str.title()`, orden A-Z y Z-A por nombre, persistencia en `data/contactos.xlsx` con `openpyxl` (cabecera `Nombre | Número`, sustituye al `.txt` sin migrar), menú de 8 opciones.
- Pruebas v2 en `tests/test_contactos.py` (19 pruebas).