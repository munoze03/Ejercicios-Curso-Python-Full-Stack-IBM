'''Realiza una función que realice la descomposición en
factores de un número. Deberá devolver una lista con
los factores de dicho número. Recordad que la
descomposición en factores de un número consiste
en hallar el conjunto de números primos cuya
multiplicación dé dicho número como resultado.'''

def factorial(x):
    primos = []
    for i in range(2, x+1):
        while x % i == 0:
            primos.append(i)
            x = x / i
    print(primos)

factorial(60)

'''Crea una función log que acepte cualquier número de
argumentos y los imprima por pantalla en una misma
línea. La línea debe empezar con el prefijo ‘LOG: ’.'''

def log(*args):
    print('LOG:', args)

log('a','d','f','gf','g','gh','h','v')
log(1,2)

'''Modifica la función log para que usuario pueda
especificar cualquier prefijo que desee.'''

def log(pref, *args):
    print(pref, args)

log('hola', 'a','d','f','gf','g','gh','h','v')
log('adios', 1,2)

'''Modifica la función log para que el prefijo tenga el
valor por defecto ‘LOG: ’'''

def log(pref='LOG: ', *args):
    print(pref, args)

log('hola', 'a','d','f','gf','g','gh','h','v')
log(1,2)