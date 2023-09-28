cuadricula = ["_","_","_","_","_","_","_","_","_"]
ganador = False

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

def comprobarVertical1(jugador):
    if (cuadricula[0] == cuadricula[3] == cuadricula[6] == jugador):
        return True
    else:
        return False
    
def comprobarVertical2(jugador): 
    if (cuadricula[1] == cuadricula[4] == cuadricula[7] == jugador):
        return True
    else:
        return False
     
def comprobarVertical3(jugador):  
    if (cuadricula[2] == cuadricula[5] == cuadricula[8] == jugador):
        return True
    else:
        return False
      
def comprobarHorizontal1(jugador):  
    if (cuadricula[0] == cuadricula[1] == cuadricula[2] == jugador):
        return True
    else:
        return False
     
def comprobarHorizontal2(jugador):
    if (cuadricula[3] == cuadricula[4] == cuadricula[5] == jugador):
        return True
    else:
        return False 
      
def comprobarHorizontal3(jugador):
    if (cuadricula[6] == cuadricula[7] == cuadricula[8] == jugador):
        return True
    else:
        return False 
     
def comprobarDiagonal1(jugador):
    if (cuadricula[0] == cuadricula[4] == cuadricula[8] == jugador):
        return True
    else:
        return False
    
def comprobarDiagonal2(jugador):
    if (cuadricula[2] == cuadricula[4] == cuadricula[6] == jugador):
        return True
    else:
        return False


def siEsTresRaya(jugador):
    
    cv1 = comprobarVertical1(jugador)
    cv2 = comprobarVertical2(jugador)
    cv3 = comprobarVertical3(jugador)
    ch1 = comprobarHorizontal1(jugador)
    ch2 = comprobarHorizontal2(jugador)
    ch3 = comprobarHorizontal3(jugador)
    cd1 = comprobarDiagonal1(jugador)
    cd2 = comprobarDiagonal2(jugador)
    
    if (cv1 or cv2 or cv3 or ch1 or ch2 or ch3 or cd1 or cd2):
        return True
    else:
        return False
    
            
## programa principal3
if __name__ == "__main__":
    
    while (ganador == False):
        
        visualizar()
        comprobacion = False
        while (comprobacion == False): 
        
            posx = input ("Jugador X --> dame la posición donde quieres colocar tu valor: ")
            comprobacion = comprobarPosicion(int (posx))
        
        anidirValor(int(posx),"x")
        visualizar()
        
        if (siEsTresRaya("x")):
            ganador == True
        else:
            comprobacion = False
            while (comprobacion == False): 
                    
                posy = input ("Jugador O --> dame la posición donde quieres colocar tu valor: ")
                comprobacion = comprobarPosicion(int(posy))

            anidirValor(int(posy),"o")
            visualizar()
            
            if (siEsTresRaya("o")):
                ganador == True
                    
