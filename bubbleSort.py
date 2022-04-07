from time import time


def bubbleSort(list):
    global comparisons
    n = len(list)

    for i in range(1,n):
        for j in range(n-i):
            comparisons += 1

            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]

list = [36, 71, 16, 21, 73, 9, 0, 40, 66, 5]
comparisons = 0

t0 = time()
bubbleSort(list)
t1 = time()

print("Sorted list:")
print (list, "\n")

print ("Time: {0:f} seconds".format(t1 - t0))
print ("comparisons:", comparisons)