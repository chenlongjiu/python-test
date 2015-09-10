'''

Medium Count of Smaller Number
18%
Accepted

Give you an integer array (index from 0 to n-1, where n is the size of this array, value from 0 to 10000) and an query list. For each query, give you an integer, return the number of element in the array that are smaller that the given integer.
Have you met this question in a real interview?
Example

For array [1,2,7,8,5], and queries [1,8,5], return [0,4,2]
Note

We suggest you finish problem Segment Tree Build and Segment Tree Query II first.
Challenge

Could you use three ways to do it.

    Just loop
    Sort and binary search
    Build Segment Tree and Search.


'''

class STNode:
    def __init__(self, start, end, max):
        self.start , self.end, self.max = start, end, max
        self.left, self.right = None, None
        
class Solution:
    """
    @param A: A list of integer
    @return: The number of element in the array that 
             are smaller that the given integer
    """
    '''
    #just loop
    def countOfSmallerNumber(self, A, queries):
        rel =[]
        for i in queries:
            cnt = 0
            for k in A:
                if k < i :
                    cnt+=1
            rel.append(cnt)
            
        return rel
        # write your code here
    #tle
    '''
    '''
    def quickSort(self, A):
        if not A:
            return []
        smaller, equal , larger = [], [], []
        for i in A:
            if i < A[0]:
                smaller.append(i)
            elif i == A[0]:
                equal.append(i)
            else:
                larger.append(i)
        return self.quickSort(smaller) + equal + self.quickSort(larger)
    
    def BS(self,target, A, left = 0, right = -1):
        
        if right == -1:
            right = len(A)-1
        if not A or target <= A[0]:
            return -1
        if target > A[-1]:
            return len(A)
        while left + 1 < right:
            mid = (left + right) / 2
            if A[mid] < target:
                left = mid
            else:
                right = mid
                
        return left
            
    #sort and binary search
    def countOfSmallerNumber(self, A, queries):
        # write your code here
        A = self.quickSort(A)
        #binary Search for each ele
        rel = []
        for i in queries:
            rel.append(self. BS(i, A)+1)
                
        return rel
    worked
    '''

    
    def BST(self, A, start, end):
        
        root = STNode(start, end, A[start])
        if start == end :
            return root
        mid = (start+ end) / 2
        # print start , "->", mid, "    " , mid+1, "->" , end
        root.left = self.BST(A, start, mid)
        root.right = self.BST(A, mid+1, end)
        root.max = max(root.left.max, root.right.max)
        return root
    
    def cnt(self, root, target):
        # if root == None:
        #     return 0
        if target > root.max:
            return root.end - root.start + 1
        
        
        if target <= root.max:
            if root.start == root. end:
                return 0
            else:
                return self.cnt(root.left, target) + self.cnt(root.right, target)
        
        
        
        
        
        
    #setment Tree
    def countOfSmallerNumber(self, A, queries):
        if not A:
            return [0]*len(queries)
        # write your code here
        root = self.BST(A, 0, len(A)-1)
        rel = []
        for ele in queries:
            cur = root
            rel.append(self.cnt(cur, ele))
        return rel
        

test = [376,628,951,585,223,422,800,813,365,953,989,389,295,369,784,632,488,550,397,583,332,423,66,132,285,419,924,687,206,468,457,867,337,879,105,654,141,284,929,229,980,147,157,430,240,14,351,602,78,718,27,535,892,281,146,44,357,835,746,267,211,140,331,642,591,922,935,790,538,784,816,431,455,495,423,987,884,863,211,165,413,121,981,237,860,569,827,115,166,316,527,484,651,381,208,93,105,825,593,67,734,675,555,96,329,178,626,931,773,172,962,356,426,971,915,279,421,573,664,625,862,786,774,676,363,185,167,566,719,663,761,328,709,958,608,39,648,606,58,489,453,570,222,471,237,117,398,761,335,484,485,553,964,175,179,470,611,334,22,556,582,704,954,354,133,289,299,345,467,218,696,229,991,540,231,43,215,265,851,754,134,610,596,124,743,142,137,507,534,755,914,418,964,432,83,937,615,967,611,643,186,907,419,774,474,364,101,451,297,554,21,538,304,36,536,984,93,900,675,338,987,185,184,126,150,121,661,279,601,643,849,535,216,289,206,913,231,374,128,814,369,850,759,835,21,824,591,631,338,279,807,166,258,325,312,908,335,555,813,428]
for _ in xrange(10):
	test += test
print len(test)
print Solution().countOfSmallerNumber(test, [365,953,989,389,295,369,784,632,488,550,3] )
    
    