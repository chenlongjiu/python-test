import collections
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
    	cur = head
    	for _ in xrange(k):
    		if cur is None:
    			return head
    		cur = cur.next
    	nextNode = self.reverseKGroup(cur, k)
    	queue = collections.deque(maxlen = k)
    	cur = head
    	for _ in xrange(k-1):
    		queue.append(cur)
    		cur = cur.next
    	reverHead = cur
    	while queue:
    		cur.next = queue.pop()
    		cur = cur.next
    	cur.next = nextNode
    	return reverHead



sol = Solution()
root = ListNode(0)
cur = root
for i in xrange(1,10):
	cur.next = ListNode(i)
	cur = cur.next
#rel = sol.reverseKGroup(root,3)
rel = sol.reverseKGroup(ListNode(1),1)
while rel:
	print "result val loop" , rel.val
	rel = rel.next