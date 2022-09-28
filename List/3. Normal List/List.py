from abc import ABC, abstractmethod


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


class MyList(ListADT):

    def __init__(self):
        self._data = list()
        self._length = 0

    def insert(self, indice, elemento):
        self._data.insert(indice, elemento)
        self._length = self._length + 1

    def remove(self, elemento):
        self._data.remove(elemento)
        self._length -= 1

    def count(self, elemento):
        return self._data.count(elemento)

    def clear(self):
        self._data = list()
        self._length = 0

    def index(self, elemento):
        return self._data.index(elemento)

    def length(self):
        return self._length

    def length2(self):
        return len(self._data)

    def __str__(self):
        return self._data.__str__()

    def remove_all(self, elemento):
        for i in self:
            if self.index(i) == elemento:
                self._data.remove(elemento)

    def __iter__(self):
        return self._data.__iter__()


if __name__ == '__main__':
    l = MyList()
    l.insert(0, 0)
    l.insert(1, 1)
    l.insert(1, 2)
    l.insert(20, 3)
    l.insert(0, 4)
    print(l)