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
        if self._prev._data == None:
            return self._data.__str__()
        else:
            return '-' + self._data.__str__()


class DoublyLinkedList:
    def __init__(self, head=None):
        self._header = Node()
        self._trailer = Node()
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._length = 0

    def insert(self, index, data):
        idx = 0
        curr = self._header
        while curr is not self._trailer:
            if idx == index:
                newNode = Node(data, curr, curr._next)
                curr._next._prev = newNode
                curr._next = newNode
            idx += 1
            curr = curr._next
        self._length += 1

    def count(self, data):
        if not self.empty():
            counter = 0
            curr = self._header._next
            while curr is not self._trailer:
                if curr._data == data:
                    counter += 1
                curr = curr._next
        return counter

    def clear(self):
        self._header._next = None
        self._trailer._prev = None
        self._length = 0

    def index(self, data):
        result = None
        idx = 0
        curr = self._header._next
        while not result and curr is not self._trailer:
            if curr._data == data:
                result = idx
            curr = curr._next
            idx += 1
        return result

    def length(self):
        print(self._length)
        return self._length

    def empty(self):
        return self._length == 0

    def append(self, data):
        newNode = Node(data, self._trailer._prev, self._trailer)
        self._trailer._prev._next = newNode
        self._trailer._prev = newNode
        self._length += 1
        return newNode

    def remove_all(self, data):
        curr = self._header._next
        while curr is not self._trailer:
            if curr._data == data:
                curr._prev._next = curr._next
                curr._next._prev = curr._prev
            curr = curr._next
        self._length -= 1

    def remove_at(self, index):
        idx = 0
        curr = self._header._next
        while curr is not self._trailer:
            if idx == index:
                curr._prev._next = curr._next
                curr._next._prev = curr._prev
            idx += 1
            curr = curr._next
        self._length -= 1

    def replace(self, index, data):
        idx = 0
        curr  = self._header._next
        while curr is not self._trailer:
            if idx == index:
                curr._data = data
            idx += 1
            curr = curr._next

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
            return '- -'

if __name__ == '__main__':
    dll = DoublyLinkedList()
    dll.append(12)
    dll.append(5)
    dll.append(8)
    print(dll)