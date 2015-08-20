class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):
        def largeRectangle(height):
            height.append(0)
            # for final calculate
            stack, size = [0], 0
            #stack for saving the stack shorter than the latest one
            for i in range(1, len(height)):
                while stack and height[i] < height[stack[-1]]:
                    h = height[stack.pop()]
                    if not stack:
                        w = i
                    else:
                        w = i - stack[-1] - 1
                    size = max(size, h*w)
                stack.append(i)
            return size
        maxi = 0
        h = len(matrix)
        if h == 0:
            w = 0
        else:
            w = len(matrix[0])
        # get the value for all the length and width
        #inital a height map 
        m = [[0]*w for _ in range(h)]
        for k in range(w):
            if matrix[0][k] == 1:
                m[0][k] = 1
        for i in range(1, h):
            for j in range(w):
                if matrix[i][j] == 1:
                    m[i][j] = m[i-1][j] + 1
        for row in m:
            maxi = max(maxi, largeRectangle(row))
        return maxi

sol = Solution()
sol.maximalRectangle(["1"])