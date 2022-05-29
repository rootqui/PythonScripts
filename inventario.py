#Practica sobre diccionarios 
#Script sobre crear y mostrar un inventario de un juego de fantasia.

def mostrarInventario(inventario):
    print("Inventario:")
    itemTotal = 0
    for k, v in inventario.items():
        print('%s %s' % (v,k))
        itemTotal += v 
    print("Total numero de items: " + str(itemTotal))

def agregarInventario(inventario, elementosAgregados):
    for item in elementosAgregados:
        if item not in inventario.values():
            inventario.setdefault(item,0)
        inventario[item] += 1
    return inventario



cosas = {'cuerda': 1, 'antorcha': 6, 'moneda de oro': 42, 'daga': 1, 'flecha': 12}
mostrarInventario(cosas)


inv = {'moneda de oro': 42, 'cuerda': 1}
dragonGanancia = ['moneda de oro', 'daga', 'moneda de oro', 'moneda de oro', 'rubi']
inv = agregarInventario(inv, dragonGanancia)
mostrarInventario(inv)