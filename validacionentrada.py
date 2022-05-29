#Script de practica para la validar si el dato ingresado es un numero
def validarNumero(numero):
    try:
        if numero.replace('-','',1).isnumeric():
            numero = int(numero)
        elif numero.replace('-','',1).replace('.','',1).isnumeric():
            numero = float(numero)
        else:
            raise ValueError

        return numero
    except ValueError:
        print('El valor debe ser un numero')

#Prueba de la funcion validarNumero()
lista = ['a','1','-1.2','-2','3.3','--2','--4.4','!@#','4.2.2','--4..1']

for i in lista:
    print(validarNumero(i))
