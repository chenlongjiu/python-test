class TrieNode:
	def __init__(self, val = None, isword = False):
		self.val = val # record node value
		self.isword = isword
		self.path = {}  #record children's node

class Trie:
	def __init__(self):
		self.root = TrieNode('') 

	def __contains__(self,word):
		cur = self.root
		for letter in word:
			if letter not in cur.path:
				return False
			cur = cur.path[letter]
		return cur.isword

	def insert(self, word):
		cur = self.root
		for l in word: 
			if l not in cur.path:
				cur.path[l] = TrieNode(l)
			cur = cur.path[l] 
		cur.isword = True
		return

	def getAllPrefix(self, word):
		#return all existing prefix of one word
		cur = self.root
		prefix = '' # undergoing prefix
		prefixes = [] # record all the prefix
		for l  in word:
			if l in cur.path:
				prefix += l 
				cur = cur.path[l]
			else:
				return prefixes
			if cur.isword:
				prefixes.append(prefix)
		return prefixes
