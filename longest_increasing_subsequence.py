class Solution:
    """
    @param nums: The integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        # write your code here
        #f[i] the longest value end with i
        if not nums:
            return 0
        f = [0]*len(nums) # how many subsequence nodes at that position
        f[0] = 1
        for i in xrange(1,len(nums)):
            for k in xrange(0,i):
                if nums[i] >= nums[k]:
                    f[i] = max(f[k],f[i])
            f[i] += 1
        print f
        return f[-1]


Solution().longestIncreasingSubsequence([88,4,24,82,86,1,56,74,71,9,8,18,26,53,77,87,60,27,69,17,76,23,67,14,98,13,10,83,20,43,39,29,92,31,0,30,90,70,37,59])