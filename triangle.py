class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        #O(n) extra size
        mini = triangle
        if len(triangle) <= 1:
            return triangle[0][0]
        else:
            for levelUp in xrange(len(triangle)-2,-1,-1):
                for count in range(len(triangle[levelUp])):
                    mini[levelUp][count] += min(mini[levelUp+1][count], mini[levelUp+1][count+1])
        return mini[0][0]
