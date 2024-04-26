from typing import List


class Solution(object):
    def merge(self, nums1: List[int], m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        p1 = int(m)
        for number in nums2:
            while nums1[m - p1] < number:
                p1 = p1 - 1
            nums1.insert(m - p1, number)

