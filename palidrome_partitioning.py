class Solution(object):
    
    def check(self, s, left, right):
        if s[left:right] == s[left:right][::-1]:
            return True
        return False
    
    def backTracking(self, s, index, rel, tmp):
        # print s, index, rel , tmp
        if index >= len(s):
            print tmp[:]
            rel.append(tmp[:])
            print rel
        for i in xrange(index+1, len(s)+1):
            if (self.check(s, index, i)):
                tmp.append(s[index:i])
                self.backTracking(s, i, rel, tmp)
                # print rel
                tmp.pop()
                # print rel
        return 
        
    
    
    
    # public void backTrack(String s, int l){
    #         if(currLst.size()>0 //the initial str could be palindrome
    #             && l>=s.length()){
    #                 List<String> r = (ArrayList<String>) currLst.clone();
    #                 resultLst.add(r);
    #         }
    #         for(int i=l;i<s.length();i++){
    #             if(isPalindrome(s,l,i)){
    #                 if(l==i)
    #                     currLst.add(Character.toString(s.charAt(i)));
    #                 else
    #                     currLst.add(s.substring(l,i+1));
    #                 backTrack(s,i+1);
    #                 currLst.remove(currLst.size()-1);
    #             }
    #         }
    #     }
    
    
    def partition(self, s):
        if not s:
            return []
        rel, tmp = [], []
        self.backTracking(s, 0, rel, tmp)
        
        return rel
        
        
        
        
        
        """
        :type s: str
        :rtype: List[List[str]]
        """
        
Solution().partition("ab")