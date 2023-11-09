# Práctica de Polimorfismo en Programación Orientada a Objetos

## Objetivo

En esta práctica, desarrollarás un entendimiento claro del polimorfismo mediante la creación de una jerarquía de clases que representen diferentes formas geométricas.

### Paso 1: Comprender el Concepto

Antes de comenzar a codificar, asegúrate de entender qué es el polimorfismo y cómo se aplica en la programación orientada a objetos. ¿Puedes explicar cómo permite el polimorfismo que diferentes clases respondan a la misma llamada de método de maneras distintas?

### Paso 2: Definir la Clase Base

- **Tarea:** Define una clase llamada `Forma`. Esta será tu clase base.
- **Preguntas de comprensión:**
  - ¿Qué es una clase base?
  - ¿Qué método debería tener la clase `Forma` para que sea polimórfica?

### Paso 3: Crear Clases Derivadas

- **Tarea:** Crea dos clases derivadas que hereden de `Forma`. Nómbralas `Circulo` y `Cuadrado`.
- **Preguntas de comprensión:**
  - ¿Cómo se relacionan estas clases derivadas con la clase base `Forma`?
  - ¿Qué significa "sobrescribir" un método en este contexto?

### Paso 4: Implementar Polimorfismo

- **Tarea:** Implementa un método en cada una de las clases derivadas que muestre cómo cada forma se dibuja de manera diferente.
- **Preguntas de comprensión:**
  - ¿Cuál es la ventaja de llamar al mismo método en diferentes objetos y obtener diferentes comportamientos?
  - ¿Cómo sabes qué método `dibujar` se llamará?

### Paso 5: Uso Polimórfico de las Clases

- **Tarea:** Escribe una función que acepte un objeto de tipo `Forma` y llame al método `dibujar` del objeto.
- **Preguntas de comprensión:**
  - ¿Por qué puedes pasar cualquier objeto de `Forma` a esta función?
  - ¿Qué concepto de la programación orientada a objetos permite esto?

### Paso 6: Crear y Probar Objetos

- **Tarea:** Crea instancias de `Circulo` y `Cuadrado` y usa la función que escribiste para dibujar estas formas.
- **Preguntas de comprensión:**
  - ¿Qué ocurre cuando llamas al método `dibujar` en las instancias de `Circulo` y `Cuadrado`?
  - ¿Puedes añadir otra forma como `Triangulo` y extender la funcionalidad sin cambiar el código existente?

### Conclusión y Reflexión

- **Tarea:** Reflexiona sobre cómo el polimorfismo puede ayudar a hacer el código más flexible y mantenible.
- **Preguntas de comprensión:**
  - ¿Cómo podría cambiar tu código si no usaras polimorfismo?
  - ¿Qué otros conceptos de la programación orientada a objetos están estrechamente relacionados con el polimorfismo?

---

Recuerda probar tu código y verificar si los resultados son los esperados. El polimorfismo es un pilar de la OOP y entenderlo te ayudará a escribir código mejor organizado y más flexible.
