# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insert(self, D, prenode, cur):
        prev = D
        prenode.next = cur.next
        while prev.next != cur:
            if prev.val < cur.val and prev.next.val >= cur.val:
                cur.next =prev.next
                prev.next = cur
                return
            else:
                prev = prev.next
            
    def insertionSortList(self, head):
        D = ListNode(-float('inf'))
        D.next = head
        cur = D
        while cur.next is not None:
            # print "loop"
            if cur.next.val >= cur.val:
                # print "next step"
                cur = cur.next
            else:
                self.insert(D, cur, cur.next)
                # print cur.next
        return D.next
        """
        :type head: ListNode
        :rtype: ListNode
        """
    
start = ListNode(2)
start.next = ListNode(1)
print Solution().insertionSortList(start).val