import collections
class Solution(object):
    def switchValue(self, array, value):
        if value >= array[0]:
            array = [value] + array[0:-1]
            return array
        if value < array[-1]:
            return array
        for i in range(len(array)):
            if value > array[i]:
                array = array[:i] + [value] + array[i:-1]
                break

        return array
        '''
        left, right = 0 , 1
        while value < array[right]: 
            left = right
            right *= 2
            if right >= k:
                right == k-1
                break
        # left and right
        while right - left <= 1:
            if value >= array[(right+left)/2]:
                left = (right+left) /2 
            else:
                right = (right+left) / 2
            
        array = array[:left+1]+ [value] + array[left+1:-1]
        return
        '''
     
    def findKthLargest(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: int
		"""
		if len(nums) == 0:
			return 
		
		max_array = [min(nums)] * k
		for i in xrange(0,len(nums)): # start a loop for treavel all the elements in nums array
		    max_array = self.switchValue(max_array,nums[i])
		    print max_array, nums[i]
		    
		return max_array[-1]


sol = Solution()
print sol.findKthLargest([-1,2,0], 3)