import bisect
class Solution(object):

    def searchRange(self, nums, target):
        lo = bisect.bisect_left(nums, target)
        hi = bisect.bisect_right(nums,target)
        return[lo,hi-1] if hi > lo else [-1,-1]

sol = Solution()
print sol.searchRange([2,2], 3)