'''
The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

    "123"
    "132"
    "213"
    "231"
    "312"
    "321"

Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.
'''
import math
class Solution(object):
    def getPermutation(self, n, k):
        num = range(1,n+1)
        step = n-1
        rel = []
        div = math.factorial(n-1)
        while k >= 0:
            seq = (k-1) / div
            rel.append(str(num.pop(seq)))
            k %= div
            if step == 0:
                break
            div /= step
            step -= 1
        return "".join(rel)