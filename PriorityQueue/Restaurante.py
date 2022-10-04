from abc import ABC, abstractmethod
import random


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
        if self.is_empty():
            raise Exception("Priority Queue is empty")
        k, v = self.data[0]
        for e in self.data:
            if e[0] < k:
                k, v = e[0], e[1]
        return k, v

    def remove_min(self):
        if self.is_empty():
            raise Exception("Priority Queue is empty")
        self.data.remove(self.min())

    def is_empty(self):
        if self.data.__len__() == 0:
            return True
        return False


class Restaurant:

    def __init__(self, no_of_tables):
        self.no_of_tables = no_of_tables
        self.queue = MyPriorityQueue()
        self.tables = []

    def __str__(self):
        return str(self.tables)

    def start_tables(self):
        for i in range(self.no_of_tables):
            t = (random.randint(2, 5), 'Empty')
            self.tables.append(t)

    def add_to_queue(self, k, v):
        self.queue.add(k, v)

    def add_to_table(self, k):  # TODO não pode adicionar se não estiver mais na lista
        for e in self.queue.data:
            if e[0] == k:
                t = (e[0], e[1])
                for i in range(len(self.tables)):
                    if self.tables[i][0] == k and self.tables[i][1] == 'Empty':
                        self.tables[i] = t


if __name__ == '__main__':
    r = Restaurant(10)
    r.start_tables()
    print(r)
    r.add_to_queue(3, 'Ana')
    r.add_to_queue(2, 'João')
    r.add_to_queue(3, 'Mariana')
    print(r.queue)
    r.add_to_table(2)
    print(r)
