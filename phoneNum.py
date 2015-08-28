class Solution(object):
    def letterCombinations(self, digits):
    	num = ['1','2','3','4','5','6','7','8','9','0','*','#']
    	words = ['1','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz',' ','*','#']
    	rel = ['']
    	for alp in digits:
    		if alp not in num:
    			return False
    		length = len(rel)
    		for _ in xrange(length):
    			cur = rel.pop(0)
    			for i in xrange(len(words[num.index(alp)])):
    				rel.append("".join([cur,words[num.index(alp)][i]]))

    	return rel

sol = Solution()
print sol.letterCombinations("334")