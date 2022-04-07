from time import time

def insertionSort(list):
    n = len(list)
    global comparisons

    for i in range(1, n):
        val = list[i]
        j = i

        while j > 0 and list[j-1] > val:
            list[j] = list[j-1]
            j -= 1
            comparisons += 1

        list[j] = val


list = [36, 71, 16, 21, 73, 9, 0, 40, 66, 5]
comparisons = 0

t0 = time()
insertionSort(list)
t1 = time()

print ("Sorted List:")
print (list, "\n")

print ("Time: {0:f} seconds".format(t1 - t0))
print ("comparisons:", comparisons)