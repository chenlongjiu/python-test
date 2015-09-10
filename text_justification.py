'''
Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.

Return the formatted lines as:

[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Note: Each word is guaranteed not to exceed L in length.

click to show corner cases.
Corner Cases:

A line other than the last line might contain only one word. What should you do in this case?
In this case, that line should be left-justified.

'''


class Solution(object):
	def fullJustify(self, words, maxWidth):
		#for each line
		text = []
		while words:
			cur, length =[], 0
			while words and length + len(words[0]) + len(cur) <= maxWidth:
				# print "length is ", length, " words[0] is ", words[0]
				length += len(words[0])#including space
				cur.append(words.pop(0))
			if words and len(words[0]) > maxWidth:
			    return []
			if words and length < maxWidth and len(cur) > 1:
				spaceNum = maxWidth-length
				spaceSpot = len(cur) - 1
				if spaceNum % spaceSpot == 0:
					space = " " * (spaceNum/spaceSpot)
					# print "space is ", len(space)
					text.append(space.join(cur))
				else:
				# 	print spaceNum, spaceSpot
					space =[]
					space += [" " * (spaceNum/spaceSpot + 1) for _ in xrange(spaceNum % spaceSpot)]
					space += [" " * (spaceNum/spaceSpot) for _ in xrange(spaceSpot-1)]
					print cur
					print space
				# 	print space
					cur.append(cur.pop(0))
					for _ in xrange(spaceSpot):
						cur.append(space.pop(0))
						cur.append(cur.pop(0))
				# 	print cur
					text.append("".join(cur))
			else:
				if length + len(cur) - 1 < maxWidth:
					cur.append(" " * (maxWidth-len(cur) - length -1))
				text.append(" ".join(cur))
		return text
#  """
#  :type words: List[str]
#  :type maxWidth: int
#  :rtype: List[str]
# """
      
['Listen', 'to   ', 'many, ', 'speak ', 'to   a', 'few. ']


test = ["This", "is", "an", "example", "of", "text", "justification."]
print Solution().fullJustify(["Don't","go","around","saying","the","world","owes","you","a","living;","the","world","owes","you","nothing;","it","was","here","first."], 30)




