'''

Implement pow(x, n). 

'''

class Solution(object):
    def myPow(self, x, n):

    	if n == 0:
    		return 1

    	if n < 0:
    		x = 1/x
    		n = -n

    	if n == 1 :
    		return x

    	return self.myPow(x*x,n/2) if n%2 == 0 else x * self.myPow(x*x, n/2)


        """
        :type x: float
        :type n: int
        :rtype: float
        """

print Solution().myPow(3.89707, 2)