# Repositorio: prueba

**Autor:** IngYeffry
**URL:** https://github.com/IngYeffry/prueba
**Rama principal:** `main`
**Primer commit:** `0cc914f` - "Primer commit"

---

## Descripcion General

Repositorio de aprendizaje y practica de Python. Contiene ejercicios basicos que cubren entrada/salida de datos, formateo de numeros, interfaces graficas con Tkinter y conceptos introductorios de Django.

---

## Estructura de Archivos

```
prueba/
├── Hola Mundo.PY              # Ejercicio basico de entrada/salida
├── Grsfico.PY                 # Ventana grafica con Tkinter
├── Basesdedatos.py            # Archivo vacio (pendiente de desarrollo)
├── DJANGO/
│   ├── Ejercicio1.py          # Ejercicio de tipos de datos y formateo
│   └── sumastring.py          # Ejercicio de suma con strings vs enteros
├── CP_T1_PE_EXPERT_2025.pdf   # Material de referencia (PDF)
├── Variables Basicas.pptm     # Presentacion sobre variables en Python
├── Pasos PAra Inicial en Python.docx  # Guia de inicio en Python
└── Trinket Download-950ba082e0aa.zip  # Archivo descargado de Trinket
```

---

## Descripcion de Cada Archivo Python

### `Hola Mundo.PY`

Primer script del repositorio. Practica conceptos de:

- **`input()`** para pedir datos al usuario (nombre, apellido, color favorito).
- **Concatenacion de strings** con `+`.
- **Conversion de tipos** con `int()` y `str()`.
- **Formateo de numeros** con f-strings (`f"{valor:.3f}"`) y `.format()`.
- Calcula la edad del usuario a partir del ano de nacimiento.

### `Grsfico.PY`

Crea una ventana grafica usando **Tkinter**:

- Ventana titulada "Verificacion de Contrasena".
- Tamano fijo de 480x240 pixeles (`resizable(0,0)`).
- Requiere un archivo de icono `seg.ico` para funcionar.

### `Basesdedatos.py`

Archivo vacio. Probablemente reservado para futuros ejercicios con bases de datos.

### `DJANGO/Ejercicio1.py`

Ejercicio mas completo que demuestra:

- Entrada de datos con `input()`.
- **Diferencia entre `input()` sin conversion (devuelve string) e `int(input())` (devuelve entero)**. Al sumar dos strings se concatenan en vez de sumarse numericamente.
- Uso de `float()` para numeros decimales.
- Tres formas de formatear decimales: `f"{:.5f}"`, `"{:.3f}".format()` y `round()`.

### `DJANGO/sumastring.py`

Ejercicio corto que muestra el **error comun** de sumar un `int` con un `string`:

- `numero1` se convierte a `int`, pero `numero2` se deja como `string`.
- La operacion `numero1 + numero2` produce un `TypeError` en tiempo de ejecucion, sirviendo como ejemplo didactico.

---

## Documentacion Complementaria

| Archivo | Descripcion |
|---------|-------------|
| `CP_T1_PE_EXPERT_2025.pdf` | Material de referencia del curso |
| `Variables Basicas.pptm` | Presentacion PowerPoint sobre tipos de variables |
| `Pasos PAra Inicial en Python.docx` | Documento guia para comenzar con Python |
| `Trinket Download-950ba082e0aa.zip` | Codigo descargado desde la plataforma Trinket |

---

## Tecnologias Utilizadas

- **Python 3** - Lenguaje principal
- **Tkinter** - Interfaz grafica (incluida con Python)
- **Git/GitHub** - Control de versiones
