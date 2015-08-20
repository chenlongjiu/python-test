class Solution:
	arr = []
	def calBase(self,digit):
		self.arr.append([])
		if digit == 1:
			for i in range(10):
				self.arr[digit-1].append(str(i))
			print self.arr
		else:
			#all the word are combine with the digit -1
			self.calBase(digit-1)
			# now you get all the level below
			for i in range(10):
				for x in self.arr[digit-2]:
					t = str(i)+x
					self.arr[digit-1].append(t)

			print self.arr

t = Solution()
t.calBase(4)