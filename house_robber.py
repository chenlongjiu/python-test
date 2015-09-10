'''
Note: This is an extension of House Robber.

After robbing those houses on that street, the thief has found himself a new place for his thievery so that he will not get too much attention. This time, all houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, the security system for these houses remain the same as for those in the previous street.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

'''


class Solution(object):
    def rob(self, nums):
        #exclude 1st and include last
        #exclude last and include first
        dp_first = [0] * len(nums)
        dp_last = [0] * len(nums)
        dp_first[1] = nums[0]
        dp_last[1] = nums[1]
        for i in xrange(2, len(nums)):
        	dp_first[i] = max(dp_first[i-1], dp_first[i-2]+nums[i-1])
        	dp_last[i] = max(dp_last[i-1], dp_last[i-2]+nums[i])
        print dp_first, dp_last
        return max(dp_first[-1], dp_last[-1])
        """
        :type nums: List[int]
        :rtype: int
        """
        
print Solution().rob([1,2,3,4,5,6,7,8,9,10])