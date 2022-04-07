from time import time

def mergeSort(list):
    if len(list) <= 1:
        return list

    medio = len(list) // 2
    izquierda = list[:medio]
    derecha = list[medio:]

    izquierda = mergeSort(izquierda)
    derecha = mergeSort(derecha)

    return merge(izquierda, derecha)

def merge(listA, listB):
    global comparisons
    list_nueva = []
    a = 0
    b = 0

    while a < len(listA) and b < len(listB):
        comparisons += 1

        if listA[a] < listB[b]:
            list_nueva.append(listA[a])
            a += 1
        else:
            list_nueva.append(listB[b])
            b += 1

    while a < len(listA):
        list_nueva.append(listA[a])
        a += 1

    while b < len(listB):
        list_nueva.append(listB[b])
        b += 1

    return list_nueva


list = [36, 71, 16, 21, 73, 9, 0, 40, 66, 5]
comparisons = 0

t0 = time()
list = mergeSort(list)
t1 = time()

print ("list ordenada:")
print (list, "\n")

print ("Tiempo: {0:f} segundos".format(t1 - t0))
print ("comparisons:", comparisons)