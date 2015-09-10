'''
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.

'''

class Solution(object):
    def plusOne(self, digits):
        if not digits:
            return [1]
        carry = 1
        for index in xrange(len(digits)-1, -1, -1):
            if digits[index] + carry < 10:
                digits[index] += 1
                return digits
            else:
                digits[index] = 0
                carry = 1
        return [1]+digits