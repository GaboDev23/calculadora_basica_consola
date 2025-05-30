<<<<<<< HEAD
# Calculadora Básica en Python

Este es un pequeño programa en Python que implementa una calculadora de operaciones básicas (`+`, `-`, `*`, `/`) utilizando una estructura de bucle. El usuario ingresa un número inicial, luego operadores y números sucesivos hasta finalizar con el signo igual (`=`), que termina la operación y muestra el resultado.

## Características

- Operaciones soportadas: suma, resta, multiplicación y división.
- Validación de operadores.
- Finaliza con el operador `=`.
- Imprime el resultado final de todas las operaciones encadenadas.
- Controla la división por 0

## Código

```python
n = 0
c = ''
res = 0

n = int(input('Número: '))
res = n

while c != '=':
    c = input('Operador: ')

    if c == '=':
        break
    elif c not in ['+', '-', '*', '/']:
        print('Error, operador incorrecto')
        c = '='
    else:
        n = int(input('Número: '))

        if c == '+':
            res = res + n
        elif c == '-':
            res = res - n
        elif c == '*':
            res = res * n
        elif c == '/':
            if n == 0:
                print('Error: no se puede dividir entre 0')
                c = '='
            else:
                res = res / n

print(f'Resultado: {res}');
```

## Ejemplo de uso

```text
Número: 10
Operador: +
Número: 5
Operador: *
Número: 2
Operador: =
Resultado: 30.0
```

## Requisitos

- Python 3.x

## Mejoras posibles

- Manejar errores si el usuario ingresa un valor no numérico.
- Agregar historial de operaciones.

---

Hecho con 💻 en Python.
=======
# Calculadora Básica en Consola (Python)

Este proyecto es una calculadora de consola en Python que permite realizar operaciones básicas (suma, resta, multiplicación, división) de forma interactiva, mostrando un historial numerado de cada paso realizado.

---

## 🚀 Características principales

- 📥 Ingreso seguro de números enteros (evita entradas inválidas)
- 🧮 Operadores soportados: `+`, `-`, `*`, `/`
- 🛑 Control de división por cero (reintento seguro)
- 📝 Registro y visualización de un historial numerado de operaciones
- ✅ Validación de operador, con reintento automático ante errores

---

## 🧑‍💻 Cómo usar

1. Este proyecto consta de un único archivo: `script.py`
2. Asegurate de tener **Python 3.x** instalado.
3. En tu terminal o consola, navega hasta la carpeta del proyecto y ejecutá:

    ```bash
    python script.py
    ```

4. Seguí las instrucciones en pantalla:
   - Ingresá el primer número
   - Luego elegí un operador (`+`, `-`, `*`, `/`) o `=` para finalizar y ver el resultado
   - Si elegís una operación válida, el programa pedirá un segundo número
   - El resultado se irá acumulando y cada paso quedará registrado en el historial
   - Cuando ingreses `=`, terminarás el proceso y se mostrará el historial

---

## 🧪 Ejemplo de uso

```text
--------------------------------------------------------------------------------------------------------
Número: 10
Operador (+, -, *, / o = para salir): +
Número: 5
Operador (+, -, *, / o = para salir): /
Número: 3
Operador (+, -, *, / o = para salir): *
Número: 2
Operador (+, -, *, / o = para salir): =
Resultado: 10.0
--------------------------------------------------------------------------------------------------------
Historial de operaciones:
1 - 10 + 5 = 15
2 - 15 / 3 = 5.0
3 - 5.0 * 2 = 10.0

## 📌 Mejoras posibles (futuro)

- 🚫 Soportar números decimales (float) en lugar de solo enteros
- ➕ Agregar operadores avanzados (exponenciación, módulo)
- 🔄 Permitir continuar operando tras usar =
- 💾 Exportar historial a archivo de texto o CSV

📝 Autor
Gabriel – tu nombre aquí
Proyecto personal de práctica en Python.
>>>>>>> cf7fa82 (Calculadora Básica en Consola V2)
