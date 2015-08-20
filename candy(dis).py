class Solution:
    # @param ratings, a list of integer
    # @return an integer
    
    #asssume all the children stand ordered by the rating value
   
    def candy(self, ratings):
        rating = []
        size = 0
        def __init__(self, rating):
            self.rating = rating
            self.size = len(rating)
        
        def(self):
            total = 0
            accumulating = 1 
            for i in range(self.size):
                if i == 0: 
                    total = 1 
                if i > 0:
                    if self.rating[i] <= self.rating[i+1]:
                        accumulating = 1
                        total += 2
                    if self.rating[i] > self.rating[i+1]:
                        accumulating += 1
                        total += accumulating
                        