
import collections

class Solution(object):
    def solveNQueens(self, n, pos = collections.deque(), row = 0,res = []):

    	
    	if row == n:
    		# tmp = 
    		# print pos
    		solution = [['.']*n for _ in xrange(n)]
    		for i in xrange(len(pos)):
    			x,y = pos[i]
    			solution[x][y] = 'Q'
    		for r in xrange(len(solution)):
    			solution[r] = "".join(solution[r][:])

    		res.append(solution)
    		# print res
    		#print res
    		return res
    	for col in xrange(n):
    		flag = False
    		for x, y in pos:
    			if y == col or abs(x-row) == abs(y-col):
    				flag = True
    				break
    		if not flag:
    			pos.append((row,col))
    			self.solveNQueens(n,pos,row+1,res)
    			pos.pop()
    	return res

print Solution().solveNQueens(17)
    		