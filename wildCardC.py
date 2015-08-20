def check(s, p):
	dp = [True] + [False]*len(s)
	l = len(s)
	for letter in p:
		new_dp = [dp[0] and letter == "*"]
		if letter == "*":
			for j in range(l):
				new_dp.append(new_dp[-1] or dp[j+1])
		if letter == "?":
			new_dp += dp[:l]
			# all move to the next digit
			new_dp += [dp[j] and s[j] == letter for j in range(l)]
		dp = new_dp
		print dp
	return dp[-1]
rules = "c*a*b?x"
true1 = "cbbbbachda*bcx"
true2 = "cabdx"
false = "dszbex"
false = "cbsydksldybtx"
#false = " "
print check(false, rules)