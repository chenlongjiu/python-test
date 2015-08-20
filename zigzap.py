import itertools
class Solution:

    # @return a string
    def convert(self, s, nRows):
        #group should be 2*Rows
        if nRows ==1:
            return s
        else:
            basesequence = itertools.chain(range(nRows), range(nRows-2,0,-1))
            rel = ['']*nRows
            for char, index in itertools.izip(s,itertools.cycle(basesequence)):
                rel[index] += char
        print rel    
	return "".join(rel)
sol = Solution()
print sol.convert("abcd",3)

