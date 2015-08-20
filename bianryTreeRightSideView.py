# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def bsf(self, node, li):
        nextLevel = []
        flag = False
        length = len(node)
        for i in range(length):
            cur = node.pop(0)
            print "cur value is ", cur.val
            if cur.right is not None:
                node.append(cur.right)
                if not flag:
                    li.append(cur.right.val)
                    flag = True
            if cur.left is not None:
                node.append(cur.left)
                if not flag:
                    li.append(cur.left.val)
                    flag = True
        if len(node) == 0:
            return
        else:
            self.bsf(node, li)
            return
        
    def rightSideView(self, root):
        #bst would be good to this 
        li = []
        node = []
        if root is not None:
            li.append(root.val)
            node.append(root) 
            self.bsf(node, li)
        
        return li            

sol  = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)

print sol.rightSideView(root)
