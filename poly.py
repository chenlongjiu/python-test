class listNode:
	def __init__(self, key, value, count):
		self.key = key
		self.val = value
		self.count = count
		self.next = None
		self.front = None

class LRUCache:

	def __init__(self, maxi):
		self.count = 0
		self.pq = []
		self.cache = {}
		self.head = None
		self.tail = None
		self.length = 0
		self.maxi = maxi
	def add(self, key, value):
		self.count += 1
		if not head:
			#add it to the first node
			count += 1
			node = (count, key, value)
			cache[key] = node
			head = node
			tail = node
			return
		elif key in cache:
			node = cache[key]
			if node.front:
				node.front.next = node.next
			if node.next:
				node.next.front = node.front
				node.next = None
			
		else:
			node = (count, key, value)
			if self.length == self.maxi
				head = head.next
				head.front = None
		tail.next = node
		node.front = tail
		tail = node
		return
	def get(self,key):
		if key in cache:
			node = cache[key]
			if head == node:
				head = head.next
				head.front = None
				node.next = None
				
