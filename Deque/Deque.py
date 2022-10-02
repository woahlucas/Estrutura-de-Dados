from abc import ABC, abstractmethod


class Deque(ABC):

    @abstractmethod
    def add_first(self, elem):
        pass

    @abstractmethod
    def add_last(self, elem):
        pass

    @abstractmethod
    def remove_first(self):
        pass

    @abstractmethod
    def remove_last(self):
        pass

    @abstractmethod
    def first(self):
        pass

    @abstractmethod
    def last(self):
        pass

    @abstractmethod
    def is_empty(self):
        pass


class MyDeque(Deque):

    def __init__(self):
        self.data = []

    def __str__(self):
        return str(self.data)

    def __len__(self):
        return len(self.data)

    def add_first(self, elem):
        self.data.insert(0, elem)

    def add_last(self, elem):
        self.data.append(elem)

    def remove_first(self):
        self.data.pop(0)

    def remove_last(self):
        self.data.pop()

    def first(self):
        return self.data[0]

    def last(self):
        return self.data[-1]

    def is_empty(self):
        if self.data.__len__() == 0:
            return True
        return False


if __name__ == '__main__':
    dq = MyDeque()
    dq.add_first(2)
    dq.add_first(4)
    dq.add_first(7)
    dq.add_last(27)
    dq.remove_last()
    print(dq)
    print(dq.first())
