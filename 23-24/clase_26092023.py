cuadricula = ["_","_","_","_","_","_","_","_","_"]

# que ponga un valor de un jugador en la cuadrícula
def anidirValor(posicion, valor):
    cuadricula[posicion-1] = valor

# visualizar la cuadricula
def visualizar ():
    
    print ("\n")
    print (cuadricula[0] + "|" + cuadricula[1] + "|" + cuadricula[2])
    print (cuadricula[3] + "|" + cuadricula[4] + "|" + cuadricula[5])
    print (cuadricula[6] + "|" + cuadricula[7] + "|" + cuadricula[8])
    print ("\n")

def comprobarPosicion(posicion):
    if (cuadricula[posicion-1] == "x" or cuadricula[posicion-1] == "o"  ):
        return False
    
    return True
         
            
## programa principal3
while (True):
    visualizar()
    posx = input ("Jugador X --> dame la posición donde quieres colocar tu valor: ")
    comprobacion = comprobarPosicion(posx)
    
    if (comprobacion == True):
        anidirValor(int(posx),"x")
        visualizar()
        posy = input ("Jugador O --> dame la posición donde quieres colocar tu valor: ")
        comprobacion = comprobarPosicion(posy)
        if (comprobacion == True):
            anidirValor(int(posy),"o")
            visualizar()
