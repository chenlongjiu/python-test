class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        step = 0
        rel = 0
        while n-m >= (1 << step):
            step += 1
            print "step is ", step
        
        #for first step -1 digit is 0
        print step,m&n,  (m&n) >> (step-1), (m&n) >> (step-1) << (step -1)
        if step == 0:
            return m
        rel += (m&n) >> (step) << (step ) 
        return rel

print Solution().rangeBitwiseAnd(3,6)