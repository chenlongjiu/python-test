#multiple array
import random
lt = []
for i in range(5):
	s = []
	for k in range(random.randrange(1,3)):
		s.append(random.randrange(100))
	lt.append(sorted(s))
print lt
def median(lt):
	l = 0
	for i in lt:
		l += len(i)
	if l % 2 == 0:
		left = l/2
		right = l/2+1
	else:
		left = right = (l+1)/2 
	print left, right
	#median position
	p = [0]*len(lt)
	#start a pointer to get index of all the median
	counter = 1
	while counter <= (l+1)/2+1:
		cp = []
		#compare the smallest one in this round
		for i in range(len(lt)):
			#print p[i]
			if p[i] == len(lt[i]):
				pass
			else:
				cp.append((lt[i][p[i]],i))
		rel = min(cp)
		#print rel
		p[rel[1]] += 1
		print rel
		if counter == left:
			left = rel[0]
		if counter == right:
			right = rel[0]
		counter += 1

	return (left+right)/2



print median(lt)


