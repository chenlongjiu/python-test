class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):
        tpLine = None
        dwLine = None
        ml = None
        mr = None
        # define the four point of the 
        if len(matrix) == 0:
            return 0
        length = len(matrix[0])
        height = len(matrix)
        for i in range(height):
            for j in range(length):
                if matrix[i][j] == '1':
                    if ml is None:
                        ml, mr = j,j 
                    else:
                        ml,mr = min(ml, j), max(mr, j)
                    if tpLine is None:
                        tpLine, dwLine = i,i
                    else:
                        tpLine, dwLine = min(tpLine, i), max(dwLine, i)
        if tpLine is None:
            return 0
        else:
            return (mr-ml+1)*(dwLine-tpLine+1)
