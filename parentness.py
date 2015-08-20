
def check(s):
      if s is None:
            return False
      length = len(s)
      #dp = [0]* length
      stack = []
      for i in range(length):
            if s[i] == '(':
                  stack.append(s[i])
                  #dp[i] = 0
            else:
                  if len(stack) == 0:
                        return False
                  if stack.pop() == "(":
                        pass
                  else:
                        return False
      if len(stack) == 0:
            return True
print check("()")
print check(")))(((")
print check("((()))")
