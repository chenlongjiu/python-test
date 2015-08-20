#Square root
def sqrT(n):
	if n < 0:
		return False
	if n == 0 or n == 1:
		return n
	maxi = 1
	while maxi**2 < n:
		maxi *= 2
	mini = maxi / 2
	print maxi, mini
	#get upper board and lower board
	target = (maxi+mini)/2
	while True:
		print maxi, mini
		if maxi - mini == 1:
			return target
		if target**2 > n:
			maxi = target
			target = (maxi+mini)/2
		elif target ** 2 < n:
			mini = target
			target = (maxi+mini)/2
		elif target**2 == n:
			return target
print sqrT(120)