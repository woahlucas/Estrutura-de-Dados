class Node:
    def __init__(self, data=None, next=None, prev=None):
        self._data = data
        self._next = next
        self._prev = prev


class Deque_With_Node():

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

    def add_first(self, elem):
        node = Node(elem)
        if self._size == 0:
            self.first = node
            self.last = node
        else:
            self.first._prev = node
            node._next = self.first
            self.first = node
        self._size += 1

    def add_last(self, elem):
        node = Node(elem)
        if self._size == 0:
            self.first = node
            self.last = node
        else:
            node._prev = self.last
            self.last._next = node
            self.last = node
        self._size += 1

    def remove_first(self):
        if self._size > 0:
            elem = self.first._data
            self.first = self.first._next
            self.first._prev = None
        else:
            raise Exception('The deque is empty!')
        self._size -= 1
        return elem

    def remove_last(self):
        if self._size > 0:
            elem = self.last._data
            self.last = self.last._prev
            self.last._next = None
        else:
            raise Exception('The deque is empty!')
        self._size -= 1
        return elem

    def get_first(self):
        if self._size > 0:
            return self.first._data
        raise Exception('The deque is empty!')

    def get_last(self):
        if self._size > 0:
            return self.last._data
        raise Exception('The deque is empty!')

    def is_empty(self):
        if self._size == 0:
            return True
        return False


if __name__ == '__main__':
    d = Deque_With_Node()
    d.add_first(2)
    print(d)
    d.add_first(4)
    print(d)
    d.add_last(6)
    print(d)
    d.remove_first()
    print(d)
    d.remove_last()
    print(d)
    d.add_last(1)
    d.add_last(2)
    d.add_last(3)
    d.remove_first()
    print(d)
    print(d.get_first())
