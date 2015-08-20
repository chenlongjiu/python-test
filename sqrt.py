class Solution:
	# @param x, an integer
	# @return an integer
	def sqrt(self, x):
	    i=1;
	    max = 1
	    min = 1
	    if x == 0:
	   		return 0
	    while True:
	    	if i**2 < x:
	    		min = i
	    		i *= 2
	    	if i**2 > x:
	    		max = i
	    		break
	    	if i**2 == x:
	    		return i
	    while True:
	    	i = int((max+min+1)/2)
	    	if i**2 == x:
	    		return i
	    	if (max-min) == 1:
	    		return i-1
	    	if i**2 < x:
	    		min = i
	    	elif i**2 > x:
	    		max = i
	    	






sol = Solution()
print sol.sqrt(100)
print sol.sqrt(2)