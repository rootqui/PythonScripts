# Script que hace una animacion de zigzag
import time, sys
def linea(espacio):
    print(' '*espacio+'*'*8)

def animacion():
    contador = 4
    cambioDireccion = True
    while True:
        time.sleep(0.1)
        if cambioDireccion and contador > 0:
            contador -= 1
        else:
            cambioDireccion = False if contador != 4 else True
            contador += 1
        linea(contador)
try:
    animacion()
except KeyboardInterrupt:
    print('\r'+ ' '*2)
    sys.exit()
