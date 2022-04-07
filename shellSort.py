from time import time

def shellSort(list):
    global comparisons
    n = len(list)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            val = list[i]
            j = i
            comparisons += 1

            while j >= gap and list[j-gap] > val:
                list[j] = list[j-gap]
                j -= gap

            list[j] = val

        gap //= 2


list = [36, 71, 16, 21, 73, 9, 0, 40, 66, 5]
comparisons = 0

t0 = time()
shellSort(list)
t1 = time()

print ("Sorted List:")
print (list, "\n")

print ("Time: {0:f} seconds".format(t1 - t0))
print ("comparisons:", comparisons)