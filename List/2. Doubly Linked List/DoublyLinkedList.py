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


class Node:
    def __init__(self, data=None, prev=None, next=None):
        self._data = data
        self._prev = prev
        self._next = next

    def __str__(self):
        if not self._next:
            return '|' + self._data.__str__() + '|'
        else:
            return '|' + self._data.__str__()


class DoublyLinkedList:
    def __init__(self, head=None):
        self._header = Node()
        self._trailer = Node()
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def length(self):
        print(self._size)
        return self._size

    def empty(self):
        return self._size == 0

    def append(self, data):
        newNode = Node()
        newNode._data = data
        newNode._prev = self._trailer._prev
        newNode._next = self._trailer
        self._trailer._prev._next = newNode
        self._trailer._prev = newNode
        self._size += 1
        return newNode

    def __str__(self):
        if not self.empty():
            result = ''
            aux = self._header._next
            result += aux.__str__()
            while aux._next != self._trailer:
                aux = aux._next
                result += aux.__str__()
            return result
        else:
            return '||'

if __name__ == '__main__':
    dll = DoublyLinkedList()
    dll.append(12)
    dll.append(5)
    dll.append(8)
    print(dll)