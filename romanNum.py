'''
I 	1
V 	5
X 	10
L 	50
C 	100
D 	500
M 	1,000
'''
class Solution(object):
	def intToRoman(self, num):
		values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
		numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]

		res = ""
		for i in xrange(len(values)):
			res.join([numerals[i]] * (num/values[i]))
			print i, res, [numerals[i]] * (num/values[i])
			num %= values[i]

			
		return res
                

sol = Solution()
print sol.intToRoman(7)