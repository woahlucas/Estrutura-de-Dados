# Write a Python program to simulate an ecosystem containing two types of creatures, bears and fish.
# The ecosystem consists of a river, which is modeled as a relatively large list. Each element of the list
# should be a Bear object, a Fish object, or None. In each time step, based on a random process, each animal either
# attempts to move into an adjacent list location or stay where it is. If two animals of the same type are about to
# collide in the same cell, then they stay where they are, but they create a new instance of that type of animal,
# which is placed in a random empty (i.e., previously None) location in the list. If a bear and a fish collide,
# however, then the fish died (i.e., it disappears).
import random
from collections import Counter


class Urso:
    def __init__(self):
        print()

    def __repr__(self):
        return 'Urso'


class Peixe:
    def __init__(self):
        print()

    def __repr__(self):
        return 'Peixe'


class Rio:
    def __init__(self):
        self.comprimentoRio = 5  # comprimento do Rio
        self.rio=[]  # inicializa o rio como uma lista vazia

    def __repr__(self):
        return str([i for i in self.rio])

    def popular_rio(self):
        self.rio=[random.choice([Urso(),Peixe(),None]) for i in range(0,self.comprimentoRio)]  # popula o rio

    def prox_iteracao(self, n=1):
        for i in range(n):
            index_atual = random.choice(list(range(self.comprimentoRio)))  # escolhe uma posição aleatória para se mover
            destino = random.choice([-1, 1])  # escolhe o destino (esquerda ou direita)
            if self.rio[index_atual] is None:  # posição None não se move
                pass
            else:
                index_novo = index_atual+destino  # define a nova posição
                print(self.rio[index_atual], "vai para", "esquerda" if destino == -1 else "direita")
                if index_novo < 0 or index_novo > len(self.rio) - 1:  # valores de fora da lista não são válidos
                    pass
                elif isinstance(self.rio[index_atual], Urso):  # se a posição escolhida aleatoriamente for um urso
                    if isinstance(self.rio[index_novo], Urso):  # se encontrar um urso
                        cont = self.rio.count(None)  # verifica se existe posição vazia na lista
                        if cont > 1:
                            self.rio.pop(self.rio.index(None))  # remove o None
                            self.rio.insert(self.rio.index(None), Urso())  # adiciona outro Urso
                    elif isinstance(self.rio[index_novo], Peixe):  # se a posição de destino for um peixe
                        self.rio[index_novo] = Urso()  # substitui por um urso
                        self.rio[index_atual] = None  # antiga posição fica vazia
                    else:  # se a posição de destino for vazia
                        self.rio[index_atual] = None  # a posição antiga fica vazia
                        self.rio[index_novo] = Urso()  # o Urso ocupa a posição de destino
                elif isinstance(self.rio[index_atual], Peixe):  # se a posição escolhida aleatoriamente for um peixe
                    if isinstance(self.rio[index_novo], Peixe):  # se encontrar um peixe
                        cont2 = self.rio.count(None)  # verifica se existe posição vazia na lista
                        if cont2 > 1:
                            self.rio.pop(self.rio.index(None))  # remove o None
                            self.rio.insert(self.rio.index(None), Peixe())  # adiciona outro peixe
                    elif isinstance(self.rio[index_novo], Urso):  # se a posição de destino for um urso
                        self.rio[index_atual] = None  # o peixe morre
                    else:  # se a posição escolhida for vazia
                        self.rio[index_atual] = None  # a posição antiga fica vazia
                        self.rio[index_novo] = Peixe()  # o peixe ocupa a posição de destino
                print(self.rio)

    def mostrar(self):
        print("Estado final")
        print(self.rio)


r = Rio()
r.popular_rio()
print("Estado inicial:")
print(r)
r.prox_iteracao(20)
r.mostrar()