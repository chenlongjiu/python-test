array = [3,5,3,2,6,8,6,4,6,7,3,55,1,4,3,8]

def Max_Heapify(array):
	if len(array) == 1:
		return array
	if len(array) > 3:
		 if array[0]<array[1]:
			array[0], array[1] = array[1], array[0]
			if array[1] <array[2]:
				array[1], array[2] = array[2], array[1]
				
