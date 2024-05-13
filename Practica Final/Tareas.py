from os import system
#Creamos la clase tarea con sus Getter y Setter
class Tarea():
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.finalizada = 'Pendiente'

    def get_Descripcion(self):
        return self.descripcion
    
    def set_Descripcion(self, descripcion):
        self.descripcion = descripcion

    def get_Finalizada(self):
        return self.finalizada
    
    def set_Finalizada(self, finalizada):
        self.finalizada = finalizada

class miErrorEleccion(Exception):
    def __init__(self, valor):
        self.valor = valor
    def __str__(self):
        return str(self.valor)


#Iniciamos programa
opcion = 0
lista = []
cabecera = '''\n           PROGRAMA DE GESTIÓN DE TAREAS
             CREADO POR ENRIQUE MUÑOZ
        ====================================
        '''
menu = '''
          1. Agregar nueva tarea
          2. Marcar tarea como completada
          3. Mostrar todas las tareas
          4. Eliminar una tarea
          5. Finalizar'''

def introducirTarea():
    descripcion = input('''
          Introduce la tarea a programar:
              
          ''')
    tarea = Tarea(descripcion)
    lista.append(tarea)

def mostrasTareas():
    n = 1
    for t in lista:
        print("        " + str(n) + " " + t.get_Descripcion() , ' - ' , t.get_Finalizada())
        n += 1
    # input('\n' + "        Pulsa intro para continuar.")

def completarTarea():
    numTarea = int(input('''
        Introduce el numero de tarea a completar:
        
        '''))
    lista[numTarea-1].set_Finalizada('COMPLETADA')
    print('\n        Tarea ' + lista[numTarea-1].get_Descripcion() + ' completada\n')
    input('        Pulsa intro para continuar.')

def borrarTarea():
    numTarea = int(input('''
        Introduce el numero de tarea a eliminar:
        
        '''))
    print('\n        Tarea ' + lista[numTarea-1].get_Descripcion() + ' eliminada\n')
    lista.pop(numTarea-1)
    input('        Pulsa intro para continuar.')
    
def comprobarOpcion(opcion):
    if opcion == 1:
        system("cls")
        print(cabecera)
        introducirTarea()
        
    elif opcion == 2:
        system("cls")
        print(cabecera)
        mostrasTareas()
        completarTarea()
        
    elif opcion == 3:
        system("cls")
        print(cabecera)
        mostrasTareas()
        input('\n' + "        Pulsa intro para continuar.")

    elif opcion == 4:
        system("cls")
        print(cabecera)
        mostrasTareas()
        borrarTarea()
        

#PROGRAMA PRINCIPAL
while opcion!=5:
    system("cls")
    print(cabecera + menu)
    try:
        opcion = int(input('\n          Introduce opcion: \n\n          '))
        if opcion < 1 or opcion > 5:
            raise ValueError("Excepcion lanzada manualmente")
        else:
            comprobarOpcion(opcion)
    except ValueError:
        print('\n          Tienes que marcar un numero del 1 al 5')
        input('\n' + "          Pulsa intro para continuar.")
