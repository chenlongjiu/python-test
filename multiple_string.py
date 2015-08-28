'''
Given two numbers represented as strings, return multiplication of the numbers as a string.

Note: The numbers can be arbitrarily large and are non-negative.
'''

class Solution(object):
    def multiply(self, num1, num2):
        rel = 0
        for i in xrange(len(num1)):
        	relL, carry  = 0, 0
        	for j in xrange(len(num2)):
        		s = carry + int(num1[-i-1]) * int(num2[-j-1])
        		relL += (s%10)*(10**j)
        		carry = s/10
        		print relL,carry
        	relL += carry * 10 ** len(num2)
        	rel += relL * (10 ** i)
        	print rel
        return rel


print Solution().multiply('98','9')

