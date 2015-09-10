class Solution(object):
    # O(m*n) space
    def calculateMinimumHP(self, dungeon):
        if not dungeon:
            return 
        r, c = len(dungeon), len(dungeon[0])
        dp = [[0 for _ in xrange(c)] for _ in xrange(r)]
        dp[-1][-1] = max(1, 1-dungeon[-1][-1])
        for i in xrange(c-2, -1, -1):
            dp[-1][i] = max(1, dp[-1][i+1]-dungeon[-1][i])
            print dp[-1][i], dp[-1][i+1]-dungeon[-1][i]
        print dp
        for i in xrange(r-2, -1, -1):
            dp[i][-1] = max(1, dp[i+1][-1]-dungeon[i][-1])
        print dp
        for i in xrange(r-2, -1, -1):
            for j in xrange(c-2, -1, -1):
                dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1])-dungeon[i][j])
        print dp
        return dp[0][0]


# # O(n) space
# class Solution(object):
#     def calculateMinimumHP(self, dungeon):
#         if not dungeon:
#             return 
#         r, c = len(dungeon), len(dungeon[0])
#         dp = [0 for _ in xrange(c)]
#         print dp
#         dp[-1] = max(1, 1-dungeon[-1][-1])
#         print dp
#         for i in xrange(c-2, -1, -1):
#             dp[i] = max(1, dp[i+1]-dungeon[-1][i])
#         print dp
#         for i in xrange(r-2, -1, -1):
#             dp[-1] = max(1, dp[-1]-dungeon[i][-1])
#             for j in xrange(c-2, -1, -1):
#                 dp[j] = max(1, min(dp[j], dp[j+1])-dungeon[i][j])
#         print dp
#         return dp[0]

# test = [[-2,-3,3],[-5, -10, 1],[10, 30, -5]]
# print Solution().calculateMinimumHP(test)

test = [[1,-3,3],[0,-2,0],[-3,-3,4]]
print Solution().calculateMinimumHP(test)