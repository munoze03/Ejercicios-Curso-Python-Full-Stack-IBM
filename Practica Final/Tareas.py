from os import system
#Creamos la clase Tarea con sus Getter y Setter
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

#Declaramos funcion de espera para que el usuario vea la pantalla hasta que pulse intro
#Para no tener que poner el mismo codigo en varios sitios
def esperar():
    input('\n          Pulsa intro para continuar.')

#Declaramos la funcion de la opcion 1 de introducir una nueva tarea
def introducirTarea():
    descripcion = input('''
          Introduce la tarea a programar:
              
          ''')
    tarea = Tarea(descripcion)
    lista.append(tarea)

#Declaramos la funcion d la opcion 2 de completar una tarea
def completarTarea():
    try:
        if len(lista) != 0:                             #Controlamos esta opcion por si la lista aun no contiene tareas
            numTarea = int(input('''
            Introduce el numero de tarea a completar:
                
            '''))
            if numTarea < 1 or numTarea > len(lista):
                raise ValueError()                      #Lanzamos una excepcion manualmente si los valores no están entre los indices de la lista
            else:
                lista[numTarea-1].set_Finalizada('COMPLETADA')
                print('\n          Tarea ' + lista[numTarea-1].get_Descripcion() + ' completada')
                esperar()
        else:
            print("          No existen tareas a completar actualmente")
            esperar()
    except ValueError:
        print('\n          Tienes que marcar un numero del 1 al '+str(len(lista)))
        esperar()

#Declaramos la funcion de la opcion 3 de mostrar todas las tareas
def mostrasTareas():
    n = 1
    for t in lista:
        print("          " + str(n) + " " + t.get_Descripcion() , ' - ' , t.get_Finalizada())
        n += 1

#Declaramos la funcion de la opcion 4 de eliminar una tarea
def borrarTarea():
    try:
        if len(lista) != 0:                             #Controlamos esta opcion por si la lista aun no contiene tareas
            numTarea = int(input('''
            Introduce el numero de tarea a eliminar:
                
            '''))
            if numTarea < 1 or numTarea > len(lista):
                raise ValueError()                      #Lanzamos una excepcion manualmente si los valores no están entre los indices de la lista
            else:
                print('\n          Tarea ' + lista[numTarea-1].get_Descripcion() + ' eliminada')
                lista.pop(numTarea-1)
                esperar()
        else:
            print("          No existen tareas a eliminar actualmente")
            esperar()
    except ValueError:
        print('\n          Tienes que marcar un numero del 1 al '+str(len(lista)))
        esperar()

#Declaramos la funcion que comprueba la opcion seleccionada
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
        esperar()

    elif opcion == 4:
        system("cls")
        print(cabecera)
        mostrasTareas()
        borrarTarea()

    elif opcion == 5:
        system("cls")
        print(cabecera)
        print('''      MUCHAS GRACIAS POR USAR GESTOR DE TAREAS
                
                  PASA UN BUEN DÍA\n\n''')

#Creamos las variables que vamos a utilizar
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

#INICIAMOS EL PROGRAMA PRINCIPAL
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
        print('\n          Tienes que marcar un numero del 1 al 5 \n')
        esperar()