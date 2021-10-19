# Adicion +
# Sustraccion -
# Multiplitacion *
# Division /
# Division de Enteros //
# Exponencial **
# Modulo/Resto %

operandoUno = 3
operandoDos = 2

suma = operandoUno + operandoDos

# print("Suma:", suma)
print(f"Resultado suma: {suma}") # A esto se le llama interpolacion (incluir variables ne una cadena)
# La f dentro del print significa format

resta = operandoUno - operandoDos
print(f"Resultado de la resta: {resta}")

multiplicacion = operandoUno * operandoDos
print(f"Resultado de la multiplicacion: {multiplicacion}")

division = operandoUno / operandoDos
print(f"Resultado de la division: {division}")

# Si no queremos un resultado de division flotante
divisionEntero = operandoUno // operandoDos
print(f"Resultado de la division sin flotante: {divisionEntero}")

exponencial = operandoUno ** operandoDos
print(f"Resultado de {operandoUno} elevado a la {operandoDos} es: {exponencial}")

resto = operandoUno % operandoDos
print(f"Resultado del modulo/resto de la division es : {resto}")