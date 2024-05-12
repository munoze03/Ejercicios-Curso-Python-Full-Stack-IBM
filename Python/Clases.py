#Declaracion de la clase
class Coche():

    #Declaracion del constructor de la clase coche
    def __init__(self, largo, ancho, ruedas, peso, color, is_enMarcha):
        self.largo = largo
        self.ancho = ancho
        self.ruedas = ruedas
        self.peso = peso
        self.color = color
        self.is_enMarcha = is_enMarcha

    #Declaracion de metodos
    def arancar(self):          #self hace referencia a la instancia de la clase
        self.is_enMarcha = True

    def estado(self):
        if(self.is_enMarcha == True):
            return 'El coche está arrancado'
        else:
            return 'El coche está parado'
        
    #Declaracion del metodo Destructor
    def __del__ (self):
        print("Acabas de llamar al metodo destructor. El objeto acaba de ser eliminado")
        

#Declaracion de una instancia de clase, objeto de clase o ejemplar de clase
miCoche = Coche(400, 160, 4, 1200, 'amarillo', True)
miCoche2 = Coche(420, 150, 4, 1500, 'verde', False)

#Acceso a un atributo de la clase coche. Nomenclatura del punto.
print("El largo del coche es de", miCoche.largo, "cm.")
miCoche.arancar()
print(miCoche.estado())


#Acceso a un metodo de la clase Coche nomenclatura del punto.
print("El coche está arrancado:", miCoche.estado())

#Modificamos el valor de una propiedad
miCoche2.ruedas = 10
print("El coche 2 tiene:", miCoche2.ruedas, "ruedas.")

del miCoche