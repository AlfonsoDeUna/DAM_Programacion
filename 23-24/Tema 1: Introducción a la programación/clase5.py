# CLASE DÍA 21/09/2023
# PROGRAMACIÓN

###
#  ¿QUÉ VAMOS A VER HOY?
#  * ESTAMOS TRABAJANDO EN VISUAL STUDIO CODE Y HEMOS VISTO COMO EJECUTAR Y DEBUGEAR
#  * EJERCICIOS DE INVERSIÓN DE CADENAS CON BUCLE FOR
#  * COLECCIONES: EJEMPLOS, EJERCICIOS
###

# tengo una cadena de texto y quiero con un bucle for sacar letra a letra
#cadena = "alfonso"
#for i in range(1,len(cadena)):
#    print (cadena[i])
    
    
# tengo una caden ade texto y quiero darle la vuelta al texto
def cadena_inversa():
    cadena2 = "alfonso"
    resultado = ""
    for i in range(0,len(cadena2)):
        #print (cadena2[len(cadena2)-1-i])
        resultado = resultado + cadena2[len(cadena2)-1-i]
    
#contador de vocales de una cadena
#cadena, for, if 
def contador_vocales():
    cadena = input ("dame una cadena que voy a contar las vocales---> ")
    contador_vocales = 0
    for caracter in cadena:
        if caracter in ['a','e','i','o','u']:
            contador_vocales +=1
    print (contador_vocales)      


##############################################################################################
###################################### COLECCIONES ###########################################

def pruebas_colecciones():
    
    frutas = ['manzana', 'plátano', 'cereza']
    print(frutas)

    numeros = [1,2,3,4,5,6,7]
    print (numeros)

    # obtener de la lista plátano frutas y el número 5 de números
    print (frutas[1])
    print (numeros[4])

    #borrar el numero 5 de numeros que es la posición 4 porque empieza en cero
    numeros.remove(5)

    print (numeros)

    #añadir un elemento al final de lista
    numeros.append(5)
    print (numeros)

    print(len(numeros))
    print (numeros)

    #añadir un elemento en la posición que quieres
    numeros.insert(4,5)
    print (numeros)
    #obtener de la lista de la posicón 2 hasta la 5
    print (numeros[2:5])
    #Obtener 3 números de la lista
    print (numeros[2],numeros[3],numeros[4])
    #recorrer la lista de dos en dos posición 0,2,4
    print (numeros[::2])
    #invertir la lista
    print (numeros[::-1])

    #cadena e inveirte con el método de las listas
    cadena = "alfonso"
    print (cadena[::-1])

# EJEMPLO 2: probar si un elemento existe
def ejemplo2():
   
    numeros = [1,2,3,4,5,6,7]
    print (3 in numeros)

    num = numeros.pop()
    print (num)
    print (numeros)

    numeros.remove(2)
    print (numeros)

# borra una posición del numeros[5]
# del numeros[5]

# EJERCICIO1 quiero borrar de esta lista todos los 2s
def ejercicio1():
  
    lista = [1,2,2]
    print (len(lista))
    ##
    contador=0
    for elemento in lista:
        if (elemento==2):
            contador +=1
        
    for i in (0,contador-1):
        lista.remove(2)       
        
    print (contador)
    print (lista)

# EJERCICIO2 rellena la lista del 1 al 10
def ejercicio2():
    lista2 = []
    for i in range (0,9):
        lista2[i] = i
        
# NOTA: PARA PROBAR LOS EJERCICIOS AQUÍ ESCRIBE EL NOMBRE DE LA FUNCIÓN CON PARÉNTESIS   

pruebas_colecciones()
ejemplo2() 
ejercicio1()    
ejercicio2()
