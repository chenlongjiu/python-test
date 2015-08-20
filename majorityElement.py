
class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        self.diction = {}
        for i in range (len(num)):
			if num[i] in self.diction.keys():
				self.diction[num[i]] += 1
			else:self.diction[num[i]] = 1
        
        max = 0
        if len(num)%2 > 0 :
            edge = len(num)/2+1
        else: 
            edge = len(num)/2
        print "self.cition is ",self.diction
        for x in self.diction.keys():
        	if self.diction[x] >= edge:return x

        return

sol = Solution()
print sol.majorityElement((8,8,7,7,7))

        

