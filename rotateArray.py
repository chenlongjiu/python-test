class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        # for rotate an array
        tmp = []
        tmp = nums[-k:]
        for i in range(0, len(nums)-k):
            tmp.append(nums[i])
        return tmp
sol = Solution()
print sol.rotate([1,2],1)

