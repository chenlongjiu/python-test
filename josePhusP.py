#Josephus problem
def jose(n,k):
	if n == 1:
		return 1
	else:
		s = 1
		for t in range(n-1):
			s = (s+k-1)%(t+2) + 1
			print s
		#s = (jose(n-1, k) + k -1)%n + 1
		return s
		# return the survivor man's position and it's next is the survivor
n, k = input(), input()
print jose(n,k)
