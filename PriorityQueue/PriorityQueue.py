from abc import ABC, abstractmethod


class PriorityQueue(ABC):
    @abstractmethod
    def add(self, k, v):
        pass

    @abstractmethod
    def min(self):
        pass

    @abstractmethod
    def remove_min(self):
        pass

    @abstractmethod
    def is_empty(self):
        pass

    def len(self):
        pass


class Node:

    def __init__(self, data, priority):
        self.data = data
        self.priority = priority


class MyPriorityQueue(PriorityQueue):

    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def __str__(self):
        return str(self.data)

    def add(self, k, v):
        t = (k, v)
        self.data.append(t)

    def min(self):
        aux = 0
        for x in range(0, self.__len__()):
            if self.data[x][0] < self.data[aux][0]:
                aux = x
        return aux

    def remove_min(self):
        self.data.pop(self.min())
        # self.data.remove(self.data[self.min()])

    def is_empty(self):
        if self.data.__len__() == 0:
            return True
        return False


if __name__ == '__main__':
    pq = MyPriorityQueue()
    pq.add(5, 'A')
    pq.add(4, 'B')
    pq.add(3, 'C')
    pq.add(3, 'D')
    print(pq)
    pq.remove_min()
    print(pq)
