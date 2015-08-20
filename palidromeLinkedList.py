#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {boolean}
    def isPalindrome(self, head):
        #first judge the 1 or 0 node
        if head is None or head.next is None:
            return True
        # find the mid Node 
        fast, slow = head, head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        #get the mid point 
        midPoint = slow
        endPoint = slow.next
        cur = slow.next.next # first node Doing the insert
        endPoint.next = None
        while(cur is not None): 
            print "adding ", cur.val
            nextNode = cur.next
            cur.next = midPoint.next
            midPoint.next = cur
            cur = nextNode
        
        # judge if the two link list
        left, right = head, midPoint.next
        while (right is not None):
	    print left.val , ',' , right.val
            if left.val == right.val:
                left = left.next
                right = right.next
            else:
                return False
        return True
            

sol = Solution()
head = ListNode(1)
t = head
t.next = ListNode(2)
t = t.next
t.next = ListNode(2)
t = t.next
t.next = ListNode(1)
k = head
while(k is not None):
    print k.val
    k = k.next
print sol.isPalindrome(head)
