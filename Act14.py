def QuickSort(lista):
    print("ORDENAMIENTO")
    if len(lista) <= 1:
        return lista
    pivote = lista[0]
    menores = [x for x in lista[1:] if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista[1:] if x > pivote]

def Busqueda():
    print("BUSQUEDA")


Diccionario = {}

cantParticipantes = int(input("Ingrese la cantidad de participantes: "))
cont = 0

while(cont < cantParticipantes):
    print("INGRESO DE PARTICIPANTES")
    dorsal = int(input("NUMERO DE DORSAL: "))
    Diccionario[dorsal]["NOMBRE"] = input("Ingrese el nombre: ")
    Diccionario[dorsal]["Edad"] = int(input("Ingrese la edad: "))
    Diccionario[dorsal]["CATEGORIA"] = input("Ingrese la categoria: ")
    cont+=1

lista = list(Diccionario.items())
resultado = QuickSort(lista)


