rules = "*"
true1 = "aa"
true2 = "cabdx"
false = "dszbex"
false = "cbsydksldybtx"
false = " "

def isMatch(s, p):
    l = len(s)
    if len(p) - p.count('*') > l:
        return False
    dp = [True]  + [False] * l
    for letter in p:
        new_dp = [dp[0] and letter == '*']
        if letter == '*':
            for j in range(l):
                new_dp.append(new_dp[-1] or dp[j + 1])
        elif letter == '?':
            new_dp += dp[:l]
        else:
            new_dp += [dp[j] and s[j] == letter for j in range(l)]
        dp = new_dp
        print dp
    return dp[-1]
print isMatch(true1, rules)













