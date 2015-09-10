class Solution:
    # @param pages: a list of integers
    # @param k: an integer
    # @return: an integer
    def copyBooks(self, pages, k):
        # write your code here
        index = [(len(pages)//k)*n for n in xrange(k)]
        index.append(len(pages))
        sumBlock = []
        for i in xrange(len(index)-1):
        	subsum = 0
        	for t in xrange(index[i],index[i+1]):
        		subsum += pages[t]
        	sumBlock.append(subsum)
        



        
       	return 

Solution().copyBooks([3,2,4],2)