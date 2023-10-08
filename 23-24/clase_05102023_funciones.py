

#Definición y Llamada de Funciones:

#Cómo definir funciones usando def y cómo llamarlas.
## Argumentos y Parámetros:
def saludo(nombre):
    print(f'Hola, {nombre}!')
  
saludo ()
    
# Argumentos posicionales y nombrados.
def mostrar_info(nombre, edad):
    print(f'{nombre} tiene {edad} años.')

mostrar_info('Juan', 25)  # Argumento posicional
mostrar_info(edad=30, nombre='Maria')  # Argumento nombrado

# Argumentos predeterminados.
def mostrar_info(nombre, edad=20):
    print(f'{nombre} tiene {edad} años.')

mostrar_info('Juan')  # Usará la edad predeterminada de 20

#Argumentos variables (*args y **kwargs).
def suma(*args):
    print(sum(args))

suma(1, 2, 3, 4)  # Sumará todos los números y mostrará 10

#Valores de Retorno:
def suma(a, b):
    return a + b

resultado = suma(5, 3)  # resultado será 8
# Uso de la instrucción return.
# Retorno de múltiples valores.
def obtener_info():
    return 'Juan', 25

nombre, edad = obtener_info()  # nombre será 'Juan' y edad será 25


# Ámbito de las Variables:
# Ámbito local vs global.
# Uso de la palabra clave global.

x = 10
def cambiar_x():
    global x
    x = 20
cambiar_x()  # x ahora será 20

# Documentación:
def suma(a, b):
    """Suma dos números y devuelve el resultado.
    Args:
    a (int): Primer número.
    b (int): Segundo número.

    Returns:
    int: La suma de a y b.
    """
    return a + b

# Cómo y por qué escribir docstrings.
# Funciones como Objetos:
def saludar():
    print('Hola!')

saludo = saludar
saludo()  # imprimirá 'Hola!'
# Asignar funciones a variables.
# Pasar funciones como argumentos a otras funciones.
def ejecutar_funcion(func):
    func()

ejecutar_funcion(saludar) 

#Retornar funciones desde otras funciones.
## Funciones Anónimas (lambda):
suma = lambda a, b: a + b
print(suma(5, 3))  # imprimirá 8


#Decoradores:

# Qué son y cómo pueden usarse para modificar el comportamiento de las funciones.
# Funciones Recursivas:
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))  # imprimirá 120


# Uso de try, except, finally dentro de funciones.
# Testing:
def dividir(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        print('No se puede dividir por cero!')
    else:
        print(f'Resultado: {resultado}')
    finally:
        print('Fin de la operación')

dividir(10, 2)  # Output: Resultado: 5.0 \ Fin de la operación
dividir(10, 0)  # Output: No se puede dividir por cero! \ Fin de la operación

#Introducción a la escritura de pruebas unitarias para funciones con frameworks como unittest o pytest.

#Optimización:

# Uso de técnicas como memoización para mejorar el rendimiento de las funciones.
# Funciones de Orden Superior y Cierre (Closure):
def suma(a, b):
    return 10

def operacion(funcion, a, b):
    return funcion(a, b)

funcion_suma = suma
resultado = operacion(funcion_suma,10, 10)

print(resultado)

# Funciones anidadas
def operacion():
    def suma(a, b):
        return a + b

    return suma

resultado = operacion()(10, 20)
print(resultado)

# Ejercicio
def funcion_principal():
    a = 'a'
    b = 'b'

    def funcion_anidada():
        c = 'c'

        print(a)
        print(b)

    funcion_anidada()
    print(c)
    
# otro ejemplo
def funcion_principal():
    a = 'a'
    b = 'b'

    def funcion_anidada():
        c = 'c'
        b = 'Cambios de valor'

    funcion_anidada()
    print(b)
    
    def funcion_principal():
    a = 'a'
    b = 'b'

    def funcion_anidada():
        c = 'c'
        print(b)
        b = 'Cambios de valor'

    funcion_anidada()
    print(b)
    
    #nonlocal
    def funcion_anidada():
        nonlocal b

        c = 'c'
        print(b)
        b = 'Cambios de valor'