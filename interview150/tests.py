import unittest
from interview150.Easy.merge_sorted_array import Solution as MergeSolution
from interview150.Easy.remove_element import Solution as RemoveElementSolution

class TestSolutions(unittest.TestCase):
    def setUp(self):
        self.merge_solution = MergeSolution()
        self.remove_element_solution = RemoveElementSolution()

    def test_merge_sorted_array(self):
        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = [2, 5, 6]
        n = 3
        self.merge_solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1, 2, 2, 3, 5, 6])

    def test_removeElement(self):
        self.assertEqual(self.remove_element_solution.removeElement([3, 2, 2, 3], 3), 2)
        self.assertEqual(self.remove_element_solution.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2), 3)


if __name__ == '__main__':
    unittest.main()


