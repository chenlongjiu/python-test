'''
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space? 
'''
'''import collections
class Solution(object):
    def getRow(self, rowIndex):
    	if rowIndex < 0:return[]
    	queue = collections.deque(maxlen = rowIndex+1)
    	queue.append(1)
    	for i in xrange(1,rowIndex+1):
    		cur,last = 0,0
    		length = len(queue)
    		for _ in xrange(length):
    			n = queue.popleft()
    			queue.append(n+cur)
    			# print queue
    			cur = n
    		queue.append(cur+last)
    	return list(queue)'''


0 votes
58 views

def getRow(self, rowIndex):
    ret = [1] * (rowIndex + 1)
    comb_next = lambda x, m, n: x * (m - n + 1) // n
    for n in range(1, rowIndex // 2 + 1):
        ret[n] = ret[-n-1] = comb_next(ret[n-1], rowIndex, n)
    return ret


# print Solution().getRow(0)
# print Solution().getRow(1)
# print Solution().getRow(2)
print Solution().getRow(3)
print Solution().getRow(100)
