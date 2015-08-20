#Search Insert Position 

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        min = 0
        max = len(A)
        while True:
        	i = int((max+min)/2)
        	print max, min, i
        	if (max - min) == 1:
        		if A[min] >= target:
        			return min
                else: return max
			if A[i] > target:
                max = i
            elif A[i] < target:
                min = i
            if A[i] == target:
                return i-1
sol = Solution()
print sol.searchInsert([1,3],0)

