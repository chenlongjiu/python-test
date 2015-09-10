'''
Given a collection of integers that might contain duplicates, nums, return all possible subsets.

Note:

	Elements in a subset must be in non-descending order.
	The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

'''
'''

#bit manipulation
class Solution(object):
	def subsetsWithDup(self, nums):
		nums = sorted(nums)
		subsetsNum = 1 << len(nums)
		rel = []
		for no in xrange(subsetsNum):
			tmp,flag = [],True
			for check in xrange(len(nums)):
				if no>>check&1 == 0:
					pass
				else:
					if check > 0 and nums[check] == nums[check-1] and no>>(check-1) & 1 == 0:
						flag = False
						break  
					else:
						tmp.append(nums[check])
			if flag:
				rel.append(tmp)
		return rel
'''


#backtracking
class Solution(object):
	def subsetsWithDup(self, nums,index = 0):
		if not nums:
			return []
		nums = sorted(nums)
		rel = []
		rel.append([])
		for i in xrange(index,len(nums)):
			if i > index and nums[i] == nums[i-1]:
				pass
			else:
				sub = self.subsetsWithDup(nums,i+1)
				for x in sub:
					x.insert(0,nums[i])
				# print sub
				rel += sub
		return rel

print Solution().subsetsWithDup([1,2,2])





		