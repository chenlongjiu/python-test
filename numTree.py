class Solution:
    # @param {integer} n
    # @return {integer}
    def numTrees(self, n):
        #for each node they can use all the legal one to be the root 
        total = 0;#count for total structure
        if(n == 1):
            return 1;
        for i in range(1, n):
            #set up a root
            total += self.countTree(1, i) + self.countTree(i+1, n)
        return total    
        
    def countTree(self, left, right):
        print('left is',left , 'right is' , right ,'/n') 
        if(right - left == 0):
            return 1
        count = 0
        for i in range(left, right):
            count += (self.countTree(left, i) + self.countTree(i+1, right))
            
        return count


sol = Solution()
print(sol.numTrees(6))
