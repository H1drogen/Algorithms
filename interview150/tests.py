import unittest
from interview150.Easy.merge_sorted_array import Solution

class TestSolutions(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_merge_sorted_array(self):
        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = [2, 5, 6]
        n = 3
        self.solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1, 2, 2, 3, 5, 6])


if __name__ == '__main__':
    unittest.main()



