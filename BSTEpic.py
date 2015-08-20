'''

Design a Binary search tree using Epic as Input

'''

class TreeNode:
	left = None
	right = None
	val = None
	def __init__(self, value):
		self.val = value

class Tree:
	head = None
	def insert (self, val):
		if self.head is None:
			self.head = TreeNode(val)
		else:
			cur = self.head
			while True:
				if val > cur.val:
					if cur.right is not None:
						cur = cur.right
					else: 
						cur.right = TreeNode(val)
						return
				elif val <cur. val:
					if cur.left is not None:
						cur = cur.left
					else:
						cur.left = TreeNode(val)
						return 
				else :
					cur = cur.right
					while cur.left is not None:
						cur = cur.left
					cur.left = TreeNode(val)
					return

	def search(self, val):
		cur = self.head
		while (cur is not None and cur.val != val):
			if cur.val > val: 
				cur = cur.left
			elif cur.val < val:
				cur = cur.right
		if cur is None:
			return False
		elif cur.val == val:
			return True

	def show(self, cur):
		if cur is None:
			return
		if cur.left is None and cur.right is None:
			print cur.val
		else: 
			if cur.left is not None:
				self.show(cur.left)
			if cur.right is not None:
				self.show(cur.right)
			print cur.val






te = Tree()
td = [0]*5
td[1] = "Epic"
td[2] = "MS"
td[3] = "SNAP"
td[0] = "Google"
td[4] = "Bloomberg"
for i in range(5):
	te.insert(td[i])

if te.search("Epic"):
	print "find it!"
te.show(te.head)




