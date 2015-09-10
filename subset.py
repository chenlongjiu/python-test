'''
Given a set of distinct integers, nums, return all possible subsets.

Note:

    Elements in a subset must be in non-descending order.
    The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]


'''

class Solution(object):
    def subsets(self, nums):
    	maxi = 2 ** len(nums)
    	rel = []
    	for i in xrange(maxi):
    		tmp = []
    		for t in xrange(len(nums)-1, -1, -1):
    			if (i >> t) & 1 == 0:
    				pass
    			else:
    				tmp.append(nums[t])
    		rel.append(tmp)
    	return rel

print Solution().subsets([1,2,3])
