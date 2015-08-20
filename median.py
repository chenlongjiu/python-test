class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        if len(A) == 0 and len(B) == 0:
            return None
        else:
            if (len(A)+len(B))%2 == 0:
                print "pass"
                count2 = int((len(A)+len(B))/2)
                count1 = count2+1
                print count2, count1
            else:
                count1 = count2 = int((len(A)+len(B)+1)/2)
            markA, markB = 0,0
            med = [] # for store result
            for i in range(count1):
                if markA == len(A):
                    med.append(B[markB])
                    markB += 1
                elif markB == len(B):
                    med.append(A[markA])
                    markA += 1
                elif A[markA] <= B[markB]:
                    med.append(A[markA])
                    markA += 1
                elif B[markB] < A[markA]:
                    med.append(B[markB])
                    markB += 1
                print med

        return float(med[count1-1]+med[count2-1])/2

print Solution().findMedianSortedArrays([],[2,3])

