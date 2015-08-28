
import collections

class Solution(object):
    def solveNQueens(self, n, pos = collections.deque(), row = 0,res = 0):
        if row == 0:
            res = 0
    	if row == n:
    		res += 1
    		return res
    	for col in xrange(n):
    		flag = False
    		for x, y in pos:
    			if y == col or abs(x-row) == abs(y-col):
    				flag = True
    				break
    		if not flag:
    			pos.append((row,col))
    			res = self.solveNQueens(n,pos,row+1,res)
    			pos.pop()
    	return res

print Solution().solveNQueens(17)
    		