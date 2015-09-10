class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        rel = [0,0]
        res = 0
        for ele in nums:
            res ^= ele
            print res
        #res record only info of the two diff digits
        digit = res & -res
        print "digit is ",  digit
        #get the least diff digits between two numbers
        for ele in nums:
            if digit & ele == 0:
                rel[0] ^= ele
                print "res & ele is 0", ele
            else:
                rel[1] ^= ele
                print ele
            print ele, rel
        return rel

print Solution().singleNumber([0,0,1,2])


#all number xor will return the one shows single numbers xor
# x & -x will find the least significant digit diff
# x & sig will will find which seperate the number set into 2
# use the first way to get the single number