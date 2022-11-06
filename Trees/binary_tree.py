class Node:
    def __init__(self, data=None, parent=None, left=None, right=None):
        self._data = data
        self._parent = parent
        self._left = left
        self._right = right

    def printNode(self):
        print(self._data)


class BinaryTree:
    def __init__(self, data=None):
        self._root = Node(data)

    def insert(self, data, _node=None):
        _node = self._root
        if _node is None:
            _node = Node(data)
        elif data < _node._data:
            if _node._left:
                self.insert(self,data,_node._left)
            else:
                _node._left = Node(data)
        elif data > _node._data:
            if _node._right:
                self.insert(self, data, _node._right)
            else:
                _node._right = Node(data)


if __name__ == '__main__':
    bt = BinaryTree(2)
    bt.insert(3)
    print(bt)