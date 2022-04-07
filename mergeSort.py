from time import time

def mergeSort(list):
    if len(list) <= 1:
        return list

    middle = len(list) // 2
    left = list[:middle]
    right = list[middle:]

    left = mergeSort(left)
    right = mergeSort(right)

    return merge(left, right)

def merge(listA, listB):
    global comparisons
    new_list = []
    a = 0
    b = 0

    while a < len(listA) and b < len(listB):
        comparisons += 1

        if listA[a] < listB[b]:
            new_list.append(listA[a])
            a += 1
        else:
            new_list.append(listB[b])
            b += 1

    while a < len(listA):
        new_list.append(listA[a])
        a += 1

    while b < len(listB):
        new_list.append(listB[b])
        b += 1

    return new_list


list = [36, 71, 16, 21, 73, 9, 0, 40, 66, 5]
comparisons = 0

t0 = time()
list = mergeSort(list)
t1 = time()

print ("Sorted List:")
print (list, "\n")

print ("Time: {0:f} seconds".format(t1 - t0))
print ("comparisons:", comparisons)