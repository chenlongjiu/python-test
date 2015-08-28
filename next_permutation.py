class Solution(object):
    def nextPermutation(self, nums):
        if not nums:
            return
        if len(nums) == 1:
            return
            
        for i in xrange(len(nums)-2, -1, -1):
            if nums[i] >= nums[i+1]:
                pass
            else:
                for k in xrange(len(nums)-1, i,-1):
                    if nums[k] > nums[i]:
                        nums[k],nums[i] = nums[i],nums[k]
                        for t in xrange(1,(len(nums)-i)/2+1):
                            nums[i+t],nums[-t] = nums[-t],nums[i+t]
                        return
        nums.reverse()
        return
sol = Solution()
print sol.nextPermutation([3,2,1])
print sol.nextPermutation([2,3,1])
print sol.nextPermutation([1,2,3])
print sol.nextPermutation([1,4,5,2,2,3])