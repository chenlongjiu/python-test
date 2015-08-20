import re
class Solution:
    # @param {string} input
    # @return {integer[]}
    def oprC(self, opr, ele1, ele2):
    	print ele1, ele2
        if opr  == '+':
            result = (ele1 + ele2)
        elif opr == '-':
            result = (ele1 - ele2)
        else:
            result = (ele1 * ele2)
        return result
        
    def getResult(self,ele):
        opr = ['+', '-', '*']
        rel = []
        if len(ele) == 1:
            rel.append(ele[0])
            return rel
        if len(ele) == 3:
        	print ele[1], ele[0], ele[2]
        	rel.append(self.oprC(ele[1], ele[0], ele[2]))
        	return rel
        
        for i in range(len(ele)):
            if ele[i] in opr:
                left = self.getResult(ele[:i])
                right = self.getResult(ele[i+1:])
                for num1 in left:
                    for num2 in right:
                        rel.append(self.oprC(ele[i],num1, num2))
     
        return rel
        
        
        
        
    def diffWaysToCompute(self, input):
        ele = re.findall('[+-/*]|\d+',input)
        for i in range(len(ele)):
            if i%2 == 0:
                ele[i] = int(ele[i])
        return self.getResult(ele)
        
sol = Solution()
print sol.diffWaysToCompute("1+2+3")