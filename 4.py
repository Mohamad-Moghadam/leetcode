class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        both = nums1 + nums2
        both.sort()
        middle = len(both) // 2
        desired = both[middle]
        if len(both)%2 == 1:
            return desired
        else:
            return (desired + both[middle - 1]) / 2.0
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        