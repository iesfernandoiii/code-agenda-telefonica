# Diario de sesiones

## Sesión 1 - 2026-10-05
### Objetivo
Preparar la estructura y la memoria del proyecto.

### Realizado
- Creadas las carpetas y plantillas iniciales.

### Comprobaciones
- `python --version` muestra Python 3.13.7.

### Pendiente
- Inicializar Git y crear el plan de la versión 1.
- Codificar
- Crear pruebas
- Redactar documentación

### Primer paso de la próxima sesión
Leer README, AGENTS, TODO, SESSION_LOG y CHANGELOG; después solicitar un plan sin programar.

## Sesión 2 - 2026-10-05
### Objetivo
Implementar la versión 1 aprobada (sin duplicados, búsqueda por teléfono).

### Realizado
- Creados `src/contactos.py` y `src/agenda.py`.
- Creadas 16 pruebas en `tests/test_contactos.py`.
- Actualizados `README.md`, `TODO.md` y `CHANGELOG.md`.

### Comprobaciones
- `python -m pytest -v`: 16 passed.
- Prueba manual del menú (añadir, buscar por nombre y teléfono, mostrar, salir) correcta.

### Pendiente
- Redactar documentación básica en `docs/` (hecho en sesión 2, falta marcar en TODO).

## Sesión 2 (continuación) - 2026-10-05
### Objetivo
Redactar `docs/` y hacer el primer commit.

### Realizado
- Creados `docs/uso.md` y `docs/diseno.md`.
- TODO marcado como terminado salvo commits futuros.

### Comprobaciones
- `python -m pytest -q`: pendiente de re-ejecutar antes del commit.

## Sesión 3 - 2026-10-06
### Objetivo
Preparar la versión 2: orden A-Z/Z-A y persistencia en data/contactos.xlsx (sustituye al .txt, sin migrar).

### Acuerdos
- Rama persistencia-excel creada, commit DESPUES de programar y probar.
- Cabecera xlsx: Nombre | Numero. Si no existe, se crea con cabecera.
- Nombre con str.title() (ej. Ana Perez); duplicados y busqueda sin distinguir mayusculas.
- Dependencia: openpyxl para .xlsx.

### Pendiente
- Acordar plan v2, aprobar, implementar, probar con pytest y commitear.

## Sesión 4 - 2026-10-06
### Objetivo
Implementar la versión 2 aprobada (title, orden A-Z/Z-A, xlsx).

### Realizado
- `src/contactos.py`: `title()`, `clave_nombre`, `ordenar_contactos`, `mostrar` con `llegada/az/za`, guardar/cargar `.xlsx` con cabecera `Nombre | Número`.
- `src/agenda.py`: menú de 8 opciones (5 llegada, 6 A-Z, 7 Z-A, 8 salir).
- `tests/test_contactos.py`: 19 pruebas v2.
- `docs/uso.md` y `docs/diseno.md`: actualizados a v2.

### Comprobaciones
- `python -m pytest -v`: 19 passed.
- Prueba manual del menú (añadir 3, mostrar A-Z, Z-A, llegada, salir) correcta.
- `data/contactos.xlsx` con cabecera y 3 contactos.
