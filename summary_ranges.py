'''
Given a sorted integer array without duplicates, return the summary of its ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
'''

class Solution(object):
    def summaryRanges(self, nums):
        if not nums:
            return []
        if len(nums)==1:
            return [str(nums[0])]
        start , i = 0, 0
        end = start
        tmp = []
        while i < len(nums):
            if i+1 < len(nums) and nums[i] + 1 == nums[i+1]:
                end = i+1
            else:
                if start == end:
                    tmp.append(str(nums[start]))
                else:
                    tmp.append(str(nums[start])+"->"+str(nums[end]))
                    # tmp.append("->".join([str(nums[start]),str(nums[end])]))
                start , end= i+1, i+1
            i += 1
        return tmp
        
        
        
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        