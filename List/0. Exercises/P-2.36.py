# Write a Python program to simulate an ecosystem containing two types of creatures, bears and fish.
# The ecosystem consists of a river, which is modeled as a relatively large list. Each element of the list
# should be a Bear object, a Fish object, or None. In each time step, based on a random process, each animal either
# attempts to move into an adjacent list location or stay where it is. If two animals of the same type are about to
# collide in the same cell, then they stay where they are, but they create a new instance of that type of animal,
# which is placed in a random empty (i.e., previously None) location in the list. If a bear and a fish collide,
# however, then the fish died (i.e., it disappears).

import random
from abc import ABC, abstractmethod


class Rio:
    def __init__(self, comprimento):
        self.comprimentoRio = comprimento  # comprimento do Rio
        self.rio = [None] * comprimento  # inicializa o rio como uma lista vazia
        self.inicio()

    def inicio(self):
        qtd_peixe = int(len(self.rio)*0.5)
        qtd_urso= int(len(self.rio) * 0.4)
        self.popular_rio(qtd_peixe, Peixe)
        self.popular_rio(qtd_urso, Urso)

    def popular_rio(self, qtd, tipo):
        num = 0
        while num < qtd:
            idx = random.randrange(0, self.comprimentoRio)
            if not self.rio[idx]:
                self.rio[idx] = tipo()
                num += 1

    def fluir(self):
        itr = 0
        while itr < 5:
            for i in range(len(self.rio)):
                if self.rio[i]:
                    a = self.rio[i]
                    pos = a.andar()
                    if 0 <= pos + i < len(self.rio) and pos + i != i:
                        if self.rio[pos + i]:
                            if isinstance(a, Urso):
                                self.movimentarUrso(a, pos, i)
                            elif isinstance(a, Peixe):
                                self.movimentarPeixe(a, pos, i)
                        else:
                            self.rio[pos + i] = self.rio[i]
                            self.rio[i] = None
            itr += 1

    def movimentarUrso(self, a, pos, i):
        if a.reproduzir(self.rio[pos + i]):
            cont = self.rio.count(None)
            if cont >= 1:
                self.rio[self.rio.index(None)] = Urso()
        elif a.comer(self.rio[pos + i]):
            self.rio[pos + i] = None

    def movimentarPeixe(self, a, pos, i):
        if a.reproduzir(self.rio[pos+i]):
            cont = self.rio.count(None)
            if cont >= 1:
                self.rio[self.rio.index(None)] = Urso()
        else:
            self.rio[i] = None

    def __str__(self):
        s = '| '
        for i in range(len(self.rio)):
            s = s + self.rio[i].__str__() + ' |'
        return s


class Animal(ABC):
    @abstractmethod
    def andar(self):
        pass

    @abstractmethod
    def comer(self, animal):
        pass

    @abstractmethod
    def reproduzir(self, animal):
        pass


class Urso:
    def andar(self):
        destino = random.choice([-1, 1])
        return destino

    def comer(self, animal):
        result = False
        if isinstance(animal, Peixe):
            result = True
        return result

    def reproduzir(self, animal):
        result = False
        if isinstance(animal, Urso):
            result = True
        return result

    def __repr__(self):
        return 'Urso'


class Peixe:
    def andar(self):
        destino = random.choice([-1, 1])
        return destino

    def comer(self, animal):
        return False

    def reproduzir(self, animal):
        result = False
        if isinstance(animal, Peixe):
            result = True
        return result

    def __repr__(self):
        return 'Peixe'


if __name__ == '__main__':
    r = Rio(5)
    print(r)
    r.fluir()
    print(r)