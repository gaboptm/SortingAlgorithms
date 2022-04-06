from time import time


def linearSearch(arr, n, element):

	
	for i in range(n):

		
		if arr[i] == element:
			
			return True

	
	return False


arr = [36, 71, 16, 21, 73, 9, 0, 40, 66, 5]
n = 10
element_to_be_searched = 9


t0 = time()
if linearSearch(arr, n, element_to_be_searched):
	print(element_to_be_searched, "is found")
else:
	print(element_to_be_searched, "is not found")
t1 = time()


print ("Tiempo: {0:f} segundos".format(t1 - t0))