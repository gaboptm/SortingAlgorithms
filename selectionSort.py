from time import time

def selectionSort(list):
    global comparisons
    n = len(list)

    for i in range(n - 1):
        minus = i
        comparisons += 1

        for j in range(i + 1, n):
            if list[j] < list[minus]:
                minus = j

        list[i], list[minus] = list[minus], list[i]


list = [36, 71, 16, 21, 73, 9, 0, 40, 66, 5]
comparisons = 0

t0 = time()
selectionSort(list)
t1 = time()

print ("Sorted List:")
print (list, "\n")

print ("Time: {0:f} seconds".format(t1 - t0))
print ("comparisons:", comparisons)