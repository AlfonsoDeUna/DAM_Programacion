# tener una lista de nombres
# añadir nombre
# borrar nombres
# buscar nombres
import sys 
import os

cita = {
    "fecha": "",
    "tarea": "",
    "prioridad": ""    
}

agenda = []

def addName(cita):
    lista_nombre.append(cita)

def deleteName(nombre):
    lista_nombre.remove (nombre)
    
def findName (nombre):
    for i in range (len(lista_nombre)):
        if lista_nombre[i] == nombre:
            return i
    
    return -1
    
if __name__ == "__main__":
    
        while (True):
            print ("1. añadir nombre")
            print ("2. borrar nombre")
            print ("3. buscar nombre")
            print ("4. ver lista")
            print ("5. exit")
            menu = input ("escribe qué quieres hacer: ")
            
            match menu:
                case "1":
                    cita ["fecha"] = input ("dime la fecha: ")
                    cita ["tarea"] = input ("dime de que va la tarea: ")
                    cita ["prioridad"] =  input ("dime la prioridad: ")
                    addName (cita)
                case "2":
                    deleteName (input ("dime el nombre: "))
                case "3":
                    findName (input("dime el nombre: "))
                case "4":
                    print (lista_nombre)
                case "5":
                    sys.exit()
            os.system('cls')