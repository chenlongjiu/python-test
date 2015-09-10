'''
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3. 
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        dummy,prehead = ListNode(0),ListNode(0)
        prehead.next = head
        dummy.next = prehead
        cur = head
        if head is None:
            return head
        while cur is not None and cur.next is not None:
            if cur.val != cur.next.val:
                dummy.next = cur
                cur = cur.next
            else:
                while cur.next is not None and cur.val == cur.next.val:
                    cur = cur.next
                dummy.next.next = cur.next
                cur = cur.next # makes cur is None
        return prehead.next
                    
        
        
        """
        :type head: ListNode
        :rtype: ListNode
        """
        