'''
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10]
'''
'''
#scenario1: if insert a value has no overlap  sub1 : on the left means insert.end < first start
#											  sub2 : on the rigth means insert. start  < max(intervals.end)
#scenario2: if insert a value has one side overlap : sub1 if left overlap with others and right not in overlap anything then extend the one has overlap 
													 sub2 if right overlap with other and left not in overlap extend that interval to left
#scenario3: if insert a value has both sides overlap, then merge all of those to one 
#scenario4: insert a value between two intervals just insert in to the array
'''
class Interval(object):
	def __init__(self, s=0, e=0):
		self.start = s
		self.end = e


class Solution(object):
	def insert(self, intervals, newInterval):

		#if there's no value in orginal intervals 
		if len(intervals) == 0:
			return [newInterval]
		# scenario1
		if newInterval.end < intervals[0].start:
			return [newInterval]+intervals
		if newInterval.start > intervals[-1].end:
			print "return append"
			return intervals + [newInterval]
		index, rel = 0, []
		while index < len(intervals) and newInterval.start > intervals[index].end:
			rel.append(intervals[index])
			index += 1

		newInterval.start = min(intervals[index].start,newInterval.start)

		while index < len(intervals) and newInterval.end >= intervals[index].start:
			newInterval.end = max(intervals[index].end, newInterval.end)
			index += 1
		
		rel.append(newInterval)

		while index < len(intervals):
			rel.append(intervals[index])
			index += 1
		return rel


	
		