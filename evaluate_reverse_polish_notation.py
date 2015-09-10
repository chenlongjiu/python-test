
class Solution(object):
	def cal(self, digit, mark):
	# 	print digit, mark
		d2 = digit.pop()
		d1 = digit.pop()
		if mark == '+':
			digit.append(d1+d2)
		if mark == '-':
			digit.append(d1-d2)
		if mark == '*':
			digit.append(d1*d2)
		if mark == '/':
			res = abs(d1)/abs(d2)
			if not ((d1 > 0) is (d2 > 0)):
				res = -res
			digit.append(res)
		# print digit
		return
	def evalRPN(self, tokens):
		digit = []
		sign = ['+','-','*','/']
		for index in xrange(len(tokens)):
			tmp = tokens[index]
			if tmp  not in sign:
				digit.append(int(tmp))
			else:
				self.cal(digit,tmp)
		return digit[0]		

# test = ["2","1","+","3","*"]
# test = ["-78","-33","196","+","-19","-","115","+","-","-99","/","-18","8","*","-86","-","-","16","/","26","-14","-","-","47","-","101","-","163","*","143","-","0","-","171","+","120","*","-60","+","156","/","173","/","-24","11","+","21","/","*","44","*","180","70","-40","-","*","86","132","-84","+","*","-","38","/","/","21","28","/","+","83","/","-31","156","-","+","28","/","95","-","120","+","8","*","90","-","-94","*","-73","/","-62","/","93","*","196","-","-59","+","187","-","143","/","-79","-89","+","-"]
test  = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print Solution().evalRPN(test)