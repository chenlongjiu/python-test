class Node:
	next = None
	data = None
	def __init__(self,nodeData):
		self.data = nodeData

class List:
	root = None
	size = 0
	def __init__(self,newRoot):
		#what is newRoot and nodeData
		self.root = newRoot
	def __init__(self):
		self.root = None
		self.size = 0
	#define delete function
	def __del__(self):
		if self.root is None: 
			return
		curNode = self.root
		while curNode.next is not None:
			tempNode = curNode
			curNode = curNode.next
			tempNode = None # this is delete nodeData
		curNode = None

	#insert new node to the List
	def Insert(self,newData):
		newNode = Node(newData)
		if self.root == None:
			self.root = newNode
			return 
		tempNode = self.root
		while tempNode.next is not None:
			tempNode = tempNode.next
		if tempNode.next is None:
			tempNode.next = newNode
			self.size = self.size+1

	#def Get data of Position pos
	def GetData(self,pos):
		if pos > self.size:
			return None
		tempNode = None
		while i in (0,pos):
			tempNode = tempNode.next
		return tempNode.data

	def Remove(self,theData):
		curNode = self.root 
		if curNode is None:  
			return  
		if self.size == 1 and curNode.data == theData:  
			curNode.data = None  
			curNode = None  
			self.size -= 1  
			return  
		while curNode.next is not None:  
			if curNode.next.data == theData:  
				tempNode = curNode.next  
				curNode.next = curNode.next.next  
				tempNode = None  #remove the node,but curNode stays still  
				self.size =self.size + 1  
				return
			else:
				curNode = curNode.next
				return

	def GetRoot(self):
		return self.root
 
	def GetSize(self):
		return self.size  

	def Print(self):
		tempNode = self.root  
		while tempNode is not None:  
			print (tempNode.data)  
			tempNode = tempNode.next    


def main():  
	print ("start main()")  
	mylist = List()  
	for i in range(0,10):  
		mylist.Insert(i)  
	mylist.Print()  
	mylist.Remove(1)  
	mylist.Print()  
	 
  
#main()  




