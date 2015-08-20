import copy
class Solution:
    # @param grid, a list of list of characters
    # @return an integer
    def numIslands(self, grid):
        land = copy.deepcopy(grid)
        counter = 2
        if len(land) == 0:
            return 0
        h = len(land)
        l = len(land[0])
        for i in range(h):
            for j in range(l):
                if land[i][j] == '1':
                    self.checkIsland(i,j, land, counter)
                    counter += 1
        
        return counter-2
        
    def checkIsland(self, i, j, land, counter):
        land[i][j] = counter
        if i+1 < len(land[0]) :
            if land[i+1][j] == '1':
                self.checkIsland(i+1, j, land, counter)
        if i-1 >= 0 :
            if land[i-1][j] =='1':
                self.checkIsland(i-1, j, land, counter)
        if j+1 < len(land) :
            if land[j+1][i] == '1':
                self.checkIsland(i, j+1, land, counter)
        return 

sol = Solution()
grid = [['10']]
print (sol.numIslands(grid))
