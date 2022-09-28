# Manual solution

def reverseList(list):
    length = len(list)-1
    reversed_list = []
    for i in range(length+1):
        reversed_list.append(list[length-i])
    return reversed_list

list1 = [100, 200, 300, 400, 500]
print(list1)
print(reverseList(list1))

 # Reverse function
list2 = [5, 16, 20, 36]
print(list2)
list2.reverse()
print(list2)

# Negative slicing
list3 = [9, 18, 27]
print(list3)
list3 = list3[::-1]
print(list3)
