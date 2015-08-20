#check if two link list converage
class listNode:
	def __init__(self, val):
		self.val = val
		self.next = None

head1 = listNode(10)
head2 = listNode(20)
head1.next = head2

def check(h1, h2):
	p1, p2 = h1, h2
	while p1.next is not None:
		p1 = p1.next
	while p2.next is not None:
		p2 = p2.next

	if p1 == p2:
		return True
	else:
		return False

print check(head1, head2)