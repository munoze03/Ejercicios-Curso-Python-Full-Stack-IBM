from math import pi

#TESTING
#Unittest

def area(r):
    #Verificamos los valores negativos
    if r<0:
        raise ValueError('No se permiten valores negativos')
    
    #Verificamos los tipos correctos
    if type(r) not in [float, int]:
        raise TypeError('Solo numeros enteros o de coma flotante.')
    
    areaC = pi*(r**2)
    return areaC

