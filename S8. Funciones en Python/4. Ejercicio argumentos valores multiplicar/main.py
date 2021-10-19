def multiplicarValores(*args):
    resultado = 1
    for i in args:
        resultado *= i
    return resultado


print(multiplicarValores(1, 2, 3))