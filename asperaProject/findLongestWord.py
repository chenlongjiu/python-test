from Trie import TrieNode
from Trie import Trie
import collections
from collections import deque

class Solution:
	#initialize value
	def __init__(self, fileA = 'wordsforproblem.txt'):

		self.word = [] # record all the word in file
		f = open(fileA, 'r')
		for line in f: 
			self.word.append(line.strip())
		return

	#if it's not sorted words, uncommand following function
	# def sort(self, word):
	# 	#sort the array by length using quick sort
	# 	maxi = 0 
	# 	for key in word:
	# 		if len(key) > maxi:
	# 			maxi = len(key)
	# 	bucket = [[] for _ in range(maxi) ]
		
	# 	for key in word:
	# 		bucket[(len(key)-1)].append(key)
	# 	rel = []
	# 	for i in bucket:
	# 		rel += i
	# 	return rel

	#calculating the longest word string combined with other words
	def findLongestWord(self):

		word = self.word
		trie = Trie()
		queue = deque()

		#insert key to tree and also mark all the prefix with tuple format
		for key in word: # from longest to shortest
			prefixes = trie.getAllPrefix(key)
			for pf in prefixes:
				queue.append((key, key[len(pf):]))
			trie.insert(key)

		# get the longest word form the provided dictionary
		longest_word = ['','']
		flag = 2 # mark get the first two longest
		dic = {} # mark visited word

		while queue: 
			key,suffix = queue.popleft()
			if key not in dic and suffix in trie:
				dic[key] = True
				if len(key) > len(longest_word[0]):
					longest_word[1] = longest_word[0]
					longest_word[0] = key
				elif len(key) > len(longest_word[1]):
					longest_word[1] = key
			else:
				prefixes = trie.getAllPrefix(suffix)
				for pf in prefixes:
					queue.append((key, suffix[len(pf):]))

		#print result
		print "longest_word 1 are ", longest_word[0], ', length is ',len(longest_word[0])
		print "longest_word 2 are ", longest_word[1], ', length is ',len(longest_word[1])
		print "total words can be combined by other words are", len(dic)
	 	

	 	return



sol = Solution()
sol.findLongestWord() # you can add parameters in fileLongestWord(file_path) for different test cases





