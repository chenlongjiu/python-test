#reverse hte words in a string
s = "hello my friend"
t = []
for i in range(len(s)-1,-1,-1):
	t.append(s[i])
print "".join(t)