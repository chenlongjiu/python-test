class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution(object):
	def zigzagLevelOrder(self, root):
		res, queue = [], [(root, 0)]
		while queue:
			curr, level = queue.pop(0)
			if curr:
				if len(res) < level+1:
					res.append([])
				if level % 2 == 0:
					res[level].append(curr.val)
				else:
					res[level].insert(0, curr.val)
				queue.append((curr.left, level+1))
				queue.append((curr.right, level+1))
		return res
			
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
pt = lambda x : x.val
print Solution().zigzagLevelOrder(root)
# for i in Solution().zigzagLevelOrder(root)[0]:
	# print pt(i)
