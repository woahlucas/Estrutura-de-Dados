from abc import ABC, abstractmethod


class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass


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


class MyStack(Stack):
    def __init__(self):
        self.data = []

    def __str__(self):
        return str(self.data)

    def __len__(self):
        return len(self.data)

    def push(self, data):
        self.data.append(data)

    def pop(self):
        if self.is_empty():
            raise Empty('The stack is empty!')
        self.data.pop()

    def top(self):
        if self.is_empty():
            raise Empty('The stack is empty!')
        return self.data[-1]

    def is_empty(self):
        if self.data.__len__() == 0:
            return True
        return False


def reverse(s):
    """Method for reversing a stack"""
    aux = MyStack()
    i = 0
    for c in range(s.__len__()):
        popped = s.top()
        s.pop()
        aux.push(popped)
    while i < aux.__len__():
        s.push(aux.data[i])
        i += 1
    return s


def matches(expression):
    """Check for balanced delimiters in expressions"""
    left = '({['
    right = ')}]'
    S = MyStack()
    for c in expression:
        if c in left:
            S.push(c)
        elif c in right:
            pos = right.index(c)
            if not S.is_empty() and left[pos] == S.data[S.__len__() - 1]:
                S.pop()
            else:
                return "Unbalanced"
    if S.is_empty():
        return "Balanced"
    else:
        return "Unbalanced"


if __name__ == '__main__':
    st = MyStack()
    st.push(4)
    st.push(24)
    st.push(6)
    print(st)
    reverse(st)
    print(st)
    print(matches('(5+[2+2])'))
