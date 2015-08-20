#find a substring in substring
s1 = "hello"
s2 = "yes"+s1
s3 = "helo"
def find(s1, s2):
	l = len(s1)
	for i in range(len(s2)):
		if s2[i] == s1[0]:
			if s1==s2[i:i+l+1]:
				return True
	return False
print find(s1, s3)