'''
Minimum Path Sum Total Accepted: 46487 Total Submissions: 143700

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.



'''
class Solution(object):
    def minPathSum(self, grid):
        if not grid or not grid[0]:
            return 0
        for row in xrange(1,len(grid)):
            grid[row][0] += grid[row-1][0]
        for col in xrange(1,len(grid[0])):
            grid[0][col] += grid[0][col-1]
        
        for row in xrange(1,len(grid)):
            for col in xrange(1,len(grid[0])):
                grid [row][col] += min(grid[row-1][col],grid[row][col-1])
        return grid[-1][-1]

        """
        :type grid: List[List[int]]
        :rtype: int
        """