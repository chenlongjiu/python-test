class Solution(object):
    def myAtoi(self, string):
        MAX = 2147483647
        MIN = -2147483648
        if string is None:
            return 0
        
        string = string.strip() # delete white spaces
        index, mark, rel = 0, 0, 0
        num = map(str,xrange(0,10))
        #if string is empty:
        if len(string) == 0:
            return 0
        if string[0] in num:
            mark = 1
        elif string[0] == '+':
            mark = 1
            index += 1
        elif string[0] == '-':
            mark = -1
            index += 1
            # print mark, index
        else:
            return 0

        while string[index] in num:
            rel *= 10
            rel += int(string[index])
            if rel >= MAX and mark > 0:
                return MAX
            elif rel > abs(MIN) and mark < 0:
                return MIN
            index += 1
            if index >= len(string):
                break
        return rel*mark

sol = Solution()
print sol.myAtoi('+22147483647')