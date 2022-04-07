from time import time

def partition(list, left, right):
	global comparisons
	pivot = list[right]
	index = left

	for i in range(left, right):
		comparisons += 1
		
		if list[i] <= pivot:
			list[index], list[i] = list[i], list[index]
			index += 1

	list[index], list[right] = list[right], list[index]
	return index

def quicksort(list, left, right):
    if left < right:
        pivot_index = partition(list, left, right)
        quicksort(list, left, pivot_index-1)
        quicksort(list, pivot_index+1, right)


list = [36, 71, 16, 21, 73, 9, 0, 40, 66, 5]
comparisons = 0

t0 = time()
quicksort(list, 0, len(list)-1)
t1 = time()

print ("Sorted List:")
print (list, "\n")

print ("Time: {0:f} seconds".format(t1 - t0))
print ("comparisons:", comparisons)