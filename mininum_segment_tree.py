import sys
class STNode:
    def __init__(self, start, end, min):
        self.start, self.end, self.min = start, end, min
        self.left, self.right = None, None


class Solution:	
    """
    @param A, queries: Given an integer array and an Interval list
                       The ith query is [queries[i-1].start, queries[i-1].end]
    @return: The result list
    """
    
    #BUILD AN SEGMENT TREE RECORD MININUM
    
    def BSTMIN(self, A, start, end):
        root = STNode(start, end, A[start])
        if start == end:
            return root
        mid = (start + end) / 2
        root.left = self.BSTMIN(A, start, mid)
        root.right= self.BSTMIN(A, mid+1, end)
        root.min = min(root.left.min, root.right.min)
        return root
    
    def BSTSearch(self,root, start, end):
        print start, end
        print "root level", root.start, root.end, "root.min" , root.min
        if root is None:
            return sys.maxint
        if root.start == start and root.end == end:
            # print root.min
            return root.min
        mid = (root.start+root.end)/2 
        if start <= mid and end > mid:
            leftmin = self.BSTSearch(root.left, start,mid)
            rightmin = self.BSTSearch(root.right, mid+1, end)

        elif end <= mid:
            leftmin = self.BSTSearch(root.left, start, end)
            rightmin = sys.maxint

        elif start > mid:
            leftmin = sys.maxint
            rightmin = self.BSTSearch(root.right,start, end)

        print leftmin, rightmin
        return min(leftmin,rightmin)
    
    
    def intervalMinNumber(self, A, queries):
        # write your code here
        root  = self.BSTMIN(A, 0, len(A)-1)
        rel = []
        for interval in queries:
            cur = root
            left, right = interval[0], interval[1]
            if left < 0 or right >= len(A):
                return []
            # print left, right
            rel.append(self.BSTSearch(cur, left, right))
        
        return rel
            
print Solution().intervalMinNumber([1,2,7,8,5], [[2,4]])#[[0,4],[0,0],[3,4],[0,3]])