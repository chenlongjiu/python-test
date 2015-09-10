# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
	def countNodes(self, root):
		if not root:
			return 0
		cur = root
		rel = [root]
		cnt = 1
		nu = 0
		depth = 0
		while cur:
			cur = cur.right
			nu += cnt
			cnt *= 2
			depth += 1
		print depth
		#now you have a list contains all the previous level nodes which were visited
		start, end = 0, 2**depth-1
		while start + 1 < end:
			print "get into the loop"
			mid = (start+end)/2
			tmp = mid
			path = []
			for _ in xrange(depth):
				path.append(tmp%2)			    
				tmp /= 2
			cur = root
			while path:
				if path.pop() == 0:
					cur = cur.left
				else:
					cur = cur.right 
			if not cur:
				end = mid
			else:
				start = mid
		if start == 0:
			cur = root
			for _ in xrange(depth):
				cur = cur.left
			if cur is None:
				return nu
			else:
				print "result "
				return nu + 1
		print "result is ", nu + start + 1
		return nu + start + 1
		
		#for thsi row it has some 
		"""
		:type root: TreeNode
		:rtype: int
		"""

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print Solution().countNodes(root)
		