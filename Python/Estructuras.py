#ESTRUCTURAS DE DATOS
#Listas pueden tener cualquier tipo, tamaño y son ordenadas
print("LISTAS")
miLista = ["Angel", 43, True]
print(miLista[:])                   #Imprime toda la lista
print(miLista[0])                   #Imprime el objeto en posicion 0
print(miLista[1:3])                 #Imprime los objetos entre posiciones
print("METODOS")
print("Metodo len() imprime la longitud", len(miLista))
print("Metodo append() añade elemento al final de la lista")
miLista.append("ultimo")
print(miLista[:])
print("Metodo pop() elimina elemento especificando lugar y devuelve ese elemento")
print(miLista.pop(3))
print(miLista[:])
print("Metodo insert() añade elemento en la posicion especificada")
miLista.insert(1, "incluyo")
print(miLista[:])
print("Metodo remove() elimina elemento con valor especifico")
miLista.remove("incluyo")
print(miLista[:], '\n')

#Tuplas son inmutables
print("TUPLAS")
miTupla = ("apple", "banana", "cereza")
print(miTupla[1])                   #Accedemos al objeto en poisicion 1
print(miTupla[-1])                  #Indexacion negativa, accedemos desde el final
print(miTupla[1:3])                 #Accedemos a los objetos entre posiciones
print(miTupla[:])                   #Accedemos a todos los elementos de la tupla
print("Convertimos tupla en lista para modificar y volvemos a Tupla")
x = list(miTupla)
x[1] = "kiwi"
miTupla = tuple(x)
print(miTupla[:])
print("Comprobamos si un elemento está en la tupla")
if "kiwi" in miTupla:
    print("si, kiwi existe en la tupla")
print("Emprimimos longitud de la tupla", len(miTupla))
print('Eliminamos la tupla completa con del \n')
del miTupla

#Diccionarios, son desordenador y tienen clave-valor
print("DICCIONARIOS")
dic = {
    "Nombre":"Miguel Angel",
    "Apellido":"Muñoz",
    "Pais":"España",
    "Ciudad":"Alcalá de Henares"
}
print(dic)                          #Imprimimos todo el diccionario
