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
        p2 = m
        for number in nums2:
            nums1[p2] = number
            p2 += 1
        sorted(nums1)


