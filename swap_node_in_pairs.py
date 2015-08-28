class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        if head is None or head.next is None:
            return head
        else:
            cur = self.swapPairs(head.next.next)
            first, second = head.next, head
            first.next = second
            second.next = cur
        return first


sol = Solution()
root = ListNode(0)
cur = root
for i in xrange(1,2):
	cur.next = ListNode(i)
	cur = cur.next
rel = sol.swapPairs(root)
while rel:
	print "result val loop" , rel.val
	rel = rel.next