class Solution(object):
	def check(self, candidates,target,cur):
		if target == 0:
			return [[]]
		if target < 0 or cur > len(candidates):
			return []
		rel = []
		for i in xrange(cur, len(candidates)):
			if i != cur and candidates[i] == candidates[i-1]:
				print "continue"
				continue
			else:
				tmp = self.check(candidates,target-candidates[i], i+1)
				for ele in tmp:
					ele.append(candidates[i])
					print "ele is ", ele ," attached with ", candidates[i]
				rel += tmp
				
		return rel




	def combinationSum2(self, candidates, target):
		candidates = sorted(candidates)[::-1]
		return self.check(candidates,target,0) 
		"""
		:type candidates: List[int]
		:type target: int
		:rtype: List[List[int]]
		"""


print Solution().combinationSum2([1,2],3)