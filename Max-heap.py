import math

class MaxH:
	size = 0
	array = []

	def __init__(self,array):
		self.size = len(array)
		self.array = array
	
	def builtHeap(self):
		if len(self.array) <= 1:
			return self.array
		for i in range(0,int(len(self.array)/2)+1):
			for j in xrange(i+1,len(self.array)):
				if self.array[i] <= self.array[j]:
					self.array[i], self.array[j] = self.array[j], self.array[i]
		return array

	def insert(self,x):
		self.size += 1
		self.array.append(x)

def reOrder(size,array):
	print array
	print size
	if size == None:
		print 'no array'
		return array
	if size == 1:
		print 'final step'
		return array
	if size >= 2:
		print 'size > 2'
		old = size-1
		new = (size-1)/2
		print array[new],'vesues',array[old]
		if array[new] < array[old]:
			array[new], array[old] = array[old], array[new]
			reOrder(new+1,array)
		if array[new] <= array[old]:
			return array

array = [3,5,6,23,1,4,43,23,16]
heapT = MaxH(array)
heapT.builtHeap()
heapT.insert(32)
reOrder(len(heapT.array),heapT.array)
print heapT.array
