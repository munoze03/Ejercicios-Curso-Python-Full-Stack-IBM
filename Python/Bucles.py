#WHILE
print("BUCLE WHILE")
a = 0
while a<3:
    print (a, end=' ')  #Acabamos con espacio en lugar de salto de linea
    a += 1              #Equivale a: a = a + 1
print (a)               #Estamos fuera del while
print ("Hemos salido fuera del while")

#Sentencia Break
print("SENTENCIA BREAK")
a = 5
while a:                #Utilizamos la propia variable como condicion
    print (a, end=' ')
    if a == 2:
        break
    a -= 1
print('\nFuera del Bucle.')
print('Valor de "a": {}'.format(a))

#Sentencia Continue
print("SENTENCIA CONTINUE")
a = 7
while bool(a):
    a -= 1
    if a % 2 == 0:
        continue        #Saltamos a la siguiente iteracion si a es par
    print (a, end=' ')
print ('\nFuera del bucle.')

#Bloque else al finalizar bucles
print("BLOQUE ELSE EN BUCLES")
a = 13
b = a // 2              #Division entera
while b > 1:
    if a % b == 0:      #% es el resto de la division
        print('{b} es factor de {a}'.format(b,a))
        break
    b -= 1
else:
    print('{} es primo.'.format(a))
print('\nFuera del bucle.')

#BUCLE FOR
print("BUCLE FOR")
for s in ['Me', 'gusta', 'python']:
    print(s, end=' ')

a = 0
for x in [1, 2, 3, 4]:
    a += x

print('\n',a)

#Bule for en un diccionario
print("Bucle for en un diccionario")
keys = ['nombre', 'apellidos', 'edad']
values = ['Guido', 'van Rossum', '60']
d = dict(zip(keys, values))             #Creamos el diccionario

for k in d:
    info = '{}: {}'.format(k, d[k])     #Texto formateado con claves y valores
    print(info)

for k, v in d.items():                  #d.items devuelve tupla con clave, valor
    print('{}: {}'.format(k, v))

#Bucle for en string
print("Bucle for recorriendo un string")
letras = "abcdefghijklmnopqrstuvwxyz"
for l in letras:
    print(l, end=' ')

#Bucle for en varias listas
print('\nBucle for recorriendo varias listas a la vez')
l1 = letras[:8]
l2 = letras[8:16]
l3 = letras[16:]

for a, b, c in zip(l1, l2, l3):
    print(a + b + c, end=' ')

