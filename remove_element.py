class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        nums = [ele for ele in nums if ele^val != 0]
        return len(nums)

sol = Solution()
print sol.removeElement([],0)