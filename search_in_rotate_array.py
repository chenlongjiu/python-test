class Solution(object):
    def search(self, nums, target):
    	if not nums:
    		return -1
    	elif len(nums) == 1:
    			return 0 if target == nums[0] else -1

    	#find pivot
    	left, right,index = 0, len(nums)-1, -1
    	while right > left:
    		mid = (left + right) / 2
    		if nums[mid] > nums[mid+1]:
    			index = mid	
    			break
    		if nums[mid] >= nums[0] and nums[mid+1] > nums[mid]:
    			left = mid+1

    		elif nums[mid] < nums[0]:
    			right = mid
    	if index == -1:
    		rL,rR = 0, len(nums)-1
    	else:
	    	if target > nums[0]:
	    		rL, rR = 0, index
	    	elif target == nums[0]:
	    		return 0
	    	else:
	    		rL, rR = index+1, len(nums)-1

    	while rR >= rL:
    		mid = (rL+rR)/2
    		if nums[mid] == target:
    			return mid
    		elif nums[mid] < target:
    			rL = mid + 1
    		else:
    			rR = mid - 1
    	return -1

sol = Solution()
print sol.search([1,3],1)
