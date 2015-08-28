class Solution(object):
    def switchValue(self, array, value):
        if value >= array[0]:
            array = [value] + array[0:-1]
            return array
        if value < array[-1]:
            return array
        '''
        for i in range(len(array)):
            if value > array[i]:
                array = array[:i] + [value] + array[i:-1]
                break
        return array
        '''
        if len(array) == 1:
            array[0] = max(array[0],value)
            return array
        else:
            left, right = 0, 1
            while value < array[right]: 
                left = right
                right *= 2
                if right >= len(array):
                    right = len(array)-1
                    break
            # left and right
            while right - left > 1:
                # print right, left
                if value >= array[(right+left)/2]:
                    right = (right+left) /2 
                else:
                    left = (right+left) / 2
            if array[right] > value:
                left = right
            # print left, right,value
            # print array[:left+1], [value], array[left+1:-1]
            array = array[:left+1]+ [value] + array[left+1:-1]
            # print array, value
            
            return array
        
     
    def findKthLargest(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: int
		"""
		if len(nums) == 0:
			return 
		
		max_array = [min(nums[:k])] * k
		for i in xrange(0,len(nums)): # start a loop for treavel all the elements in nums array
		    max_array = self.switchValue(max_array,nums[i])
		    
		    
		return max_array[-1]

sol = Solution()
print sol.findKthLargest([7,6,5,4,3,2,1], 5)