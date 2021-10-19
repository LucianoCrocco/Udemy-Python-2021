def mostarNumeros(numero):
    if numero > 0:
        print(numero)
        mostarNumeros(numero-1)


mostarNumeros(9)
