# Manual de uso — Agenda Telefónica (versión 1)

Explicación sencilla: este documento enseña a usar la agenda paso a paso, como si fuera la primera vez.

## 1. Requisitos

- Tener Python instalado (probado con Python 3.13.7).
- Tener `pytest` instalado para las pruebas (ver `requeriments.txt`).
- Estar en la carpeta del proyecto `code-agenda-telefonica`.

## 2. Cómo arrancar

```bash
python -m src.agenda
```

## 3. Qué puedes hacer en el menú

1. **Añadir contacto**: escribe un nombre y un teléfono.
   - El nombre se guarda en minúsculas (`Ana` se guarda como `ana`).
   - No se puede repetir un nombre que ya exista (`ana` y `ANA` cuentan como el mismo).
   - El teléfono debe tener 9 dígitos, sin empezar por 0, sin espacios ni guiones. Ejemplo válido: `612345678`.
   - Si algo falla, el programa avisa y no lo añade.
2. **Buscar por nombre**: escribe el nombre (da igual mayúsculas). La búsqueda es exacta: `an` no encuentra a `ana`.
3. **Buscar por teléfono**: escribe los 9 dígitos exactos. Puede devolver varios contactos, porque los teléfonos duplicados sí se permiten.
4. **Eliminar contacto**: escribe el nombre. Lo borra sin pedir confirmación y avisa si no existía.
5. **Mostrar todos**: muestra cada contacto como `nombre;telefono`. Si no hay ninguno, dice `Agenda vacía.`
6. **Salir**: guarda la agenda y termina.

## 4. Dónde se guardan los datos

- En `data/contactos.txt`, con codificación `utf-8`.
- Una línea por contacto: `nombre;telefono`. Ejemplo:

```text
ana;612345678
luis;623456789
```

- Si el fichero no existe, el programa crea uno vacío.
- Las líneas vacías o rotas se ignoran al cargar.
- Si el fichero trae el mismo nombre dos veces, se queda con el primero.

## 5. Cómo pasar las pruebas

```bash
python -m pytest -v
```

Deberías ver `16 passed`.
