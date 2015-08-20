def sortT(st):
	n = st.split(',')
	for i in range(len(st)):
		s[i] = int(s[i])
	

with open("workfile","r+w") as f:
	readData = True
	while readData:
		readData = f.readline()
		print readData
