class Solution(object):
    def findEnd(self, start, end, target, numbers):
        left, right = start+1, end
        while left + 1 < right:
            print "loop1"
            mid = (left+right)/2
            if numbers[start] + numbers[mid] > target:
                right = mid
            elif numbers[start] + numbers[mid] == target:
                return mid
            else:
                left = mid
        
        return left
    
    def findStart(self, start, end, target, numbers):
        left, right = start, end-1
        while left + 1 < right:
            print "loop2"
            mid = (left+right)/2
            if numbers[end] + numbers[mid] > target:
                right = mid
            elif numbers[end] + numbers[mid] == target:
                return mid
            else:
                left = mid
        return right
            
    def twoSum(self, numbers, target):
        if not numbers:
            return []
        start, end = 0, len(numbers)-1
        while numbers[start] + numbers[end] != target and start + 1 < end:
            print "loop3"
            if numbers[start] + numbers[end] > target:
                end = self.findEnd (start, end, target, numbers)
            elif numbers[start] + numbers[end] < target:
                start = self.findStart(start, end, target, numbers)
            
        print numbers[start], numbers[end]
        if numbers[start] + numbers[end] != target:
            return []
        else:
            return [start+1, end+1]

print Solution().twoSum([1,2,3,4,6,9],9)
