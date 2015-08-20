import copy

s1 = set("abcde")
print "s1 = ", s1

s2 = copy.deepcopy(s1)
s1.add(34)
print s1, s2 


class Counter(dict):
	def __missing__(self,key):
		return 0
c = Counter()

