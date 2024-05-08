'''Un usuario introduce texto desde teclado y queremos
averiguar si es un número entero. Si es entero lo
añadiremos a una variable tipo lista de números
enteros.'''
lista = list()
x = input(("Introduce un numero: "))
if x.isnumeric():
    print("Es un numero")
    num = int(x)
    lista.append(num)
else:
    print("No es un numero")                

'''Tenemos un diccionario en el que asociamos los
números de los documentos de identidad de ciertas
personas con su edad. Queremos realizar un
programa en el que el usuario introduzca un el
número de un documento de identidad. Si dicho
número ya está en el diccionario debe mostrar la
edad, en caso contrario debe solicitarnos que
introduzcamos la edad, que posteriormente
añadiremos al diccionario.'''
dic = {"09042722": 36 , "09019181": 37}

texto = input("Introduce numero DNI")

if texto in dic:
    print("El DNI ", texto," esta ya incluido, esta persona tiene ", str(dic[texto]))
else:
    edad = input("El DNI introducido no está en la lista par incluirlo dime la edad")
    if edad.isnumeric():
        num = int(edad)
        dic[texto] = num
        print("Añadido al diccionario")
print(dic)

'''¿Cómo haríamos si quisiéramos guardar este
diccionario en un archivo y posteriormente abrirlo
siempre que queramos consultarlo?
Para ello usamos el paquete Path y Pickle (los
veremos más detalladamente en otro momento).
Pickle nos ofrece procedimientos para poder leer y
escribir diccionarios en archivos. El paquete Path lo
utilizamos para comprobar si el archivo existe.'''

import pickle
from pathlib import Path

#Creamos el diccionario
d = dict()

#Preguntamos el nombre del archivo con los datos
file_name = input("Introduce el nombre del archivo que contiene el diccionario: ")

#Comprobamos que existe
path = Path(file_name)
if path.is_file():
    #Abrimos el archivo en modo lectura
    input_file = open(file_name, 'rb')
    d = pickle.load(input_file)
    #Cerramos el archivo
    input_file.close()
else:
    print("El archivo no existe, creamos el nuevo diccionario")

#Comprobamos el DNI
document_reader = input("Introduce un DNI: ")

if document_reader in d:
    print("La edad de ", document_reader, " es ", str(d[document_reader]))
else:
    age = input("El DNI introducido no existe, introduce su edad: ")
    if age.isnumeric():
        num = int(age)
        d[document_reader] = num
        print("DNI añadido al diccionario")

#Guardamos el archivo y cerramos
output_file = open(file_name, 'wb')
pickle.dump(d, output_file)
output_file.close()
