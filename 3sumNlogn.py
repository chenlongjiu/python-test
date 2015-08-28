class Solution(object):
    def check(self, sumup, nums, rel):
        #nums contain the rest of the sum
        left, right = 0, len(nums)-1
        
        while right - left > 0:
            if nums[left] + nums[right] > sumup:
                right -= 1
            elif nums[left] + nums[right] < sumup:
                left += 1
            else:
                if [-sumup, nums[left],nums[right]] not in rel:
                    rel.append([-sumup, nums[left], nums[right]])
                if nums[left] == nums[left+1]:
                    while nums[left] == nums[left+1]:
                        left += 1
                        if left == right:
                            return
                else:
                    left += 1
        
        #want to write a binary search
        return
    
    
    def quickSort(self, nums): # time complexity is O(nlogn)
        if len(nums) <= 1:
            return nums
        else:
            left, right, equal = [], [], []
            for ele in nums:
                if ele > nums[0]: 
                    right.append(ele)
                elif ele < nums[0] : 
                    left.append(ele)
                else:
                    equal.append(ele)
            return self.quickSort(left) + equal + self.quickSort(right)

    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        
        
        nums = self.quickSort(nums)
        if len(nums) == 3 and sum(nums) == 0:
            return [nums]
        rel = []
        
        for index1 in range(0,len(nums)-2):
            if nums[index1] > 0 : 
                return rel
            self.check(-nums[index1],nums[index1+1:],rel)

        return rel


sol = Solution()
print sol.threeSum([8,-15,-2,-13,8,5,6,-3,-9,3,6,-6,8,14,-9,-8,-9,-6,-14,5,-7,3,-10,-14,-12,-11,12,-15,-1,12,8,-8,12,13,-13,-3,-5,0,10,2,-11,-7,3,4,-8,9,3,-10,11,5,10,11,-7,7,12,-12,3,1,11,9,-9,-4,9,-12,-6,11,-7,4,-4,-12,13,-8,-12,2,3,-13,-12,-8,14,14,12,9,10,12,-6,-1,8,4,8,4,-1,14,-15,-7,9,-14,11,9,5,14])

        