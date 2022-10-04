class Node:
    def __init__(self, data=None, next=None):
        self._data = data
        self._next = next

class Queue_With_Node:
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0

    def __repr__(self):
        if self._size > 0:
            r = ""
            aux = self.first
            while(aux):
                r = r + str(aux._data) + " "
                aux = aux._next
            return r
        raise Exception('The list is empty!')

    def __str__(self):
        return self.__repr__()

    def __len__(self):
        return self._size

    def enqueue(self, elem):
        node = Node(elem)
        if self._size == 0:
            self.first = node
            self.last = node
        else:
            self.last._next = node
            self.last = node
        self._size += 1

    def dequeue(self):
        if self.__len__() > 0:
            self.first = self.first._next
            self._size -= 1
        else:
            raise Exception('The list is empty!')

    def get_first(self):
        if self._size > 0:
            elem = self.first._data
            return elem
        raise Exception('The list is empty!')

    def is_empty(self):
        if self.__len__() == 0:
            return True
        return False


if __name__ == '__main__':
    q = Queue_With_Node()
    q.enqueue(27)
    q.enqueue(4)
    print(q)
    print(q._size)
    q.dequeue()
    print(q)
    q.enqueue(30)
    print(q)
    print(q.get_first())