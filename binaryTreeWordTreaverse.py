# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def __init__(self):
		self.result = []
	
	def search(self, cur, rel):
		print cur.val, rel
		if cur.left is not None:
			rel.append(str(cur.val))
			self.search(cur.left,rel)
			rel.pop()
		if cur.right is not None:
			rel.append(str(cur.val))
			self.search(cur.right,rel)
			rel.pop()
		if cur.left is None and cur.right is None:
			rel.append(str(cur.val))
			self.result.append("->".join(rel))
			rel.pop()
		return
	def binaryTreePaths(self, root):
		"""
		:type root: TreeNode
		:rtype: List[str]
		"""
		if root is None:
			return self.result
		rel = []
		self.search(root, rel)
		return self.result


sol = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)
print sol.binaryTreePaths(root)