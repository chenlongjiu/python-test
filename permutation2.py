'''
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[1,1,2], [1,2,1], and [2,1,1]. 
'''


class Solution(object):
	def check(self,nums):
		if len(nums) <= 1:
			return [nums]
		last = []
		rel  = []
		for i in xrange(len(nums)):
			if nums[i] not in last:
				last.append(nums[i])
				if i < len(nums)-1:
					tmp = self.check(nums[:i]+nums[i+1:])
				else:
					tmp = self.check(nums[:i])
				for ele in tmp:
					ele += [nums[i]]
				rel += tmp
		return rel




	def permuteUnique(self, nums):
		#nums = sorted(nums)
		return self.check(nums)

print Solution().permuteUnique([1,1,2])