'''
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26

Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2. 
'''
class Solution(object):
    def numDecodings(self, s):
        if not s or s[0] == '0':
            return 0
        dp = [1]*(len(s)+1)
        digits = range(0,10)
        digits = map(str,digits)
        for digit in xrange(1,len(s)):
            if s[digit] == '0':
                if (int(s[digit-1:digit+1]) == 0 or int(s[digit-1:digit+1])>26):
                    return 0
                else:
                    dp[digit+1] = dp[digit]
            elif s[digit]!= '0' and s[digit-1] != '0' and digit+1 == len(s):
                if int (s[digit-1:digit+1]) <= 26 :
                    dp[digit+1] = dp[digit] + dp[digit-1]
                else:
                    dp[digit+1] = dp[digit]
            elif digit + 1 < len(s) and s[digit]!='0' and s[digit-1] != '0' and s[digit+1]!= '0':
                if int (s[digit-1:digit+1]) <= 26 :
                    dp[digit+1] = dp[digit] + dp[digit-1]
                else:
                    dp[digit+1] = dp[digit]
            else:
                if s[digit] not in digits:
                    return 0
                else:
                    dp[digit+1] = dp[digit]
            
            
            
            # print dp
        return dp[-1]
                
            
        """
        :type s: str
        :rtype: int
        """
        