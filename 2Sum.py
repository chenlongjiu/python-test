class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, nums, target):
        dic = {}
        for i, num in enumerate(nums,1):
            val = dic.get(target-num)
            if val != None:
                return (i, val)
            else:
                dic[num] = i
            
            
        
print sol.twoSum([5,75,25], 100)
