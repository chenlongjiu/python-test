class Solution(object):
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False
        if not s1 or not s2:
            return s1 == s3 or s2 == s3

        dp = [[False] * (len(s2)+1) for _ in xrange(len(s1)+1)]
        
        dp[0][0] = True
        if s1 and s1[0] == s3[0]:
            dp[1][0] = True
        if s2 and s2[0] == s3[0]:
            dp[0][1] = True
        for p in xrange(2, len(s3)+1):
            if p <= len(s1):
                print p 
                dp[p][0] = dp[p-1][0] and s1[p-1] == s3[p-1]
            if p <= len(s2):
                dp[0][p] = dp[0][p-1] and s2[p-1] == s3[p-1]
            for i in xrange(1, p):
                if i >= len(dp) or p-i >= len(dp[0]):
                    pass
                else:
                    dp[i][p-i] = (dp[i-1][p-i] and s1[i-1] == s3[p-1]) or (dp[i][p-i-1] and s2[p-i-1] == s3[p-1])
                
        return dp[-1][-1]

print Solution().isInterleave("db", "b", "cbb")