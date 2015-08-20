class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None




class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        curB = None
        cur = head
        flag = True
        if( cur is None or cur.next is None):
            return cur
        else:
           
            while(cur.next is not None):
                if(cur.val == cur.next.val):
                    print("cur b has duplicate  value", cur.next.val)
                    flag = False
                    if(cur.next.next is not None):
                        cur.next = cur.next.next
                    else:
                        return curB
                else:
                    print("cur b has unique  value", cur.next.val)
                    if(flag):
                        if(curB is None):
                            print("cur b has got the first value", cur.val)
                            curB = cur
                        else:
                            print("cur b has got the other value", curB.val)
                            curB.next = cur
                            curB = curB.next
                    cur = cur.next
                    flag = True
            if(flag):
                if(curB is None):
                    #print("cur b has got the first value", cur.val)
                    curB = cur
                else:
                    #print("cur b has got the other value", cur.val)

                    curB.next = cur
            
            return curB
            
sol = Solution()
head = ListNode(0)
cur = head
for i in range(1, 4):
    cur.next = ListNode(i)
    cur = cur.next
cur = head

cur = sol.deleteDuplicates(head)
while(cur is not None):
    print ("value for next node is" , cur.val)
    cur = cur.next

