#Funcion para dividir entre cero con cualquier numero dado por el usuario

class DivisionCalculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def dividir(self):
        try:
            if self.num2 == 0:
                raise ZeroDivisionError("¡Error! No se puede dividir entre cero.")

            resultado = self.num1 / self.num2
            return resultado
        except ValueError:
            raise ValueError("Por favor, ingrese números válidos.")
        except ZeroDivisionError as error:
            raise ZeroDivisionError(error)

