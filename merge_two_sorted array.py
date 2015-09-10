class Solution(object):
    def merge(self, nums1, m, nums2, n):
        start = m+n-1
        index1 = m-1
        index2 = n-1
        while index1 >= 0 and index2 >= 0:
            if nums1[index1] > nums2[index2]:
                nums1[start] = nums1[index1]
                index1-=1


            else:
                nums1[start] = nums2[index2]
                index2-=1
            start -= 1
        if index1 < 0:
            while index2 >=0:
                nums1[start] = nums2[index2]
                index2 -= 1
                start -= 1
        return

nums1 = [2,0]
nums2 = [1]
sol = Solution()
sol.merge(nums1, 1, nums2, 1)
print nums1