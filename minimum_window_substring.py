class Solution(object):
    def minWindow(self, s, t):
        if len(t) > len(s):
            return ""
        dicO = {}
        for ele in t:
            if ele in dicO:
                dicO[ele] += 1
            else:
                dicO[ele] = 1
        left, right = 0, 0
        mini, cnt = len(s),0
        dic = {}
        rel = (0,0)
        while right < len(s):
            if s[right] not in dic and s[right] in dicO:
                dic[s[right]] = 1
                cnt += 1
            elif s[right] in dic and dic[s[right]] < dicO[s[right]] :
                dic[s[right]] += 1
                cnt += 1
            elif s[right] in dic and dic[s[right]] >= dicO[s[right]]:
                dic[s[right]] += 1
            print dic, dicO, cnt
            while cnt == len(t):
                if right-left + 1 <= mini:
                    print left, right
                    rel = (left,right+1)
                    mini = right - left + 1
                if s[left] in dic and dic[s[left]] > dicO[s[left]]:
                    dic[s[left]] -= 1
                    left += 1
                elif s[left] in dic and dic[s[left]] == dicO[s[left]]:
                    dic[s[left]] -= 1
                    left += 1
                    cnt -= 1

                else:
                    left += 1
            right += 1
        
        return s[rel[0]:rel[1]]

print Solution().minWindow('a','a')