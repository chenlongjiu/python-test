class Solution(object):
    def minDistance(self, word1, word2):
        if word1 == "" or word2 == "":
            return max(len(word1), len(word2))
        dp = [[0]*(len(word2)+1) for _ in xrange(len(word1)+1)]
        #initialize the value
        for i in xrange(len(dp)):
            dp[i][0] = i
        for j in xrange(len(dp[0])):
            dp[0][j] = j
        for w1 in xrange(1,len(word1)+1):
            for w2 in xrange(1,len(word2)+1):
                print word1[w1-1], word2[w2-1]
                if word1[w1-1] == word2[w2-1]:
                    dp[w1][w2] = dp[w1-1][w2-1]
                else:
                    dp[w1][w2] = min(dp[w1-1][w2-1] + 1, dp[w1-1][w2]+1, dp[w1][w2-1]+1)
                print dp[0]
                print dp[1]
                print dp[2]
                print "///////////////////////////////"
        return dp[-1][-1]

print Solution().minDistance('ab','ba')