class Solution:
    # @return an integer
    def trailingZeroes(self, n):
    	print n
        return 0 if n == 0 else n / 5 + self.trailingZeroes(n / 5)


sol = Solution()
print sol.trailingZeroes(42)


