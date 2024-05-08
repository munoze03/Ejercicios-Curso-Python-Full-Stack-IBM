#EXCEPCIONES
#Bloque Try-Except
print("BLOQUE TRY - EXCEPT")

def indexador(objeto, indice):
    return objeto[indice]

try:
    print(indexador('Python', 'c'))
except IndexError:                              #Captura IndexError
    print("Has puesto un indice muy grande")
except TypeError:                               #Captura TypeError
    print("El indice tiene que ser un numero")
print('Hemos salido del bloque try-excep\n')

#Raise, Lanza excepciones manualmente
print("RAISE")

try:
    raise IndexError("Excepcion lanzada manualmente")
except:
    print('He capturado mi propia excepcion\n')


#Assert, lanza excepcion manualmente si cumple una condicion
print("ASSERT")

a = 10
b = 0
try:
    assert(b > a), 'A tiene que ser mayor que B!'   #Si se cumple no salta el error
except AssertionError:
    print('Ha saltado el error assert')

print('Si se muestra esto es que no ha saltado el assert\n')

#Creamos nuestra propia excepcion
print("CREANDO EXCEPCION")

class miError(Exception):                 #Las excepciones heredan de Exception
    def __init__(self, valor):
        self.valor = valor

    def __str__(self):
        return str(self.valor)

try:
    raise (miError('Mensaje de Error'))
except miError:
    print('He capturado mi propia excepcion\n')

#Bloque Finally y Else
print("FINALLY Y ELSE")

def divide(x, y):
    try:
        resultado = x/y
    except ZeroDivisionError:
        print('No se puede dividir por cero')
    else:
        print("El resultado es: ", resultado)      #Se ejecuta si no salta la excepcion
    finally:
        print('Ejecutamos el finally')  #Se ejecuta siempre salte o no la excepcion

divide(12, 4)
divide(4, 0)