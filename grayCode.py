def grayCode(n):
	if n == 0:
		return [0,]
	if n == 1:
		return [0,1]
	bit = 1 << (n-1)
	#define bit set one bit to 1
	print "n is ", n
	print "this is bit",bit
	lower = grayCode(n-1)
	print "this is lower", lower
	
	print lower+[(bit|i) for i in reversed(lower)]

	return lower+[(bit|i) for i in reversed(lower)]
grayCode(5)

