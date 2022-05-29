# Este es un script de practica sobre listas. El valor de entrada es una lista y devuelve un string con un formato.
# Ejemplo. Si la lista es [manzana, pera, naranja, fresa] la salida es "manzana, pera, naranja y fresa".

def formato(lista):
    res = ''
    if lista:
        longitud = len(lista)
        if longitud > 2:
            for i in range(longitud-2):
                res += lista[i] + ', '
            res += lista[i+1] + ' y ' + lista[i+2]
        elif longitud == 2:
            res = lista[0] + ' y ' + lista[1]
        else:
            res = lista[0]
    return res

#Pruebas para funcion formatoLista
test1 = ['manzana']
test2 = ['pera', 'fresa','naranja']
test3 = ['manzana', 'pera', 'naranja', 'fresa']
test4 = ['manzana', 'papaya', 'fresa', 'pera', 'durazno']

listaPruebas = []
listaPruebas.append(test1)
listaPruebas.append(test2)
listaPruebas.append(test3)
listaPruebas.append(test4)

for test in listaPruebas:
    resultado = formato(test)
    print(resultado)
