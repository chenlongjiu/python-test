'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example,
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6. 
'''

class Solution(object):
    def trap(self, height):
    	left, right , mHeight , rel  = 0, len(height)-1, 0, 0
    	if len(height) == 0:
    		return 0
    	while left < right:
    		while left < right and height[left] <= mHeight:
    			#print "left position", left, right
    			rel += mHeight-height[left]
    			left += 1
    			
    		while left < right and height[right] <= mHeight:
    			#print "right movement", left, right
    			rel += mHeight - height[right]
    			right -= 1
    			
    		mHeight = min(height[left], height[right])
    	return rel
        """
        :type height: List[int]
        :rtype: int
        """
print Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1])