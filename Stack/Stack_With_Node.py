from abc import ABC, abstractmethod


class Stack(ABC):

    @abstractmethod
    def push(self, elem):
        """Empilha <elemento>"""
        pass

    @abstractmethod
    def pop(self):
        """Desempilha elemento da pilha"""
        pass

    @abstractmethod
    def top(self):
        """Verifica qual é o elemento que se encontra no topo da pilha, sem removê-lo"""
        pass

    @abstractmethod
    def is_empty(self):
        """Verifica se a pilha está vazia"""
        pass


class Node:
    def __init__(self, data=None, next=None):
        self._data = data
        self._next = next


class Stack_With_Node(Stack):
    def __init__(self, head=None):
        self._top = None
        self._size = 0

    def __len__(self):
        return self._size

    def push(self, data):
        node = Node(data)
        node._next = self._top
        self._top = node
        self._size += 1

    def pop(self):
        if self._size > 0:
            node = self._top
            self._top = self._top._next
            self._size -= 1
            return node._data
        raise IndexError("The stack is empty")

    def top(self):
        if self._size > 0:
            return self._top._data
        raise IndexError("The stack is empty")

    def is_empty(self):
        return self._size == 0

    def __repr__(self):
        r = ""
        aux = self._top
        while (aux):
            r = r + str(aux._data) + "\n"
            aux = aux._next
        return r

    def __str__(self):
        return self.__repr__()


if __name__ == '__main__':
    s = Stack_With_Node()
    s.push(2)
    s.push(24)
    s.push('Oi')
    print(s)
