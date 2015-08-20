class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        def check(st, stack):
            if len(stack) < 2:
                return False
            a1 = stack.pop()
            a2 = stack.pop()
            if st == "+":
                stack.append(a2+a1)
		print a2,"+",a1,"=",a1+a2
            if st == "-":
                stack.append(a2-a1)
		print a2,"-",a1,"=",a2-a1 
            if st == "*":
                stack.append(a1*a2)
		print a2,"*",a1,"=",a1*a2
            if st == "/":
		if abs(a1)>abs(a2):
			print a2,"/",a1,"=0"
			stack.append(0)
		else:
                	stack.append((a2)/(a1))
			print a2,"/",a1,"=",a2/a1
            return
        stack  = []
        cal = ["+", "-", "*", "/"]
        for i in tokens:
            if i in cal:
                if check(i, stack) == False:
                    return
		print stack
            else:
                stack.append(int(i))
        if len(stack) != 1:
            return
        return stack[0]

sol = Solution()
str = ["-78","-33","196","+","-19","-","115","+","-","-99","/","-18","8","*","-86","-","-","16","/","26","-14","-","-","47","-","101","-","163","*","143","-","0","-","171","+","120","*","-60","+","156","/","173","/","-24","11","+","21","/","*","44","*","180","70","-40","-","*","86","132","-84","+","*","-","38","/","/","21","28","/","+","83","/","-31","156","-","+","28","/","95","-","120","+","8","*","90","-","-94","*","-73","/","-62","/","93","*","196","-","-59","+","187","-","143","/","-79","-89","+","-"]
print sol.evalRPN(str)

