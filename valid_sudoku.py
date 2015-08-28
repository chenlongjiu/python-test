import math
class Solution(object):
    def isValidSudoku(self, board):
        #hashtable should work for this 
        row, col, squ = [{} for _ in xrange(9)] ,[{} for _ in xrange(9)], [{} for _ in xrange(9) ]
        for r in xrange(len(board)):
            for c in xrange(len(board[0])):
                if board[r][c] == '.':
                    pass
                elif board[r][c] in row[r] or board[r][c] in col[c] or board[r][c] in squ[c/3 + int(3 * math.floor(r/3))]:
                    print r, c, board[r][c],board[r][c] in row[r], board[r][c] in col[c], board[r][c] in squ[c/3 + int(3 * math.floor(r/3))]
                    
                    return False
                else:
                    row[r][board[r][c]] = True
                    col[c][board[r][c]] = True
                    squ[c/3 + int(3 * math.floor(r/3))][board[r][c]] = True
                    
        return True

sol = Solution()
print sol.isValidSudoku([".87654321","2........","3........","4........","5........","6........","7........","8........","9........"])