import random

listaPalabras = ['farola','perro','ejercito','camaleon','externocleidomastoideo']
palabraOculta = ""
palabraAdivinar = ""

def elegirPalabra ():
    return random.choice (listaPalabras)

def mostrarPalabra (palabra):
    return list("_" * len(palabra))

def adivinarLetra (letra):
    contador = 0
  
    for i in palabraAdivinar:
        
        if (i == letra):
           palabraOculta[contador] = letra
        contador+=1    
    
palabraAdivinar = "casa"
palabraOculta = mostrarPalabra(palabraAdivinar)
print (palabraOculta)
adivinarLetra ('a')
print (palabraOculta)
palabraOculta = ''.join(palabraOculta) 
print (palabraOculta)