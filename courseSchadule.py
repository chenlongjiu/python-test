class Solution:
	# @param {integer} numCourses
	# @param {integer[][]} prerequisites
	# @return {boolean}
	def dfsCheck(self, dic, passed, val):
		print "key value is " , val 
		print "the value linked with ", val, "are " , dic[val]
		print "visited value are ", passed
		
		for key in dic[val]:
			if key in passed:
				print "error key is ", key, "under ", val
				return False
				
			if key in dic:
				passed.append(key)
				if self.dfsCheck(dic,passed,key) == False:
					return False
				passed.pop()
			else:
				pass
		return True
	
	def canFinish(self, numCourses, prerequisites):
		dic = {}
		maxi = numCourses-1
		#prepare
		if len(prerequisites) == 0:
			return True
		# matrix occupied too much space
		for key in prerequisites:
			if key[0] in dic:
				dic[key[0]].append(key[1])
			else:
				dic[key[0]] = [key[1]]
		print "before start what dic included", dic 
		# do a depth review
		for key in dic:
			if self.dfsCheck(dic, [key], key) == False:
				return False
		
		return True

sol = Solution()
print sol.canFinish(3,[[1,0],[2,1]])
