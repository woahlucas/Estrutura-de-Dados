from enum import IntEnum, unique
from abc import ABC, abstractmethod
import random


class ListADT(ABC):

    @abstractmethod
    def insert(self, indice, elemento):
        """Insere <elemento> na posição <indice>"""
        pass

    @abstractmethod
    def remove(self, elemento):
        """Remove primeira ocorrência de <elemento>"""
        pass

    @abstractmethod
    def count(self, elemento):
        """Conta a quantidade de <elemento> na lista"""
        pass

    @abstractmethod
    def clear(self):
        """Apaga a lista"""
        pass

    @abstractmethod
    def index(self, elemento):
        """Retorna o primeiro índice de <elemento>"""
        pass

    @abstractmethod
    def length(self):
        """Retorna o tamanho da lista"""
        pass


class DoublyLinkedList(ListADT):
    class _DoublyNode:

        def __init__(self, elem, prev, next):
            self._elem = elem
            self._prev = prev
            self._next = next

        def __str__(self):
            if self._elem is not None:
                return str(self._elem) + ' '
            else:
                return '|'

    def __init__(self, tamanho=0):
        self._header = self._DoublyNode(None, None, None)
        self._trailer = self._DoublyNode(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._length = 0
        if tamanho:
            for i in range(tamanho):
                self.insert(i, None)

    def insert(self, index, elem):
        if index >= self._length:  # se o indice se inserção passado for maior que a lista
            index = self._length  # atualiza para o último indice
        if self.empty():  # Caso da lista vazia
            new_node = self._DoublyNode(elem, self._header, self._trailer)
            self._header._next = new_node
            self._trailer._prev = new_node
        elif index == 0:  # caso da inserção na primeira posição da lista
            new_node = self._DoublyNode(elem, self._header, self._header._next)
            self._header._next._prev = new_node
            self._header._next = new_node
        else:  # outros casos de inserção
            this = self._header._next
            successor = this._next
            pos = 0
            while pos < index - 1:
                this = successor
                successor = this._next
                pos += 1
            new_node = self._DoublyNode(elem, this, successor)
            this._next = new_node
            successor._prev = new_node

        self._length += 1

    def remove(self, elemento):
        if not self.empty():
            node = self._header._next
            pos = 0
            found = False
            while not found and pos < self._length:
                if node._elem == elemento:
                    found = True
                else:
                    node = node._next
                    pos += 1
            if found:
                node._prev._next = node._next
                node._next._prev = node._prev
                self._length -= 1

    def count(self, elem):
        result = 0
        this = self._header._next
        if self._length > 0:
            while this._next is not None:  # aqui a lista é percorrida
                if this._elem == elem:
                    result += 1
                this = this._next
        return result

    def clear(self):
        self._header = self._DoublyNode(None, None, None)
        self._trailer = self._DoublyNode(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._length = 0

    def index(self, elem):
        result = None  # armazena a primeira posição do elemento
        pos = 0
        aux = self._header._next
        # Vamos percorrer a lista em busca de elem
        while not result and pos < self._length:  # lembrando que not None é o mesmo que True
            if aux._elem is elem:
                result = pos
            aux = aux._next
            pos += 1
        return result  # se o elemento não estiver na lista, retorna None

    def length(self):
        return self._length

    def empty(self):
        return self._length == 0

    def element_at(self, index):
        if not self.empty() and index < self._length:
            node = self._header._next
            for i in range(index):
                node = node._next
            return node._elem

    def replace_at(self, index, elem):
        if not self.empty() and index < self._length:
            node = self._header._next
            for i in range(index):
                node = node._next
            node._elem = elem

    def __len__(self):
        return self._length

    def __str__(self):
        if not self.empty():
            result = ''
            aux = self._header
            result += aux.__str__()
            while aux._next:
                aux = aux._next
                result += aux.__str__()
            return result
        else:
            return '||'


def gerador_numero(maximo, minimo=0):
    """Função que gera um número entre dois limites"""
    return random.randrange(minimo, maximo)


@unique
class Direcao(IntEnum):
    ESQUERDA = -1
    DIREITA = 1
    PARADO = 0


class Rio:
    """Classe que modela e implementa o comportamento do rio"""

    def __init__(self, tamanho=100):
        self.__rio = DoublyLinkedList(tamanho)
        self.__inicio_do_mundo()

    def __inicio_do_mundo(self):
        """Método privado para inicializar o mundo"""
        qtd_peixe = round(len(self.__rio) * 0.2)
        qtd_urso = round(len(self.__rio) * 0.4)
        self.__gerar_animal(qtd_peixe, Peixe)
        self.__gerar_animal(qtd_urso, Urso)

    def __gerar_animal(self, qtd, classe):
        bicho = 0
        while bicho < qtd:
            indice = gerador_numero(len(self.__rio))
            if not self.__rio.element_at(indice):
                self.__rio.insert(indice, classe())
                bicho += 1

    def fluir(self):
        iteracao = 0
        while iteracao < 5:
            for i in range(len(self.__rio)):
                if self.__rio.element_at(i):
                    a = self.__rio.element_at(i)
                    pos = a.andar()
                    if 0 <= pos + i < len(self.__rio) and pos + i != i:
                        # testar mecânicas diferentes de andar
                        if self.__rio.element_at(pos + i):
                            if isinstance(a, Urso):
                                self.__movimento_urso(a, i, pos + i)
                            elif isinstance(a, Peixe):
                                if a.reproduzir(self.__rio.element_at(pos + i)):
                                    self.__gerar_animal(1, Peixe)
                                else:
                                    self.__rio.replace_at(i, None)
                        else:
                            # efetivamente ando aqui!!!
                            self.__rio.replace_at(pos + i, self.__rio.element_at(i))
                            self.__rio.replace_at(i, None)
            iteracao += 1

    def __movimento_urso(self, a, atual, seguinte):
        elem_outra_posicao = self.__rio.element_at(seguinte)
        if isinstance(elem_outra_posicao, Urso):
            if a.reproduzir(self.__rio.element_at(seguinte)):
                self.__gerar_animal(1, Urso)
            else:
                a.brigar(elem_outra_posicao)
                if not a.get_forca():
                    self.__rio.replace_at(atual, None)
                elif not elem_outra_posicao.get_forca():
                    self.__rio.replace_at(seguinte, None)

        elif a.comer(elem_outra_posicao):
            self.__rio.replace_at(seguinte, None)

    def __movimento_peixe(self, animal, new_pos, old_pos):
        if animal.reproduzir(self.__rio[new_pos]):
            self.__gerar_animal(1, Peixe)
        else:
            self.__rio[old_pos] = None

    def __str__(self):
        s = '| '
        for i in range(len(self.__rio)):
            s = s + self.__rio.element_at(i).__str__() + ' |'
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


class Peixe(Animal):

    def andar(self):
        return gerador_numero(Direcao.DIREITA + 1, Direcao.ESQUERDA)

    def comer(self, animal):
        return False

    def reproduzir(self, animal):
        result = False
        if isinstance(animal, Peixe):
            result = True
        return result

    def __str__(self):
        return 'Peixe'


class Urso(Animal):

    def __init__(self):
        self._forca = gerador_numero(7, 4)
        self._fome = []

    def andar(self):
        return gerador_numero(Direcao.DIREITA + 1, Direcao.ESQUERDA)

    def comer(self, animal):
        result = False
        if isinstance(animal, Peixe):
            result = True
        return result

    def reproduzir(self, animal):
        result = False
        if isinstance(animal, Urso) and self.get_forca() == animal.get_forca():
            result = True
        return result

    def brigar(self, urso):
        if isinstance(urso, Urso):
            if self.get_forca() > urso.get_forca():
                self.set_forca(self.get_forca() + 1)
                urso.set_forca(urso.get_forca() - 1)
            elif urso.get_forca() > self.get_forca():
                self.set_forca(self.get_forca() - 1)
                urso.set_forca(urso.get_forca() + 1)

    def get_forca(self):
        return self._forca

    def set_forca(self, forca):
        self._forca = forca

    def __str__(self):
        return 'Urso'


if __name__ == '__main__':
    r = Rio(15)
    print(r)
    r.fluir()
    print(r)
