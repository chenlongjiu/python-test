
#stastic window size:
import random
random.seed(23)
ts =[]
ip =[]
for i in range(200):
	ts.append((random.randrange(70), random.randrange(100,199)))
ts = sorted(ts)
# all two stamp is there
def check(ts, ip):
	rel = []
	for i in range(0,len(ts)-1):
		if ts[i][1] == ip:
			rel.append(i)
	#so far we get all candidate element
	target = 2
	if len(rel) < target:
		return False
	window = max(rel[target-1]+1, len(ts)+1-rel[-target])
	for i in range(0, len(rel)-3):
		window = max(rel[i+3] - rel[i] + 1, window)
	return window


	
for i in range(100, 200):
	print check(ts, i)

