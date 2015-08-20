
array = [1,2,4,5,2,6,2,4,5,6]
final = []
def sort(array):
	less=[]
	equal=[]
	greater= []
	if len(array) <= 1:
		return array
	elif len(array) > 1:
		pivot = array[0]
		for x in array:
			if x < pivot:
				less.append(x)
			if x == pivot:
				equal.append(x)
			if x > pivot:
				greater.append(x)
		return sort(less)+equal + sort(greater)
print sort(array)
