# Ejercicios de Programación Orientada a Objetos en Python para Juegos

## Ejercicio 1: Herencia en Juego de Aventura

1. **Crea una clase base `Personaje`**
   - Atributos: `nombre`, `vida`, `fuerza`, `defensa`.
   - Método: `atacar(otro_personaje)`.

2. **Desarrolla clases derivadas: `Guerrero`, `Mago`, `Arquero`**
   - Heredan de `Personaje`.
   - Añaden habilidades únicas o modifican atributos base.

3. **Implementa interacción entre personajes**
   - Métodos como `hablar()` o `intercambiar(objeto)`.

## Ejercicio 2: Clases Abstractas en Juego de Estrategia

1. **Crea una clase abstracta `Unidad`**
   - Métodos abstractos: `mover()`, `atacar()`.

2. **Desarrolla clases concretas: `Infantería`, `Caballería`, `Arquero`**
   - Implementan métodos de `Unidad`.
   - Atributos específicos para cada tipo de unidad.

3. **Añade atributos de unidad**
   - Como rango de movimiento o poder de ataque.

## Ejercicio 3: Polimorfismo en Juego de Rol

1. **Crea una clase `Habilidad`**
   - Método: `ejecutar()` que varía según la habilidad.

2. **Personajes con lista de habilidades**
   - Uso polimórfico de habilidades.

3. **Implementa varias habilidades concretas**
   - Heredadas de `Habilidad`.
   - Cada personaje las usa adecuadamente.

## Ejercicio 4: Composición en Juego de Construcción

1. **Diseña una clase `Edificio`**
   - Atributos: `tipo`, `capacidad`, `coste`.

2. **Crea clases para diferentes tipos de edificios**
   - `Casa`, `Granja`, `Barraca`.
   - Contienen y expanden `Edificio`.

3. **Sistema para construir y gestionar edificios**
   - Dentro de un entorno de juego.
