#Script de la secuencia de Collatz 
#Si el numero es par, la funcion collatz() imprime el numero/2 y devuelve este valor.
#Si el numero es impar, retorna el valor (numero*3) + 1
import sys
def collatz(numero):
    print(numero)
    if numero == 1:
        return
   
    if numero%2 == 0:
        collatz(numero // 2)
    else:
        collatz(3*numero + 1)


try:
    valorNumerico = False
    while not valorNumerico:
        print('Ingrese un numero:')
        n = input()
        valorNumerico = n.isnumeric()

    n = int(n)
    print('La secuencia de Collatz para %s es:' % n)
    collatz(n)
except KeyboardInterrupt:
    print('\r'+' '*2)
    sys.exit()
