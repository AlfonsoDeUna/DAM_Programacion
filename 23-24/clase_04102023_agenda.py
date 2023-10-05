import sys
import os

cita = {
    "tarea": "",
    "fecha": "",
    "prioridad" :""
}

agenda = []

def addFecha (cita_copia, fecha):
    cita_copia["fecha"] = fecha

def addTarea (cita_copia, tarea):
    cita_copia["tarea"] = tarea    

def addPrioridad (cita_copia, prioridad):
    cita_copia["prioridad"] = prioridad
      
def addCita(tarea, fecha, prioridad):
    cita_copia = cita.copy()
    addFecha (cita_copia,fecha)
    addTarea (cita_copia,tarea)
    addPrioridad (cita_copia, prioridad)
    agenda.append (cita_copia)
    
def borrarCita(tarea):
    for cit in agenda:
        if cit["tarea"] == tarea:
            agenda.remove(cit)
            
def buscarCita(tarea):
    for cit in agenda:
        if cit["tarea"] == tarea:
            return cit
    return None

def visualizarMenu():
    os.system('cls')
    print ("--------------------menu de citas-----------------")
    print ("===================================================")
    print ("")
    print ("1. añadir cita: ")
    print ("2. borrar cita: ")
    print ("3. visualizar todas las citas: ")
    print ("4. salir: ")
    print ("")
    return input ("dime qué quieres hacer (1,2,3,4))---->  ")

def visualizar(cita):

    tarea_valor = cita["tarea"]
    fecha_valor = cita["fecha"]
    prioridad_valor = cita["prioridad"]
    print ("--------------------cita-----------------")
    print ("=========================================")
    print ("")
    print (f"nombre de la cita: {tarea_valor}"  )
    print (f"nombre de la cita: {fecha_valor}"  )
    print (f"nombre de la cita: {prioridad_valor}"  )
    print ("")
    print ("-------------------------------------------")
    
if __name__ == '__main__':

    while (True):
        salida = visualizarMenu()
        match salida:
            case "1":
               
                nombre_tarea = input ("dime el nombre de la cita: ")
                fecha_tarea = input ("dime la fecha: ")
                prioridad_tarea = input ("dime la prioridad: ")
                addCita(nombre_tarea, fecha_tarea, prioridad_tarea)
                input("------------- pulse una tecla ------------")
                
            case "2":
              
                nombre_tarea = input ("dime el nombre de la tarea que quieres borrar")
                borrarCita(nombre_tarea)
                input("------------- pulse una tecla ------------")
                
            case "3":
               
                for cita in agenda:                    
                    visualizar(cita)
                    print ("------------- pulse una tecla para continuar ------------")
                
            case "4":
                sys.exit()
                