
class Solution(object):
	def heapifyAdd(self, heap, height, dic):
		if height in dic:
			dic[height][1] += 1
			return
		heap.append(height)
		index , dic[height] = len(heap)-1, [len(heap)-1,1]
		while index > 0 and height > heap[(index-1)/2]:
			father = (index-1)/2
			dic[height][0], dic[heap[father]][0] = father, index
			heap[father], heap[index] = heap[index], heap[father]
			index = father
		#mark the 
		# print "add value ", height, dic
		print heap
		return 

	def heapifyDel(self, heap, height, dic):
		if dic[height][1] > 1:
			dic[height][1] -= 1
			return 
		index = dic[height][0]
		value = heap[-1]
		# print dic, heap
		heap[-1],heap[index] = heap[index], heap[-1]
		dic[value][0] = index
		heap.pop()
		del dic[height]
		while True:
			left = index * 2 + 1
			right = index * 2 + 2
			print left, right, len(heap), heap, index
			if left >=len(heap): # reach leaf node
				break
			elif right >= len(heap) : # only have one son node
				if heap[index] < heap[left]:
					dic[value][0] , dic[heap[left]][0] = left, index
					heap[index] , heap[left] = heap[left], heap[index]
				else:
					break # finish
			else:
				if heap[index] >= heap[left] and heap[index] >= heap[right]:
					break
				elif heap[left] >= heap[index] and heap[left] >= heap[right]:
					dic[value][0], dic[heap[left]][0] = left, index
					heap[left], heap[index] = heap[index], heap[left]
					index = left

				elif heap[right] >= heap[index] and heap[right] >= heap[left]:
					dic[value][0], dic[heap[right]][0] = right, index
					heap[right] , heap[index] = heap[index], heap[right]
					index = right
		# print heap
		return





	def getSkyline(self, buildings):
		start, termi, heap, dic =  [], [], [], {}
		for i in xrange(len(buildings)):
			start.append((buildings[i][0],buildings[i][2]))
			termi.append((buildings[i][1],buildings[i][2]))
		#set up two poiner to compare if the change hapend at some position
		termi = sorted(termi, key = lambda x: x[0])
		# print termi
		p1, p2 = 0, 0 
		#p1 point to the first array
		rel = []
		#p2 point to the second array
		while p1 < len(start) and p2 < len(termi):
			if start[p1][0] < termi[p2][0]:
				# print 'insert into p1, value', p1, start[p1][0]
				tmp = start[p1]
				pos, height = start[p1][0], start[p1][1]
				self.heapifyAdd(heap,height,dic)
				p1 += 1 
			elif start[p1][0] > termi[p2][0]:
				# print 'del  p2, value', p2, termi[p2][0]
				tmp = termi[p2]
				pos, height = termi[p2][0],  termi[p2][1]
				self.heapifyDel(heap,height,dic)
				p2 += 1
			else:
				# print 'insert into p1, value', p1, start[p1][1], 'del  p2, value', p2, termi[p2][1]
				tmp = start[p1]
				pos, height = start[p1][0], start[p1][1]
				self.heapifyAdd(heap,height,dic)
				p1+=1
				# print heap
				tmp = termi[p2]
				pos, height = termi[p2][0],termi[p2][1]
				self.heapifyDel(heap,height,dic)
				p2+=1
				# print heap

			# print start, termi
			if not heap:
				rel.append([pos,0])
			else:
				rel.append([pos,heap[0]])
		#combine same height
		while p2 < len(termi):
			# print 'del  p2, value', p2, termi[p2][0]
			tmp = termi[p2]
			pos, height = termi[p2][0],  termi[p2][1]
			self.heapifyDel(heap,height,dic)
			p2 += 1
			if not heap:
				rel.append([pos,0])
			else:
				rel.append([pos,heap[0]])
		# print rel
		#combine the list
		length = len(rel)
		last = -1
		for _ in xrange(length):
			tmp = rel.pop(0)
			if tmp[0] == last:
				rel.pop()
				rel.append(tmp)
			else:
				rel.append(tmp)
				last = tmp[0]
		length = len(rel)
		last = 0
		for _ in xrange(length):
			tmp = rel.pop(0)
			if tmp[1] == last:
				pass
			else:
				rel.append(tmp)
				last = tmp[1]


		return rel
test = [[3,7,8],[3,8,7],[3,9,6],[3,10,5],[3,11,4],[3,12,3],[3,13,2],[3,14,1]]
# test = [[2190,661048,758784],[9349,881233,563276],[12407,630134,38165],[22681,726659,565517],[31035,590482,658874],[41079,901797,183267],[41966,103105,797412],[55007,801603,612368],[58392,212820,555654],[72911,127030,629492],[73343,141788,686181],[83528,142436,240383],[84774,599155,787928],[106461,451255,856478],[108312,994654,727797],[126206,273044,692346],[134022,376405,472351],[151396,993568,856873],[171466,493683,664744],[173068,901140,333376],[179498,667787,518146],[182589,973265,394689],[201756,900649,31050],[215635,818704,576840],[223320,282070,850252],[252616,974496,951489],[255654,640881,682979],[287063,366075,76163],[291126,900088,410078],[296928,373424,41902],[297159,357827,174187],[306338,779164,565403],[317547,979039,172892],[323095,698297,566611],[323195,622777,514005],[333003,335175,868871],[334996,734946,720348],[344417,952196,903592],[348009,977242,277615],[351747,930487,256666],[363240,475567,699704],[365620,755687,901569],[369650,650840,983693],[370927,621325,640913],[371945,419564,330008],[415109,890558,606676],[427304,782478,822160],[439482,509273,627966],[443909,914404,117924],[446741,853899,285878],[480389,658623,986748],[545123,873277,431801],[552469,730722,574235],[556895,568292,527243],[568368,728429,197654],[593412,760850,165709],[598238,706529,500991],[604335,921904,990205],[627682,871424,393992],[630315,802375,714014],[657552,782736,175905],[701356,827700,70697],[712097,737087,157624],[716678,889964,161559],[724790,945554,283638],[761604,840538,536707],[776181,932102,773239],[855055,983324,880344]]
print Solution().getSkyline(test)

