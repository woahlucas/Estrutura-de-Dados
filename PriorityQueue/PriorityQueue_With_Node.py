class Node:
    def __init__(self, key=None, data=None):
        self._key = key
        self._data = data

    def __repr__(self):
        return '(' + str(self._data) + ', ' + str(self._key) + ')'


class PriorityQueueWithNode:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def __str__(self):
        return str(self.data)

    def is_empty(self):
        return self.data == []

    def add(self, key, value):
        elem = Node(key, value)
        self.data.append(elem)

    def min(self):
        pos = 0
        min = self.data[pos]._key
        for i in range(self.__len__()):
            if self.data[i]._key < min:
                pos = i
                min = self.data[i]._key
        return pos

    def remove_min(self):
        if self.is_empty():
            raise Exception('The list is empty!')
        self.data.pop(self.min())


if __name__ == '__main__':
    pq = PriorityQueueWithNode()
    pq.add(2, 'Ana')
    pq.add(1, 'Paulo')
    pq.add(1, 'Gabriel')
    print(pq)
    pq.remove_min()
    print(pq)
    print(pq.is_empty())

