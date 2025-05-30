# Inicialización de variables
n = 0 # Variable para el número actual ingresado
c = '' # Variable para el operador
res = 0 # Resultado acumulado de las operaciones

# Se pide el primer número y se almacena como resultado inicial
n = int(input('Número: '))
res = n

# Bucle principal que se ejecuta hasta que el usuario ingrese '='
while c != '=':
    c = input('Operador: ') # Se solicita el operador
    
    if c == '=':
        break # Si el operador es '=', se termina el bucle
    elif c not in ['+', '-', '*', '/']: # Si el operador no es válido, se muestra un error y se termina
        print('Error, operador incorrecto')
        c = '=' # Se fuerza la salida del bucle
    else:
        n = int(input('Número: ')) # Si el operador es válido, se pide otro número

        if c == '+':
            res = res + n
        elif c == '-':
            res = res - n
        elif c == '*':
            res = res * n
        elif c == '/':
            if n == 0: # Control de error: división por cero
                print('Error: no se puede dividir entre 0')
                c = '=' # Se fuerza la salida del bucle
            else:
                res = res / n # División válida
        
print(f'Resultado: {res}'); # Se imprime el resultado final
=======
n = 0  # Variable para el número actual ingresado
c = ''  # Variable para el operador
res = 0  # Resultado acumulado de las operaciones
historial = []  # Lista para guardar historial de operaciones

def ingresar_numero():
    """
    Solicita un número entero al usuario.
    Vuelve a intentar si la entrada no es válida.
    """
    while True:
        try:
            return int(input('Número: '))
        except ValueError:
            print('Error, el valor ingresado no es válido, vuelve a intentarlo')

print('--------------------------------------------------------------------------------------------------------')

# Se solicita el primer número y se asigna al resultado inicial
n = ingresar_numero()
res = n

# Bucle principal: pide operador y número hasta que se ingrese '='
while True:
    c = input('Operador: ')  # Se solicita el operador

    if c == '=':
        break  # Sale del bucle
    elif c not in ['+', '-', '*', '/']:
        print('Error, operador incorrecto, vuelve a intentarlo')
        continue  # Pide operador nuevamente

    n = ingresar_numero()  # Solicita un nuevo número
    aux = res  # Guarda el valor anterior del resultado

    # Operaciones aritméticas
    if c == '+':
        res = res + n
    elif c == '-':
        res = res - n
    elif c == '*':
        res = res * n
    elif c == '/':
        # Validación de división por cero con reintento
        while n == 0:
            print('Error: no se puede dividir entre 0, vuelva a intentarlo')
            n = ingresar_numero()
        res = res / n  # División válida

    # Añade al historial de operaciones
    historial.append(f'{aux} {c} {n} = {res}')

# Muestra del resultado final
print(f'\nResultado: {res}')
print('--------------------------------------------------------------------------------------------------------')

# Impresión del historial numerado
print('Historial de operaciones')
for i, h in enumerate(historial, 1):
    print(f'{i} - {h}')
