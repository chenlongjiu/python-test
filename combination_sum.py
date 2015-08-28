class Solution(object):
    def check(self, candidates, target, cur):
        if target == 0:
            return [[]]
        if target < 0:
            return False
        rel = []
        for t in xrange(cur, len(candidates)):
            tmp = self.check(candidates, target-candidates[-t-1],t)
            if tmp == False:
                pass
            else:
                for ele in tmp:
                    ele.append(candidates[-t-1])
                rel += tmp
                print rel
        return rel
        
    def combinationSum(self, candidates, target):
        rel = []
        for i in xrange(len(candidates)):
            tmp = self.check(candidates, target - candidates[-1-i], i) 
            if not tmp:
                pass
            else:
                for ele in tmp:
                    ele.append(candidates[-1-i])
                    ele = ele[::-1]
                rel += tmp
        return rel

print Solution().combinationSum([92,71,89,74,102,91,70,119,86,116,114,106,80,81,115,99,117,93,76,77,111,110,75,104,95,112,94,73], 310)