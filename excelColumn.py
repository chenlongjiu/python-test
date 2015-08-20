'''
Given a positive integer, return its corresponding column title as appear in an Excel sheet.
'''

class Solution:
    # @return a string
    def convertToTitle(self, num):
        res = list()
        result = ''
        while num > 0:
            if num % 26 == 0:
                num /= 26
                num -= 1
                res.append('Z')
            else: 
            	res.append(chr(ord('A')-1+num%26)) 
                num /= 26

        for i in range(len(res)):
        	result += res.pop()
        return result

sol = Solution()
print sol.convertToTitle(27)
         