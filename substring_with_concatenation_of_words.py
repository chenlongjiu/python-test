# import collections

# class Solution(object):
#     def findSubstring(self, s, words):
#         dic,rel = {},[]
#         for ele in words:
#             if ele in dic:
#                 dic[ele]+= 1
#             else:
#                 dic[ele] = 1
        
#         wL, length = len(words[0]),len(words)*len(words[0])
#         if len(s) < length or not words:
#             return []
#         for index in xrange(len(s)-length+1):
#             if self.checkWindow(dic, s[index:index + length], wL, len(words)):
#                 rel.append(index)
#         return rel
    
#     def checkWindow(self, dic, subString, wL, total):
#         tmpDic = {}
#         for index in xrange(total):

#             tmp = subString[index*wL:(index+1)*wL]
#             print tmpDic,subString
#             if tmp not in dic:
#                 return False
#             else:
#                 if tmp in tmpDic and tmpDic[tmp] + 1 <= dic[tmp]:
#                     tmpDic[tmp] += 1
#                 elif tmp not in tmpDic:
#                     tmpDic[tmp] = 1
#                 else:
#                     return False
            
#         return True

# class Solution:
# # @param {string} s
# # @param {string[]} words
# # @return {integer[]}
#     def findSubstring(self, s, words):
#         if len(words) == 0:
#             return []
#         # initialize d, l, ans
#         l = len(words[0])
#         d = {}
#         for w in words:
#             if w in d:
#                 d[w] += 1
#             else:
#                 d[w] = 1
#         i = 0
#         ans = []
    
#         # sliding window(s)
#         for k in range(l):
#             print 'k is ', k
#             left = k
#             subd = {}
#             count = 0
#             for j in xrange(k, len(s)-l+1, l):
#                 tword = s[j:j+l]
#                 print tword
#                 # valid word
#                 if tword in d:
#                     if tword in subd:
#                         subd[tword] += 1
#                     else:
#                         subd[tword] = 1
#                     count += 1
#                     while subd[tword] > d[tword]:
#                         subd[s[left:left+l]] -= 1
#                         left += l
#                         count -= 1
#                     if count == len(words):
#                         ans.append(left)
#                 # not valid
#                 else:
#                     left = j + l
#                     subd = {}
#                     count = 0
    
#         return ans

class Solution:
# @param {string} s
# @param {string[]} words
# @return {integer[]}
    def findSubstring(self, s, words):
        if len(s) == 0 or not words:
            return []
        wL, length = len(words[0]), len(words)
        dic = {} # recording all words occurance times
        for ele in words:
            if ele in dic:
                dic[ele] += 1
            else:
                dic[ele] =1 
        rel = []
        for divisor in xrange(wL):
            #start record start index of the qualified subString
            #tmpDic record the tempary dictionary
            #cnt used for counting how many words has passed 
            start, tmpDic , cnt= divisor, {}, 0
            left = start
            while start+wL <= len(s):
                tmp = s[start:start+wL]
                if tmp in dic:
                    if tmp in tmpDic:
                        tmpDic[tmp] += 1
                    else:
                        tmpDic[tmp] = 1
                    cnt += 1
                    while tmpDic[tmp] > dic[tmp]:
                        tmpDic[s[left:left+wL]] -= 1
                        cnt -= 1
                        left += wL
                    if cnt == length:
                        rel.append(left)

                else:
                    left = start + wL
                    tmpDic = {}
                    cnt = 0
                start += wL
        return rel   




# test = "abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababab"
# words = ["ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba"]
# words = ["foo","bar"]
# print Solution().findSubstring(test,words)
print Solution().findSubstring("swordgoodgoodgoodbestword", ["word","good","best","good"])