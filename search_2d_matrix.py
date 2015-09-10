class Solution(object):
	def searchMatrix(self, matrix, target):
		#search from the bottom left to upper right
		row, col = len(matrix)-1, 0
		while True:
			if row < 0 or col == len(matrix[0]):
				return False
			if matrix[row][col] > target:
				row -= 1
			elif matrix[row][col] < target:
				col += 1
			elif matrix[row][col] == target:
				return True