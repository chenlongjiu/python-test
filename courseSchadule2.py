'''
There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

For example:

2, [[1,0]]

There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1]

4, [[1,0],[2,0],[3,1],[3,2]]

There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. So one correct course order is [0,1,2,3]. Another correct ordering is[0,2,1,3].
'''
'''
class topoNode(object):
	def __init__(self,val):
		self.path = {} #record the courses depends on this course
		self.val = val # record course number 
		self.visit = 0 # 0 for non-visit 1 for visited -1 for visiting

class Solution(object):

	def dsf(self, node):
		#print node.val,  node.visit
		if node.visit == -1:
			return False
		res , rel = [], [] # res record the final result and rel record temporary value of one step value
		flag = False
		if node.visit == 0: # this node has never been reviewed
			flag = True
		node.visit = -1
		#print "after node.visit has been reviewing", node.visit
		for key in node.path:
			
			rel = self.dsf(node.path[key])
			if rel == False:
				return False
			else:
				res += rel
		node.visit = 1
		if flag : res.append(node.val)
		return res

	def findOrder(self, numCourses, prerequisites):
		courses = {}
		for x,y in prerequisites:  # if you need x should study y first 
			if x not in courses:
				courses[x] = topoNode(x)
			if y not in courses:
				courses[y] = topoNode(y)
			courses[x].path[y] = courses[y]

		res = []
		for i in range(numCourses):
			if i in courses.keys():
				if courses[i].visit == 0:
					rel = self.dsf(courses[i])
					if rel is False:
						return []
					else: res += rel
			else:
				res.append(i)

		return res



		#set up a topo tree to store the list 



'''
import collections

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        graph  = collections.defaultdict(set)
        preCourse = collections.defaultdict(set)
        for course, pre  in prerequisites:
            graph[course].add(pre)
            preCourse[pre].add(course)
        stack = [n for n in range(numCourses) if not graph[n]]
        res = []
        while stack:
            node = stack.pop()
            print node
            res.append(node)
            for n in preCourse[node]:
                graph[n].remove(node)
                if not graph[n]: stack.append(n)
        return res if len(res) == numCourses else []
# this solution use prerequest course, and keep remove the prerequest courese until all the pre courses has been done. Then put this course in to the right place

sol = Solution()

print sol.findOrder(5, [[1,0],[0,3],[3,1],[3,2]])

