'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

You should return [1,2,3,6,9,8,7,4,5]. 
'''

class Solution(object):
	def spiralOrder(self, matrix):
		cnt = 0
		if len(matrix) == 0 or len(matrix[0]) == 0:
			return []
		rel = []
		left, right , up, down = 0, len(matrix[0]), 0, len(matrix)
		
		while True:
			if not left < right:
				return rel
			#right order:
			for index in xrange(left, right):
				
				rel.append(matrix[up][index])
			up += 1

			print "left to right", rel
			#down order:
			if not up < down:
				return rel
			for index in xrange(up,down):
				rel.append(matrix[index][right-1])
			right -= 1
			print "top to down", rel

			#left order:
			if not left < right:
				return rel
			print right-1, left-1
			for index in xrange(right-1, left-1, -1):
				rel.append(matrix[down-1][index])
			down -= 1
			print "right to left", rel
			#up order
			if not up < down:
				return rel
			for index in xrange(down-1,up-1, -1):
				rel.append(matrix[index][left])
			left += 1
			print "bot to top", rel

		return rel



print Solution().spiralOrder([[1,2],[3,4]])

# print Solution().spiralOrder([[ 1, 2, 3 ]])

# print Solution().spiralOrder([[ 1]])

# print Solution().spiralOrder([[]])

