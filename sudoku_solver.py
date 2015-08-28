"""
:type board: List[List[str]]
:rtype: void Do not return anything, modify board in-place instead.
"""
import collections
class Solution(object):
	def __init__(self):
		self.row, self.col, self.square = [set([]) for _ in xrange(9)], [set([])  for _ in xrange(9)], [set([]) for _ in xrange(9)]
		return

	def check(self,fill, board):
		if not fill:
			return True
		
		r, c = fill.popleft()
		for i in xrange(1, 10):
			if str(i) not in self.row[r] and str(i) not in self.col[c] and str(i) not in self.square[int(r/3) * 3 + c/3]:
				board[r] = "%s%s%s"%(board[r][:c] , str(i) , board[r][c+1:])
				self.row[r].add(str(i))
				self.col[c].add(str(i))
				self.square[int(r/3) * 3 + c/3].add(str(i))
				if self.check(fill, board):
					return True
				board[r] = "%s%s%s"%(board[r][:c] , '.' , board[r][c+1:])
				self.row[r].discard(str(i))
				self.col[c].discard(str(i))
				self.square[int(r/3) * 3 + c/3].discard(str(i))

		fill.appendleft((r,c))
		return False


	def solveSudoku(self, board):
		needFill = collections.deque()
		#loop up for initial the board		
		for r in xrange(len(board)):
			for c in xrange(len(board[0])):
				if board[r][c] == '.':
					needFill.append((r,c))
					pass
				else:
					if board[r][c] in self.row[r]:
						return 
					else:
						self.row[r].add(board[r][c]) 
					if board[r][c] in self.col[c]:
						return 
					else:
						self.col[c].add(board[r][c])
					if board[r][c] in self.square[int(r/3) * 3 + c/3]:
						return 
					else:
						self.square[int(r/3) * 3 + c/3].add(board[r][c])
		self.check(needFill,board)
		return board

sol = Solution()
print sol.solveSudoku(["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."])






