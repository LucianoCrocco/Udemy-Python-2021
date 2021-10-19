def calcularFactorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * calcularFactorial(numero-1)



resultado = calcularFactorial(5)
print(resultado)

