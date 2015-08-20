'''
Populating Next Right Pointers in Each Node 
'''
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        #first get the most right nodes and set their next to null and value 'null' 
        # Then go through all left node then redirect other nodes. 
        if root is None: 
            return
        elif root.left != None:
            root.left.next = root.right
            if root.next == None:
                root.right.next = None
            else:
                root.right.next = root.next.left
            self.connect(root.right)
            self.connect(root.left)
            return