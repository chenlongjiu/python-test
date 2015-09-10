#morris treaversal
class TreeNode (object):
	def __init__(self,x):
		self.left, self.right = None, None
		self.val = x

class Solution2(object):
	def morris_traversal(self, root):
		cur = root
		prev = None
		# print cur.left.val
		while cur is not None:
			if cur.left is None:
				print cur.val
				cur = cur.right
			else:
				prev = cur.left
				while prev.right is not None and prev.right != cur:
					prev = prev.right

				if prev.right is None:
					prev.right = cur
					cur = cur.left
				else:
					prev.right = None
					print cur.val
					cur = cur.right

		return
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        cur = root
        first, second = None, None
        rel = []
        prev = TreeNode(-float('inf'))
        while cur is not None:
            if cur.left is not None:
	            p = cur.left
	            while p.right is not None and p.right!=cur:
	            	p = p.right
	            
	            if p.right is not None:
	            	if prev.val > cur.val:
	            		print "left travel", prev.val, cur.val
	            		if first is None: 
	            			first,second = prev, cur
	            		else:
	            			second = cur

	            	prev = cur
	            	p.right = None
	            	cur = cur.right
	            else:
	            	p.right = cur
	            	cur = cur.left
            else:
            	if prev.val > cur.val:
            		print "coner place", prev.val, cur.val
            		if first is None:
            			first,second = prev,cur
            		else:
            			second = cur
            	prev = cur
            	cur = cur.right
        print first.val, second.val
        first.val,second.val = second.val,first.val

        return 
        
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        









test = TreeNode(2)
test.right = TreeNode(1)


start = TreeNode(5)
start.left = TreeNode(3)
start.left.left , start.left.right = TreeNode(1), TreeNode(7)
start.right = TreeNode(8)
start.right.left, start.right.right = TreeNode(4), TreeNode(9)
Solution().recoverTree(test)
Solution2().morris_traversal(test)