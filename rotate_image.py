'''
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?

'''

class Solution(object):
    def rotate(self, matrix):
        for row in xrange(len(matrix)):
        	for col in xrange(row,len(matrix)):
        		matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
        		
        
        #then reverse:
        for row in xrange(len(matrix)):
        	for col in xrange(len(matrix)/2):
        		matrix[row][col], matrix[row][-col-1] = matrix[row][-col-1], matrix[row][col]
        		print matrix[0]
        		print matrix[1]
        		print matrix[2]
        		print "//////////////////////////"
        #print matrix
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print Solution().rotate(matrix)