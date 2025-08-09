def QuickSort(lista):
    print("ORDENAMIENTO")
    if len(lista) <= 1:
        return lista
    pivote = lista[0]
    menores = [x for x in lista[1:] if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista[1:] if x > pivote]

    return QuickSort(menores) + iguales + QuickSort(mayores)

def Busqueda():
    print("BUSQUEDA")


Diccionario = {}

cantParticipantes = int(input("Ingrese la cantidad de participantes: "))
cont = 0
opcion = 0

while opcion != 4:
    print("1. AGREGAR PARTICIPANTES")
    print("2. MOSTRAR PARTICIPANTES ORDENADOS POR NOMBRE")
    print("3. MOSTRAR PARTICIPANTES ORDENADOS POR EDAD")
    print("4. SALIR")
    opcion = int(input("OPCION A INGRESAR: "))

    match(opcion):
        case 1:
          while (cont < cantParticipantes):
            print("INGRESO DE PARTICIPANTES")
            dorsal = int(input("NUMERO DE DORSAL: "))
            Diccionario[dorsal]["NOMBRE"] = input("Ingrese el nombre: ")
            Diccionario[dorsal]["Edad"] = int(input("Ingrese la edad: "))
            Diccionario[dorsal]["CATEGORIA"] = input("Ingrese la categoria: ")
            cont += 1
        case 2:
          lista = list(Diccionario.items())
          resultado = QuickSort(lista)
          for dorsal in resultado:
            print(f"{dorsal}:[valor]")









