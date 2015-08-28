# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val <= l2.val:
            root,cur = l1,l1
            l1 = l1.next
            print "l1 smaller than l2 and attached l1", l1.val, l2.val
        else:
            root,cur = l2, l2
            l2 = l2.next
            print "l2 smaller than l1 and attached l2", l1.val, l2.val
        while l1 or l2:
            if l1 is None:
                print "l1 is None attached l2"
                cur.next = l2
                return root
            if l2 is None:
                cur.next = l1
                return root
            if l1.val <= l2.val:
                print l1.val, l2.val
                cur.next = l1
                l1 = l1.next
            else:
                print "l2 smaller than l1 and attached l2", l1.val, l2.val
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        return root

val1, val2 = [1,2,4], [5]
l1 = ListNode(0)
l2 = ListNode(5)
cur = l1
while val1:
    cur.next = ListNode(val1.pop(0))
    cur = cur.next
cur = l1
while cur:
    print cur.val
    cur = cur.next
sol = Solution()
rel = sol.mergeTwoLists(l1,l2)
while rel:
    print rel.val
    rel = rel.next 