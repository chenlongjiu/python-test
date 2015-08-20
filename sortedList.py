import random
random.seed(23)
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        #constant space
        if head is None:
            return
        copy = []
        pr = head
        #O(n)
        while pr is not None:
            copy.append((pr.val, pr))
            pr = pr.next
        # copy contains val and address of one node
        copy = sorted(copy)#O(nlgn) time can use quick sort
        for i in range(len(copy)-1):
            _, adr = copy[i]
            adr.next = copy[i+1][1]
        copy[-1][1].next = None
	head = copy[0][1]
        return head
head = ListNode(10)
pr = head
for i in range(10):
	val = random.randrange(100)
	ct = ListNode(val)
	pr.next = ct
	pr = pr.next
sol = Solution()
t =  sol.sortList(head)
while t is not None:
	print t.val
	t = t.next
