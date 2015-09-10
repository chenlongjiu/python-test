'''
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"

click to show corner cases.
Corner Cases:

	Did you consider the case where path = "/../"?
	In this case, you should return "/".
	Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
	In this case, you should ignore redundant slashes and return "/home/foo".


'''



class Solution(object):
	def simplifyPath(self, path):
		step = path.split('/')
		rel,level =['/'], []
		while step:
			action = step.pop(0)
			if action == '' or action == '.':
				pass
			elif action == '..':
			    if level :
				    level.pop() 
			else:level.append(action)
		# print level
		rel.append("/".join(level))
		# print rel
		return ''.join(rel)

		"""
		:type path: str
		:rtype: str
		"""



print Solution().simplifyPath("/a/./b/../../c/")