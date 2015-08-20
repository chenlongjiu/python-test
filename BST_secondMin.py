# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.stack = list()
        self.stack.append(root)
        
    
    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        if self.stack:
            return self.stack;

    # @return an integer, the next smallest number
    def next(self):
        tmp = self.stack.pop()
        tmpN = tmp.right #find the next smallest num in right tree
        while tmpN != None: 
            self.stack.append(tmp)
            tmpN = tmpN.left
        return tmp

# Your BSTIterator will be called like this:
root = TreeNode(10)
i, v = BSTIterator(root), []
while i.hasNext():
    v.append(i.next())
    