def sol():
    s = raw_input()
    dp = [0] *len(s)
    l1 = 0
    l2 = 0
    stack = []
    for i in range(len(s)):
        if i == 0:
            stack.append(s[i])
        else:
            if s[i] == stack[-1]:
                l = 0
                for j in range(min(len(stack),len(s)-1)):
                    if len(s) < i+j+1:
                        break
                    if stack[-1-j] == s[i+j]:
                        l += 2
                    else: break
                dp[i-1+l/2] = max(l, dp[i-1+l/2]) 
               
            
            if len(stack) >= 2 and stack[-2] == s[i]:
                l = 0
                for j in range(min(len(stack)-1,len(s)-i)):
                    if len(s) == i+j:
                        break
                    if stack[-2-j] == s[i+j]:
                        l += 2
                    else: break
                dp[i-1+l/2] = max(l+1, dp[i-1+l/2])
            stack.append(s[i])
    print dp
    maxi = max(dp)
    print maxi*max(dp[:dp.index(maxi)-10]+dp[dp.index(maxi)+1:])
                
              
            
            
    
    
sol()