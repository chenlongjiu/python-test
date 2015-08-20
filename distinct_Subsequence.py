class Solution:
    # @return an integer
    def numDistinct(self, S, T):
        lt,ls = len(T),len(S)
        if lt > ls or lt== 0:
            return 0
        dp = [1] * (ls+1)   #[1,1,1,1,1,1,1]
        for i in range(lt):
            new_dp = [0]*(ls+1) #[0,0,0,0,0,0,0]
            for j in range(ls):
                if i <= j:
                    new_dp[j+1] = new_dp[j] + (T[i] == S[j]) * dp[j]
            dp = new_dp
    return dp[ls]

sol = Solution()
print sol.numDistinct("", "a")