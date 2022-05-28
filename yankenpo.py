# Este es un juego de consola de piedra, papel y tijera

import random, sys
print("PIEDRA, PAPEL, TIJERA")

victoria = 0
derrota = 0
empate = 0

while True:
    print('%s Victorias, %s Derrotas, %s Empates' % (victoria, derrota, empate))
    while True:
        print('Ingresa tu movimiento: (r)piedra (p)apel (t)ijera or (s)alir')
        jugador = input()
        if jugador == 's':
            sys.exit()
        if jugador == 'r' or jugador == 'p' or jugador == 't':
            break
        print('Escribe alguna de estas opciones r, p, t, s.')

    if jugador == 'r':
        print('PIEDRA versus...')
    elif jugador == 'p':
        print('PAPEL versus...')
    elif jugador == 't':
        print('TIJERA versus...')

    aleatorio = random.randint(1,3)

    if aleatorio == 1:
        bot = 'r'
        print('PIEDRA')
    elif aleatorio == 2:
        bot = 'p'
        print('PAPEL')
    elif aleatorio == 3:
        bot = 't'
        print('TIJERA')


    if  jugador == bot:
        empate = empate + 1 
        print('Esto es un empate.')
    elif jugador == 'r' and bot == 't':
        victoria = victoria + 1
        print('Ganaste.')
    elif jugador == 'p' and bot == 'r':
        victoria = victoria + 1
        print('Ganaste.')
    elif jugador == 't' and bot == 'p':
        victoria = victoria + 1
        print('Ganaste.')
    elif jugador == 'r' and bot == 'p':
        derrota = derrota + 1
        print('Perdiste.')
    elif jugador == 'p' and bot == 't':
        derrota = derrota + 1
        print('Perdiste.')
    elif jugador == 't' and bot == 'r':
        derrota = derrota + 1
        print('Perdiste.')
