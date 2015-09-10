'''
Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true

Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one. 
'''

#special case :      return bool(re.match(' *[\+\-]?(((\d*\.?\d+)|(\d+\.?\d*))(e[\+\-]?\d+)?)[ ]*$', s))

class Solution(object):
	def isNumber(self, s):
		if not s:
			return False
		#find the first one with valid digit
		digit,digitPos = ['0','1','2','3','4','5','6','7','8','9'], []
		pn,pnPos = ['+','-'], []
		point,times = [],[]
		index = 0
		while index < len(s): 
			if s[index] != ' ':
				break
			index += 1
		if index == len(s):
			return False
		while index < len(s):
			if s[index] in digit:
				digitPos.append(index)
			elif s[index] in pn:
				pnPos.append(index)
			elif s[index] == '.':
				point.append(index)
			elif s[index] == 'e':
				times.append(index)
			else:
				break
			index += 1
		
		if len(digitPos) < 1:
			return False
		
		#all the rest has to be space 
		while index < len(s):
			if s[index] != ' ':
				return False
			index += 1


		for ele in pnPos:
			if ele-1 in digitPos or ele-1 in point :
				print "pn false -1"
				return False
			if ele+1 not in digitPos and ele+1 not in point:
				print "pn false 1"
				return False

		if len(point) > 1:
			print "point false"
			return False
		for ele in point:
			if ele-1 not in digitPos and ele+1 not in digitPos:
				return False
			for pt in times:
				if ele > pt:
					return False
		if len(times) > 1:
			return False
		for ele in times:
			if ele-1 not in digitPos and ele-1 not in point:
				print "times false -1"
				return False
			if ele+1 not in digitPos and ele+1 not in pnPos:
				print "times false 1"
				return False
		return True


print Solution().isNumber('0')
print Solution().isNumber(' 0 ')
print Solution().isNumber('abc')
print Solution().isNumber('1 a')
print Solution().isNumber('2e10')
