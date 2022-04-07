from time import time


def binarySearch(sorted_arr, n, element):


	i = 0


	start = 0
	end = n - 1

	
	while i < n:
		
		middle = (start + end) // 2

		
		if sorted_arr[middle] == element:
			
			return True
		elif sorted_arr[middle] < element:
			
			start = middle + 1
		else:
			
			end = middle - 1
		i += 1
	return False

arr = [0, 5, 9, 16, 21, 36, 40, 66, 71, 73] 
n = 10
element_to_be_searched = 9


t0 = time()
if binarySearch(arr, n, element_to_be_searched):
	print(element_to_be_searched, "is found")
else:
	print(element_to_be_searched, "is not found")
t1 = time()


print ("Time: {0:f} seconds".format(t1 - t0))