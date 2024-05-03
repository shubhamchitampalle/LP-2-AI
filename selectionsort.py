
def selectionSort(array, size):
	for i in range(size):
		min_index = i
		for j in range(i + 1, size):
			if array[j] < array[min_index]:
				min_index = j
		(array[i], array[min_index]) = (array[min_index], array[i])

array=[]
n = int(input("Enter number of elements in array : "))
for i in range(n):
	element=int(input("Enter element in the array : "))
	array.append(element)
selectionSort(array,n)
print('The array after sorting in Ascending Order by selection sort is : ')
print(array)

