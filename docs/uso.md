# Manual de uso — Agenda Telefónica (versión 2)

Explicación sencilla: este documento enseña a usar la agenda paso a paso, como si fuera la primera vez.

## 1. Requisitos

- Tener Python instalado (probado con Python 3.13.7).
- Tener `pytest` y `openpyxl` instalados (ver `requeriments.txt`).
- Estar en la carpeta del proyecto `code-agenda-telefonica`.

## 2. Cómo arrancar

```bash
python -m src.agenda
```

## 3. Qué puedes hacer en el menú

1. **Añadir contacto**: escribe un nombre y un teléfono.
   - El nombre se guarda con `title()` (`ana perez` se guarda como `Ana Perez`).
   - No se puede repetir un nombre que ya exista (sin distinguir mayúsculas).
   - El teléfono debe tener 9 dígitos, sin empezar por 0, sin espacios ni guiones. Ejemplo válido: `612345678`.
   - Si algo falla, el programa avisa y no lo añade.
2. **Buscar por nombre**: escribe el nombre (da igual mayúsculas). La búsqueda es exacta.
3. **Buscar por teléfono**: escribe los 9 dígitos exactos. Puede devolver varios contactos, porque los teléfonos duplicados sí se permiten.
4. **Eliminar contacto**: escribe el nombre. Lo borra sin pedir confirmación y avisa si no existía.
5. **Mostrar todos**: en orden de llegada, como `nombre;telefono`. Si no hay ninguno, dice `Agenda vacia.`
6. **Mostrar todos (A-Z)**: ordenados por nombre de la A a la Z.
7. **Mostrar todos (Z-A)**: ordenados por nombre de la Z a la A.
8. **Salir**: guarda la agenda y termina.

## 4. Dónde se guardan los datos

- En `data/contactos.xlsx` (sustituye al `.txt`, sin migrar datos).
- Primera fila de cabecera: `Nombre | Número`. Desde la fila 2, un contacto por fila.
- Si el fichero no existe, el programa lo crea con la cabecera.
- Las filas vacías o rotas se ignoran al cargar.
- Si el fichero trae el mismo nombre dos veces, se queda con el primero.

## 5. Cómo pasar las pruebas

```bash
python -m pytest -v
```

Deberías ver `19 passed`.
