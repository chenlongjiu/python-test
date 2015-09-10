class STNode:
    def __init__(self, start, end, max):
        self.start, self.end, self.max = start, end, max
        self.left, self.right = None, None

class Solution:
    """
    @param A: A list of integer
    @return: Count the number of element before this element 'ai' is 
             smaller than it and return count number list
    """
    def BST(self, A, start, end):
        if not A:
            return 
        root = STNode(start, end, A[start])

        if start == end:
            return root
        mid = (start + end) / 2
        root.left = self.BST(A,start, mid)
        root.right = self.BST(A, mid+1, end)
        root.max = max(root.left.max, root.right.max)
        return root
        
    def cnt(self, root, start, end, target):
        # print "initial start, and  end and target are " , start, end, target,root.start, root.end
        if target > root.max:
            # print "start : end : target", start, end, target, " return: ", end - start + 1
            return end - start + 1
        
        if root.start == root.end:
            return 0
        mid = (root.start + root.end) // 2
        if end <= mid:
            return self.cnt(root.left, start, end, target)
        elif start > mid: 
            return self.cnt(root.right, start, end, target)
        else:
            return self.cnt(root.left, start, mid, target) + self.cnt(root.right, mid+1, end, target)
        
        
        
        
    def countOfSmallerNumberII(self, A):
        # write your code here
        
        root = self.BST(A, 0, len(A)-1)
        if root is None:
            return []
        rel = [0]
        for index in xrange(1, len(A)):
            cur = root
            rel.append(self.cnt(cur,0, index-1, A[index]))
        return rel

print Solution().countOfSmallerNumberII([1,2,7,8,5])