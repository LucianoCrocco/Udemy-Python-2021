class Aritmetica:
    """
    Clase Arimetica para realizar las operaciones de restar, sumar, etc.
    """
    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    def sumar(self):
        return self.operandoA + self.operandoB

    def restar(self):
        return self.operandoA - self.operandoB

    def multiplicar(self):
        return self.operandoA * self.operandoB

    def dividir(self):
        return self.operandoA / self.operandoB


aritmetica = Aritmetica(6, 3)
print(f"Suma: {aritmetica.sumar()}")
print(f"Resta: {aritmetica.restar()}")
print(f"Multiplicacion: {aritmetica.multiplicar()}")
print(f"Division: {aritmetica.dividir():.2f}")

