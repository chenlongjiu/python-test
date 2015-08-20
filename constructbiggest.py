
'''
for getting the biggest number, 
first sorting by the first digit, 
if first digit is same, compare the second degit, 
finally, sort from the biggest to smallest. 
'''
import math
# strip the number in digits
def strip(array, num):
	if len(str(num)) == 1:
		print num
		array.append[num]=num
		return num
	if len(str(num)) > 1:
		left = num%10**(len(str(num))-1)
		digit =num/10**(len(str(num))-1)
		array.append(num, left)

		strip(array[digit],left)
		print digit

def constructBiggest(array):
	digitArray = {}
	for x in array:
		i= x/(10**(len(str(x))-1))
		if digitArray.has_key(i):			
			digitArray[i].append()
	for x in range(0,10):
		print x,digitArray



		
#constructBiggest([32,23,1,3,2,6,5])
strip([],2333)