class Solution(object):
    def check(self, board,row,col,flag,word,index):
        #check 4 directions
        if index >= len(word):
            print "reach true"
            return True
        print 'row , col', row, col,index
        #search top
        if row > 0 and board[row-1][col] == word[index] and flag[row-1][col] == 0:
            flag[row-1][col] = 1
            if self.check(board,row-1,col,flag,word,index+1):
                return True
            flag[row-1][col] = 0
        #search left
        if col > 0 and board[row][col-1] == word[index] and flag[row][col-1] == 0:
            flag[row][col-1] = 1
            if self.check(board,row,col-1,flag,word,index+1):
                return True
            flag[row][col-1] = 0
        #search down
        if row + 1 < len(board) and board[row+1][col] == word[index] and flag[row+1][col] == 0:
            flag[row+1][col] = 1
            if self.check(board,row+1,col,flag,word,index+1):
                return True
            flag[row+1][col] = 0
        #search right    
        if col+1 <len(board[0]) and board[row][col+1] == word[index] and flag[row][col+1] == 0:
            print "get in"
            flag[row][col+1] = 1
            if self.check(board,row,col+1,flag,word,index+1):
                return True
            flag[row][col+1] = 0
        
        return False
    
    
    def exist(self, board, word):
        if not board or not word:
            return False
        
        flag = [[0]*len(board[0]) for _ in xrange(len(board))]
        for r in xrange(len(board)):
            for c in xrange(len(board[0])):
                if board[r][c] == word[0]:
                    flag[r][c] = 1
                    print flag
                    if self.check(board,r,c,flag,word,1):
                        return True
                    flag[r][c] = 0
        return False


print Solution().exist(["ab"], "ab")