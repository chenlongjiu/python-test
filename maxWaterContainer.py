class Solution:
    # @return an integer
    def maxArea(self, height):
        # container's height should be the shorter line
        if height is None:
            return 
        if len(height) < 2:
            return 
        else:
            right = len(height)-1
            maxi = 0
            index = 0
            while index < right :
                maxi = max(maxi, (right - index)*min(height[index],height[right]))
                if height[index] > height[right]:
                    right -= 1
                elif height[index] <= height[right]:
                    index += 1
            return maxi
