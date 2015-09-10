'''
Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.

For example,
Given n = 3, your program should return all 5 unique BST's shown below.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def gT(self, start, end):
        # print start, end
    	if start > end:
    		return [None]
    	if start == end:
    		return [TreeNode(start)]
    	rel = []
    	for x in xrange(start,end+1):
    		leftTree = self.gT(start,x-1)
    		rightTree = self.gT(x+1,end)
    		tmp = []
    		for leftNode in leftTree:
    			for rightNode in rightTree:
    				t = TreeNode(x)
    				t.left, t.right = leftNode, rightNode
    				tmp.append(t)
    		rel += tmp
    	return rel



    	#return list[all trees's nodes]

    def generateTrees(self, n):
    	return self.gT(1,n)





        """
        :type n: int
        :rtype: List[TreeNode]
        """
        