'''
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,
You should return the following matrix:

[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

'''
class Solution(object):
    def generateMatrix(self, n):
        if n == 0:
            return []
        rel = [[0] * n for _ in xrange(n)]
        left, top, right, bot = 0, 0, n, n
        cnt = 0
        while cnt < n*n:
            #right movement
            for index in xrange(left, right):
                rel[top][index] = cnt+1
                cnt += 1
            top += 1
            
            #bot movement
            for index in xrange(top, bot):
                rel[index][right-1] = cnt+1
                cnt += 1
            right -= 1
            
            #left movement
            for index in xrange(right-1,left-1,-1):
                rel[bot-1][index] = cnt+1
                cnt += 1
            bot -= 1
            
            #up movement
            for index in xrange(bot-1, top-1, -1):
                rel[index][left] = cnt+1
                cnt += 1
            left += 1
        return rel
        """
        :type n: int
        :rtype: List[List[int]]
        """
        