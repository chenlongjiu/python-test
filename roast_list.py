'''
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        if head is None or k == 0:
            return head
        test, last, first = head, head, head
        depth = 1
        #detect the lenght of the list
        while test.next is not None:
            depth += 1
            test = test.next
        k %= depth
        if k == 0:
            return head
        k = depth - k
        first = first.next
        for _ in xrange(k-1):
            first = first.next
            last = last.next
        test.next = head
        last.next = None
        return first
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        