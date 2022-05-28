# Este es un juego de consola para adivinar el numero 

import random

numeroSecreto = random.randint(1,20)

print('Estoy pensando un numero entre 1 y 20')

#El jugador solo tiene 6 intentos
for intento in range(1,7):
    print('Adivina el numero')
    numero = int(input())
    if numero < numeroSecreto:
        print('Tu numero es muy bajo.')
    elif numero > numeroSecreto:
        print('Tu numero es muy alto.')
    else:
        break

if numero == numeroSecreto:
    print('Felicitaciones. Adivinaste mi numero en %s intentos' % intento)

else:
    print('Lo siento. El numero que estaba pensando es %s' % numeroSecreto)


