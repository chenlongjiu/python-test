
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

#best solution:
class Solution:
    # @param {int[]} points an array of point
    # @return {int} an integer

            
    def maxPoints(self, points):
        # Write your code here
        if len(points) <= 2:
            return len(points)
        maxi = 0
        
        for i in xrange(len(points)-1):
            tmp = 0
            extra = 1
            dic = {}
            for j in xrange(i+1,len(points)):
                p1, p2 = points[i], points[j]
                if p1.x == p2.x and p1.y == p2.y:
                    extra += 1
                else:
                    if p1.x == p2.x:
                        k = 'a'
                    elif p1.y == p2.y:
                        k = 'b'
                    else:
                        k = float(p1.x-p2.x)/(p1.y-p2.y)
                        # print k
                    if k in dic:
                        dic[k] += 1
                    else:
                        dic[k] = 1
            # print dic
            for k in dic:
                tmp = max(tmp, dic[k])
            tmp += extra
            maxi = max(maxi,tmp)
                    
        return maxi


'''

class Solution:
    # @param {int[]} points an array of point
    # @return {int} an integer
    def getMiniDiv(self,p1,p2):

        div1, div2 = abs(p1.x-p2.x), abs(p1.y-p2.y)
        # print "d1,d2",div1, div2
        if div1 == 0:
            return (0,0)
        if div2 == 0:
            return ('inf','inf')
        while div1%div2 != 0:
            x, y = div2, div1%div2
            div1,div2 = x,y
        q = div2
        r1, r2 = abs(p1.x-p2.x)/q, abs(p1.y-p2.y)/q
        # print "r1,r2",r1, r2
        if (p1.x-p2.x) * (p1.y-p2.y) > 0:
            return(r1,r2)
        else:
            return(r1,-r2)
            
    def maxPoints(self, points):
        # Write your code here
        if len(points) <= 2:
            return len(points)
        maxi = 0
        
        for i in xrange(len(points)-1):
            tmp = 0
            extra = 0
            dic = {}
            for j in xrange(i+1,len(points)):
                if points[i].x == points[j].x and points[i].y == points[j].y:
                    extra += 1
                    print "tmp",tmp
                k = self.getMiniDiv(points[i],points[j])
                # print k
                if k in dic:
                    dic[k] += 1
                else:
                    dic[k] = 1
            print dic
            print "/////////////////////////////////////////////"
            for k in dic:
                tmp = max(tmp, dic[k])
            tmp += 1 + extra
            maxi = max(maxi,tmp)
                    
        return maxi
'''
rel = []
test = [[0,0],[1,1],[0,0]]
# test = [[-54,-297],[-36,-222],[3,-2],[30,53],[-5,1],[-36,-222],[0,2],[1,3],[6,-47],[0,4],[2,3],[5,0],[48,128],[24,28],[0,-5],[48,128],[-12,-122],[-54,-297],[-42,-247],[-5,0],[2,4],[0,0],[54,153],[-30,-197],[4,5],[4,3],[-42,-247],[6,-47],[-60,-322],[-4,-2],[-18,-147],[6,-47],[60,178],[30,53],[-5,3],[-42,-247],[2,-2],[12,-22],[24,28],[0,-72],[3,-4],[-60,-322],[48,128],[0,-72],[-5,3],[5,5],[-24,-172],[-48,-272],[36,78],[-3,3]]
for ele in test:
    rel.append(Point(ele[0],ele[1]))
print Solution().maxPoints(rel)