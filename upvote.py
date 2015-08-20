import sys

def upvote():
	#data processing

	x, y = map(int,sys.stdin.readline().split())
	num = map(int,sys.stdin.readline().split())

	# each step will print result 
	val = 0

	start = 0
	mark = [0]*y

	#if window size is less than 2
	if y < 2:
		for _ in range(len(num)) :
			print 0 
		return
	#if window size is equal to 2
	if y == 2:
		for start in range(len(num)-1):
			if num[start] > num[start+1]:
				print -2 
			if num[start] < num[start-1]:
				print 2
		return

	#if window size is larger than 2
	if y > 2:
		for i in range(start,start+y):
			if  i > 0 and num[i] > num[i-1] and mark[i-start] < 1:
				mark[i-start] += 1 
			elif i > 0 and num[i] < num[i-1] and mark[i-start] > -1:
				mark[i-start] -= 1 
			
			if i+1 < start+y and num[i] > num[i+1] and mark[i-start] > -1:
				mark[i-start] -= 1 
			elif i+1 < start+y and num[i] < num[i+1] and mark[i-start] < 1:
				mark[i-start] += 1 

	for ele in mark:
		val += ele 
	print val
	while(start+1 < x -y +1):
		start += 1
		#compare head:
		if num[start] > num[start+1]:
			val -= (mark[0] + 1)
			mark[1] = -1
		elif num[start] == num[start+1]:
			val -= mark[0]
		else:
			val -= (mark[0]-1)
		print mark
		mark[0:-1] = mark[1:]
		print mark
		if num[start+y-1] < num[start+y-2]:
			mark[-1] = -1
			if mark[-2] > -1:
				mark[-2] -= 1
				val -= 1

		elif num[start+y-1] > num[start+y-2]:
			mark[-1] = 1
			if mark[-1] < 1:
				mark[-2] += 1
				val += 1
		else:
			mark[-1] = 0
		val += mark[-1]
		print val
	return

upvote()
