def merge_sort(arranjo, inicio=0, fim=None):
    if fim is None:
        fim = len(arranjo)
    if (fim - inicio > 1):
        meio = (fim+inicio)//2
        print(meio)
        merge_sort(arranjo, inicio, meio)
        merge_sort(arranjo, meio, fim)
        merge(arranjo, inicio, meio, fim)
    return arranjo

def merge(arranjo, inicio, meio, fim):
    left = arranjo[inicio:meio]
    right = arranjo[meio:fim]
    i, j = 0, 0
    for k in range(inicio, fim):
        if i >= len(left):
            arranjo[k] = right[j]
            j += 1
        elif j >= len(right):
            arranjo[k] = left[i]
            i += 1
        elif left[i] < right[j]:
            arranjo[k] = left[i]
            i += 1
        else:
            arranjo[k] = right[j]
            j += 1

if __name__ == '__main__':
    lista = [3, 2, 1]
    print(merge_sort(lista))