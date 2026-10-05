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
