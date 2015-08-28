class Solution(object):
    def firstMissingPositive(self, nums):
        if len(nums) == 0:
            return 1
        i = 0
        while i < len(nums):
            print i, nums
            if nums[i] < 1 or nums[i] >= len(nums) or nums[i] == i+1 or nums[i] == nums[nums[i]-1]:
                pass
            else:
                left , right = i, nums[i]-1
                nums[left], nums[right] = nums[right], nums[left]# = nums[nums[i]-1], nums[i] use this as index, it will change since the first value get changed means the nums[i]-1 will change to some unexpected value
                if nums[i] != i+1:
                    print nums[i] , i
                    i -= 1
            i += 1
            print "i is ", i
        for cnt in xrange(len(nums)):
            if nums[cnt] != cnt+1:
                return cnt+1
        return len(nums)+1

print Solution().firstMissingPositive([0,2,2,1,1])