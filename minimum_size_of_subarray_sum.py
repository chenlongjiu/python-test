'''
Given an array of n positive integers and a positive integer s, find the minimal length of a subarray of which the sum ≥ s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.

click to show more practice.
More practice:

If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).

Credits:
Special thanks to @Freezen for adding this problem and creating all test cases.


'''


class Solution(object):
	def divide(self, devidend, devisor):
		flag = (devidend >= 0) is (devisor >= 0)
		if devisor == 0:
			if flag:
				return pow(2,31)-1
			else:
				return -pow(2,31)
		devidend, devisor = abs(devidend),abs(devisor)
		res=0
		while devidend >= devisor:
			div = devisor
			move = 1
			while devidend >= div:
				res += move
				devidend -= div
				div <<= 1
				move <<= 1
		if not flag:
			res = -res
		return max(-pow(2,31),min(pow(2,31)-1,res))





