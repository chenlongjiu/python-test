'''
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100". 
'''
import collections
class Solution(object):
	def addBinary(self, a, b):
		rel = []
		index, carry, maxi= 1, 0 , max(len(a), len(b))
		while index <= maxi or carry == 1:
			digit = carry 
			if index <= len(a):
				digit += int(a[-index])
			if index <= len(b):
				digit += int(b[-index])
			rel.append(str(digit%2))
			carry = digit/2
			index += 1

		
		print rel
		return "".join(rel[::-1])


print Solution().addBinary("10", "110010")


class Solution(object):
	def addBinary(self, a, b):
		i, j, carry, res = len(a)-1, len(b)-1, 0, ""
		while i >= 0 or j >= 0 or carry:
			if i >= 0:
				carry += int(a[i])
				i -= 1
			if j >= 0:
				carry += int(b[j])
				j -= 1
			res = str(carry%2) + res
			carry //= 2
		return res