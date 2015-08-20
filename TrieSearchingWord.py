class Node(object):
    def __init__(self, wd = ''):
        self.path = {}
        self.val = wd
        self.isWord = False

class WordDictionary(object):
    def __init__(self):
        self.root = Node()
        """
        initialize your data structure here.
        """
        

    def addWord(self, word):
        cur = self.root
        for i in word:
            if i not in cur.path:
                cur.path[i] = Node(i)
            cur = cur.path[i]
        cur.isWord = True
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """

        
    def search(self, word ,root = False):
        if root == False:
            cur = self.root
        else:
            cur = root
            
        if word == "":
            return cur.isWord
        
        for i in range(len(word)):
            if word[i] not in cur.path:
                if word[i] == '.':
                    #no more alphabet
                    if len(cur.path) == 0:
                        return False 
                    if i < len(word)-1:
                            suffix = word[i+1:]
                    else:
                        suffix = ""
                    for key in cur.path:
                        if self.search(suffix,cur.path[key]) == True:
                            return True
                    return False
                else:
                    return False
            else:
                cur = cur.path[word[i]]
        return cur.isWord
        
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        

# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")