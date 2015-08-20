'''
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?
'''


'''
solution: 
check the increasing array and decreasing array. 
counting the number for both of the arrays, and use (1+n)n/2 to count each 
block. Then get the result by add all block. 
O(n) for time O(1) for space
'''
class Solution:
    # @param ratings, a list of integer
    # @return an integer
    size = 0 
    ratings ={}
    def candy(self, ratings):
    	
    	self.size = len(ratings)
    	self.ratings = ratings

    	total, up, upE, down, downE, equal, equalE = None

    	for i in range(len(self.ratings)):
    		if self.ratings[i] < self.ratings[i+1]:
    			if downE == i :
    				total += slope(downE, down)
    			else if up != None: 
    				upE = i+1
    			else: 
    				up = i
    				upE = i+1
    		if self.ratings[i] = self.ratings[i+1]:
    			if equalE == i: 


def slope(i, j):
	return (1+(j-i+1))(j-i+1)/2