import unittest
from Testing import area
from math import pi

class TestArea(unittest.TestCase):
    def test_area(self):
        print('-----test valores de resultado conocido-----')
        self.assertAlmostEqual(area(1), pi)
        self.assertAlmostEqual(area(0), 0)
        self.assertAlmostEqual(area(3), pi*(3**2))

    #Test de valores negativos
    def test_negativos(self):
        print('-----Test de valores negativos-----')
        #Indicamos el tipo de excepcion, la funcion y el valor esperado 
        self.assertRaises(ValueError, area, -1)

    #Test de tipos no compatibles.
    #Verificamos si el tipo de los parametros es el correcto
    #El tipo de la excepcion debe ser TypeError
    #Hacemos una prueba para que cada tipo conocido no valido

    def test_tipos(self):
        print('-----Test de tipos no compatibles-----')
        self.assertRaises(TypeError, area, True)
        self.assertRaises(TypeError, area, 'hola')
        self.assertRaises(TypeError, area, 2+3j)