from abc import ABC, abstractmethod


class BinaryTreeADT(ABC):
    @abstractmethod
    def insert(self, data):
        """Insere elemento na árvore"""
        pass

    @abstractmethod
    def empty(self):
        """Verifica se a árvore está vazia"""
        pass

    @abstractmethod
    def root(self):
        """Retorna a raíz da árvore"""
        pass


class Node:
    def __init__(self, data=None, parent=None, left=None, right=None):
        self._data = data
        self._parent = parent
        self._left = left
        self._right = right

    def printNode(self):
        print(self._data)


class BinaryTree(BinaryTreeADT):
    def __init__(self, data=None):
        self._root = Node(data)

    def insert(self, data, _node=None):
        if self.empty():
            self._root = Node(data)
        else:
            if not _node:
                _node = self.root()
            if _node._data >= data:
                if not _node._left:
                    _node._left = Node(data)
                else:
                    self.insert(data, _node._left)
            else:
                if not _node._right:
                    _node._right = Node(data)
                else:
                    self.insert(data, _node._right)

    def empty(self):
        if self._root._data is None:
            return True
        return False

    def root(self):
        if not self.empty():
            return self._root
        return False

    def inOrderTraverse(self, node=None, lista=list()):
        if node is None:
            node = self.root()
        if node._left:
            self.inOrderTraverse(node._left, lista)
        lista.append(node._data)
        if node._right:
            self.inOrderTraverse(node._right, lista)
        return lista

    def preOrderTraverse(self, node=None, lista=list()):
        if node is None:
            node = self.root()
        lista.append(node._data)
        if node._left:
            self.preOrderTraverse(node._left, lista)
        if node._right:
            self.preOrderTraverse(node._right, lista)
        return lista

    def postOrderTraverse(self, node=None, lista=list()):
        if node is None:
            node = self.root()
        if node._left:
            self.postOrderTraverse(node._left, lista)
        if node._right:
            self.postOrderTraverse(node._right, lista)
        lista.append(node._data)
        return lista


if __name__ == '__main__':
    bt = BinaryTree(2)
    bt.insert(3)
    bt.insert(7)
    bt.insert(12)
    bt.insert(5)
    bt.insert(2)
    bt.insert(6)
    bt.insert(1)
    print(bt.inOrderTraverse())
    print(bt.preOrderTraverse())
    print(bt.postOrderTraverse())
