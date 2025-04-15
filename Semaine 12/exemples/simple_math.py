# simple_math.py

class SimpleMath:

    def __init__(self, base):
        self.base = base

    @staticmethod
    def somme(a, b):
        return a + b

    @staticmethod
    def soustraction(a, b):
        return a - b

    @staticmethod
    def somme_liste(data):
        total = 0
        for x in data:
            total += x
        return total

    def conversion_base_10(self, nombre: int):

        if self.base > 10 or self.base < 2:
            raise ValueError("La base doit être entre 2 et 10")
        exp = 0
        total = 0
        for x in reversed(str(nombre)):
            if int(x) >= self.base:
                raise ValueError("Le nombre ne peut pas être converti dans cette base")
            total += int(x) * (self.base ** exp)
            exp += 1
        return total

    @staticmethod
    def division(a, b):
        if b == 0:
            raise ValueError("Division par zéro")
        return a / b
