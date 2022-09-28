from abc import ABC, abstractmethod


class QueueEd(ABC):

    @abstractmethod
    def enqueue(self, elem):
        """Enfileira <elemento>"""
        pass

    @abstractmethod
    def dequeue(self):
        """Desenfileira elemento da pilha"""
        pass

    @abstractmethod
    def first(self):
        """Verifica qual é o elemento que se encontra no início da fila, sem removê-lo"""
        pass

    @abstractmethod
    def is_empty(self):
        """Verifica se a fila está vazia"""
        pass


class MyQueue(QueueEd):
    def __init__(self):
        self.data = []

    def __str__(self):
        return str(self.data)

    def enqueue(self, elem):
        self.data.append(elem)

    def dequeue(self):
        if self.data.__len__() != 0:
            self.data.pop(0)
        else:
            raise Exception('The list is empty!')

    def first(self):
        if self.data.__len__() != 0:
            return self.data[0]
        else:
            raise Exception('The list is empty!')

    def is_empty(self):
        if self.data.__len__() == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    q = MyQueue()
    q.enqueue(2)
    q.enqueue(4)
    print(q)
    q.dequeue()
    print(q)
