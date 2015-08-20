class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        total = 0
        length = len(s)
        for letter in s:
            total += (ord(letter)-ord('A')+1)*(26**(length-1))
            length -= 1
        return total

solu = Solution()
print solu.titleToNumber('AD')