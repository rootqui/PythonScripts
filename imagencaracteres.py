# Script de practica sobre listas que imprime una imagen por medio de caracteres.

imagen=[['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


columnas = len(imagen[0])
filas = len(imagen)
for c in range(columnas):
    res = ''
    for f in range(filas):
        res+=imagen[f][c]
    print(res)
