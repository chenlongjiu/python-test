import collections
class Solution(object):
    def countAndSay(self, n):
        if n <= 0:
            return 
        start = '1'
        cur = collections.deque([start])
        for t in xrange(1,n):
            cnt = 0
            mark = None
            tmp = collections.deque()
            while cur:
                p = cur.popleft() 
                if mark is None:
                    mark = p
                    cnt += 1
                    
                elif mark == p:
                    cnt += 1
                else:
                    
                    tmp.append(str(cnt))
                    tmp.append(mark)
                    cnt = 1
                    mark = p
            tmp.append(str(cnt))
            tmp.append(mark)
            cur = tmp
            
        return "".join(cur)

print Solution().countAndSay(0)