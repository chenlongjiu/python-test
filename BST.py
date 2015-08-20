import math

class BSTNode:
	def __init__(self, key, value, parent=None, left=None, right=None):
        """
        The class constructor

        @param key: the key of the node
        @param value: the value of the node
        @param parent: pointer to the parent node
        @param left: pointer to the left child
        @param right: pointer to the right child

        @return: null
        """
        self.key = key
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

	'''adding a key pair to the BST'''
	def put(self,key,value):
		if self.root = None:
			self.root.put(key, value)
		else:
			self.root = TreeNode(key,value)

	def get(self,key):
		'''retrieve the value associate with the key '''
		if self.root:
			return self.root.get(key)
		else: 
			return None	

class BST:
	 """
        Search the key from node, iteratively

        @param node: a BST Node
        @param key: a key value
        @return: the node with the key; Null if the key is not found
    """
	def __init__(self):
		slef.root = None

	def find(self, node, key):
		if None == node or key == node.key: 
			return node
		else if node.value < key
			return find(self.right, key)
		else if node.valeu > key
			return find(self.left, key)

	def find_iterative(self, node, key):
		"""
        Search the key from node, iteratively

        @param node: a BST Node
        @param key: a key value
        @return: the node with the key; Null if the key is not found
        """
        if node == None or node.value == key:
        	return node
        current = node
        while (current.value != key):
        	if current.value < key and current.right != None:
        		current = current.right
        	else if current.value > key and current.left != None:
        		current = current.left
        	else: 
        		return null
        return 


    def insert(self, key, value):
    	if self.root == None:
    		self.root = BSTNode(key, value)
    	else:
    		while((current.value < value and current.right != None)or (current.value > value and current.left != None)):
    			if current.value < value :
    				current = current.right
    			if current.value > value : 
    				current = current.left
    		if current.value < value:
    			current.right = BST(key,value, current)
    		if current.value > value: 
    			current.left = BST(key, value, current)

    	return 
    		

    # still need to create def function





