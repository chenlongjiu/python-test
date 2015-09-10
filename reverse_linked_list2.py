'''
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list. 
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def reverseBetween(self, head, m, n):
		H, D = ListNode(0),ListNode(0)
		D.next = H
		H.next = head
		for _ in xrange(m-1):
			D.next = D.next.next
		#D.next.next = startNode
		p1,p2= D.next.next, D.next.next.next
		end = m+1
		while end <= n:
			#keep going
			p2,p2.next,p1= p2.next,p1,p2
		D.next.next.next = p2
		D.next.next = p1
		return H.next



		






		
		"""
		:type head: ListNode
		:type m: int
		:type n: int
		:rtype: ListNode
		"""
