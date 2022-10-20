def bubble_sort(arranjo):
    n = len(arranjo)
    for i in range(n):  # todos os elementos de arranjo
        for j in range(0, n - i - 1):  # até onde não estiver ordenado
            if arranjo[j] > arranjo[j + 1]: \
                    # arranjo[j], arranjo[j+1] = arranjo[j+1], arranjo[j]
                aux = arranjo[j]
                arranjo[j] = arranjo[j + 1]
                arranjo[j + 1] = aux


def insertion_sort(arranjo):
    for i in range(1, len(arranjo)):
        valor = arranjo[i]
        j = i
        while j > 0 and arranjo[j - 1] > valor:
            arranjo[j] = arranjo[j - 1]
            j -= 1
        arranjo[j] = valor


def selection_sort(arranjo):
    for i in range(len(arranjo)):
        min_index = i
        for j in range(i + 1, len(arranjo)):
            if arranjo[j] < arranjo[min_index]:
                min_index = j

        if arranjo[min_index] != arranjo[i]:
            arranjo[i], arranjo[min_index] = arranjo[min_index], arranjo[i]


def search(e, arranjo):
    found = False
    selection_sort(arranjo)
    if arranjo.count(e):
        while not found:
            meio = arranjo[int((len(arranjo)) / 2)]
            if e > meio:
                arranjo = arranjo[arranjo.index(meio):]
            elif e < meio:
                arranjo = arranjo[:arranjo.index(meio)]
            elif e == meio:
                print('Elemento encontrado! O elemento é: ', e)
                found = True
    else:
        print('O elemento não existe na lista')

    # selection_sort(arranjo)
    # meio = int((len(arranjo))/2)
    # print(arranjo)
    # print(arranjo[meio])
    # if e > arranjo[meio]:
    #     arranjo = arranjo[arranjo[meio]:arranjo[len(arranjo)-1]]
    #     meio = int((len(arranjo)) / 2)
    #     print(arranjo)
    #     print(arranjo[meio])
    #     if e > arranjo[meio]:
    #         arranjo = arranjo[arranjo[meio]:arranjo[len(arranjo) - 1]]
    #         meio = int((len(arranjo)) / 2)
    #         print(arranjo)
    #         print(meio)



if __name__ == '__main__':
    # l = [6, 5, 4, 3, 2, 1]
    # bubble_sort(l)
    # print(l)

    # l = [6, 5, 4, 3, 2, 1]
    # insertion_sort(l)
    # print(l)

    # l = [6, 5, 4, 3, 2, 1]
    # selection_sort(l)
    # print(l)

    l = [6, 5, 4, 3, 2]
    search(6, l)
