import collections
class Solution:
    # @param s, a string
    # @return a list of strings
    def findRepeatedDnaSequences(self, s):
        seq = collections.Counter(s[i:i+10] for i in range(len(s)))
        #[key for key, value in sequences.iteritems() if value > 1]
        return [i for i,v in seq.iteritems() if v > 1]
        
sol = Solution()
st= "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
print sol.findRepeatedDnaSequences(st)
