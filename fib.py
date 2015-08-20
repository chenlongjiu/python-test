def fib(term, val = 1, prev = 0):
    if term == 0:
	return prev
    if term == 1:
	return val
    if term >= 2:
	print val
	return fib(term-1, val+prev, val)
print fib(19)

