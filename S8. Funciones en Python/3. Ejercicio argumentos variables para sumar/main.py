def sumarValores(*args):
    acumulador = 0
    for i in args:
        acumulador += i
    return acumulador



resultado = sumarValores(9,5,10)

print(resultado)
