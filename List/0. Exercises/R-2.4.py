# Write a Python class, Flower, that has three instance variables of type str,
# int, and float, that respectively represent the name of the flower, its num-
# ber of petals, and its price. Your class must include a constructor method
# that initializes each variable to an appropriate value, and your class should
# include methods for setting the value of each type, and retrieving the value
# of each type.


class Flower:
    def __init__(self):
        self.nome = str('Nome')
        self.petalas = int(0)
        self.preco = float(0.0)

    def set_nome(self, nome):
        self.nome = nome

    def set_petalas(self, petalas):
        self.petalas = petalas

    def set_preco(self, preco):
        self.preco = preco

    def get_nome(self):
        print(self.nome)
        return self.nome

    def get_petalas(self):
        print(self.petalas)
        return self.petalas

    def get_preco(self):
        print(self.preco)
        return self.preco


flor1 = Flower()
flor1.set_preco(5.99)
flor1.get_preco()