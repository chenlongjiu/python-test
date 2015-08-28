'''
Given a collection of numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1]. 
'''

class Solution(object):
    def permute(self, nums):
    	if len(nums) <= 1:
    		return [nums]
    	else:
    		rel = []
    		for i in xrange(len(nums)):
    			if i + 1 < len(nums):
    				tmp = self.permute(nums[:i]+nums[i+1:])
    			else:
    				tmp = self.permute(nums[:i])
    			for ele in tmp:
    				ele.append(nums[i])
    			rel += tmp
    		return rel


print Solution().permute([1,2,3])
