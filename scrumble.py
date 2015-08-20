class Solution:
    # @return a boolean
    def isScramble(self, s1, s2):
	print "this is s1", s1, "this is s2", s2
        if len(s1) != len(s2) or len(s1) == 0 or len(s2) == 0:
            return False
        if s1 == s2:
            return True
        if sorted(s1)==sorted(s2):
            for i in range (len(s1)-1):
		print s1[0:i+1], s2[len(s2)-i-1:],s1[len(s1)-i-1:], s2[0:i+1]
                if self.isScramble(s1[0:i], s2[0:i]) and self.isScramble(s1[i+1:],s2[i+1:]):
                    return True
                if (self.isScramble(s1[0:i+1], s2[len(s2)-i-1:]) and self.isScramble(s1[len(s1)-i:], s2[0:i])):
                    return True
        return False
print Solution().isScramble("abc","bca")
