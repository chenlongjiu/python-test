class Solution(object):
    
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
    def threeSumClosest(self, nums, target):
        if len(nums) < 3:
            return []
        nums = self.quickSort(nums)
        print nums
        if len(nums) == 3:
            return sum(nums)
        mini = float('inf')
        for i in xrange(len(nums)-2):
            left,right, su = i+1, len(nums)-1, target - nums[i]
            while right - left > 0:
                if nums[left] + nums[right] > su:
                    right -= 1
                elif nums[left] + nums[right] < su:
                    left += 1
                else:
                    return target
                    
            if abs(target - sum([nums[i],nums[left],nums[right]])) < abs(target - mini):
                mini = sum([nums[i],nums[left],nums[right]])
                print nums[i],nums[left],nums[right]    
            
        return mini

sol = Solution()
print sol.threeSumClosest([1,1,1,0], 100)
print sol.threeSumClosest([87,6,-100,-19,10,-8,-58,56,14,-1,-42,-45,-17,10,20,-4,13,-17,0,11,-44,65,74,-48,30,-91,13,-53,76,-69,-19,-69,16,78,-56,27,41,67,-79,-2,30,-13,-60,39,95,64,-12,45,-52,45,-44,73,97,100,-19,-16,-26,58,-61,53,70,1,-83,11,-35,-7,61,30,17,98,29,52,75,-73,-73,-23,-75,91,3,-57,91,50,42,74,-7,62,17,-91,55,94,-21,-36,73,19,-61,-82,73,1,-10,-40,11,54,-81,20,40,-29,96,89,57,10,-16,-34,-56,69,76,49,76,82,80,58,-47,12,17,77,-75,-24,11,-45,60,65,55,-89,49,-19,4], -275)
