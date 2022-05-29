
#Practica sobre strings
#Script que imprime una lista de dos dimensiones en formato de cuadricula

def imprimirCuadricula(datos):
    dimensiones = []
    filas = len(datos[0])
    columnas = len(datos)

    for lista in datos:
        dimensiones.append(max([len(item) for item in lista]) + 1)
    dimensiones = tuple(dimensiones)
    
    for f in range(filas):
        i = 0
        res = ''
        for c in range(columnas):
            res += datos[c][f].rjust(dimensiones[i])
            i += 1
        print(res)

lista = [['manzanas', 'naranjas', 'cerezas', 'fresas'],
        ['Alicia', 'Bob', 'Carol', 'David'],
        ['perros', 'gatos', 'alces', 'gansos']]


imprimirCuadricula(lista)