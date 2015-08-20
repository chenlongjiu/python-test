#number of line
'''
# Definition for a point
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b
import collections
class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        # the k is the rate of the line and the point calculate the k for all two points is the  Cn2 = N(N-1)/2 O(n2) time
        line = {}
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                if points[i][0] == points[j][0]:
                    k = "vertical"
                else:
                    k = float(points[i][1]-points[j][1])/(points[i][0]-points[j][0])
                # hwo to unique the line
                l = (points[i], k)
                if l in line.keys():
                    line[l] += 1
                else:
                    line[l] = 1
        return line     

s = [(40,-23),(9,138),(429,115),(50,-17),(-3,80),(-10,33),(5,-21),(-3,80),(-6,-65),(-18,26),(-6,-65),(5,72),(0,77),(-9,86),(10,-2),(-8,85),(21,130),(18,-6),(-18,26),(-1,-15),(10,-2),(8,69),(-4,63),(0,3),(-4,40),(-7,84),(-8,7),(30,154),(16,-5),(6,90),(18,-6),(5,77),(-4,77),(7,-13),(-1,-45),(16,-5),(-9,86),(-16,11),(-7,84),(1,76),(3,77),(10,67),(1,-37),(-10,-81),(4,-11),(-20,13),(-10,77),(6,-17),(-27,2),(-10,-81),(10,-1),(-9,1),(-8,43),(2,2),(2,-21),(3,82),(8,-1),(10,-1),(-9,1),(-12,42),(16,-5),(-5,-61),(20,-7),(9,-35),(10,6),(12,106),(5,-21),(-5,82),(6,71),(-15,34),(-10,87),(-14,-12),(12,106),(-5,82),(-46,-45),(-4,63),(16,-5),(4,1),(-3,-53),(0,-17),(9,98),(-18,26),(-9,86),(2,77),(-2,-49),(1,76),(-3,-38),(-8,7),(-17,-37),(5,72),(10,-37),(-4,-57),(-3,-53),(3,74),(-3,-11),(-8,7),(1,88),(-12,42),(1,-37),(2,77),(-6,77),(5,72),(-4,-57),(-18,-33),(-12,42),(-9,86),(2,77),(-8,77),(-3,77),(9,-42),(16,41),(-29,-37),(0,-41),(-21,18),(-27,-34),(0,77),(3,74),(-7,-69),(-21,18),(27,146),(-20,13),(21,130),(-6,-65),(14,-4),(0,3),(9,-5),(6,-29),(-2,73),(-1,-15),(1,76),(-4,77),(6,-29)]
print Solution().maxPoints(s)
'''

























'''
#Best Time for stock
class Solution:
    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0
        else:
            start = 0
            end = 0
            profit = 0
            while start <= len(prices)-2:  #this loop will stop at the last two element
                if prices[start] < prices[start + 1]:
                    end = start + 1
                    if end != len(prices)-1:
                        while(prices[end] < prices[end+1]):
                            end += 1
                            if end > len(prices)-2: # this loop will stop at the last one element
                                break
                    profit += prices[end] - prices[start] 
                    start = end + 1
                else:
                    start += 1
        return profit
print Solution().maxProfit([4,2,4,6,2,5])
'''



















#Gas Station
'''
class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        if len(gas) == len(cost) and len(gas) > 0:
            start = len(gas)-1
            end = 0
            sum = gas[start] - cost[start]
            print sum
            # sum including the gas statue
            while start > end:
                if sum >= 0:
                    sum += (gas[end] - cost[end])
                    end += 1
                else:
                    start -= 1
                    sum += (gas[start] - cost[start])
            if sum >= 0:
                print sum
                return start
            else:
                return -1
        else:
            return -1

gas = [4]
cost =[5]
print Solution().canCompleteCircuit(gas, cost)
'''
