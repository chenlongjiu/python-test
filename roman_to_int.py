class Solution(object):
    def romanToInt(self, s):
        num = [1000,500,100,50,10,5,1]
        roman = ['M','D','C','L','X','V','I']
        romanM = ['C','X','I']
        rel,wait = 0, []
        for alp in s:
            print rel,wait
            if alp not in romanM and not wait:
                rel += num[roman.index(alp)]
            else:
                if wait:
                    cur = wait[0]
                    if roman.index(alp) < roman.index(cur):
                        rel += num[roman.index(alp)] - len(wait) * num[roman.index(cur)]
                        wait = []
                    elif alp == cur:
                        wait.append(alp)
                    else:
                        rel += len(wait) * num[roman.index(cur)]
                        if alp in romanM:
                            wait = [alp]
                        else:
                            rel += num[roman.index(alp)]
                            wait = []
                else:
                    wait.append(alp)
        if wait:
            rel += num[roman.index(wait[0])]  * len(wait)
        return rel

sol = Solution()
print sol.romanToInt("MDCCCLXXXIV")