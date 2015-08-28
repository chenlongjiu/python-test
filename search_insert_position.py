class Solution(object):
    def searchInsert(self, nums, target):
        if not nums:
            return 0
        index = 0
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        left, right = 0, len(nums)-1
        while right > left:
            mid = (right + left) / 2
            if nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return left

print Solution().searchInsert([1,3,5], 2)