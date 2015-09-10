class Solution(object):
    def maximumGap(self, nums):
        if len(nums) < 2:
            return 0
        minE, maxE = [float('inf')]*len(nums) , [-float('inf')] * len(nums)
        maxi, mini = max(nums), min(nums)
        divisor = float(maxi-mini)/float(len(nums)-1)
        for ele in nums:
            index = int(float(ele-mini) / float(divisor))
            print ele, index, divisor, maxE[index], minE[index]
            maxE[index], minE[index] = max(maxE[index], ele), min(minE[index],ele)
            print ele, index, divisor, maxE[index], minE[index]
        print maxE, minE
        #set up a loop to check all the values' gap
        maxGap, prev = 0, maxE[0]
        for index in xrange(1, len(nums)):
            if minE[index] == float('inf'):
            	print "gap value"
                continue
            else:
                maxGap = max(maxGap, minE[index] - prev)
                prev = maxE[index]
        return maxGap
            
        
        
        """
        :type nums: List[int]
        :rtype: int
        """
        
print Solution().maximumGap([100,3,2,1])