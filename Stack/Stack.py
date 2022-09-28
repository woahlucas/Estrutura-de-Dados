from abc import ABC, abstractmethod


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

    def push(self,data):
        self.data.append(data)

    def pop(self):
        if self.__len__() > 0:
            self.data.pop()
        else:
            raise Exception('The list is empty!')

    def top(self):
        if self.__len__() > 0:
            return self.data[-1]
        else:
            raise Exception('The list is empty!')

    def is_empty(self):
        if self.__len__() == 0:
            return True
        else:
            return False

if __name__ == '__main__':
    st = MyStack()
    st.push(4)
    st.push(24)
    st.push(6)
    print(st)
    print(st.top())