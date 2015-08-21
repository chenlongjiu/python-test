import collections

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        if len(nums) == 0:
            return []
        window = collections.deque(nums[0:k],maxlen = k)
        maxQ = collections.deque([0])
        rel = [] # result
        #initialize the queue 
        for i in range(1,k):
            while len(maxQ) > 0 and window[i] > nums[maxQ[-1]]:
                maxQ.pop()
            maxQ.append(i)
        rel.append(nums[maxQ[0]]) # first one is the biggest num in the queue
        
        for i in range(k,len(nums)):
            if nums[maxQ[0]] == window[0]:
               maxQ.popleft()
            window.append(nums[i])
            while len(maxQ) > 0 and window[-1] > nums[maxQ[-1]]:
                maxQ.pop()
            maxQ.append(i)
            while maxQ[0] < i-k+1:
                maxQ.popleft()
            print nums[maxQ[0]] , maxQ, window
            rel.append(nums[maxQ[0]])
        return rel

sol = Solution()
print sol.maxSlidingWindow([1,2,3,1,1,4,2,3,5,6,7], 3)