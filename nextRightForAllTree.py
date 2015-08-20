'''
Populating Next Right Pointers in Each Node II 
Follow up for problem "Populating Next Right Pointers in Each Node".
What if the given tree could be any binary tree? Would your previous solution still work?
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
        #create a empty node on each layer user that keep tracking the whole nodes on that layer. And connect all of then
        templateNode = TreeNode(0)
        header = root
        while header:
            trackNode = templateNode
            while header:
                if header.left:
                    trackNode.next = header.left
                    trackNode = trackNode.next
                if header.right:
                    trackNode.next = header.right
                    trackNode = trackNode.next
                header = header.next
                
            while root:
                if root.left:
                    header = root.left
                    root= root.left 
                    break
                elif root.right:
                    header = root.right
                    root = root.right
                    break
                else: root = root.next
                
        return