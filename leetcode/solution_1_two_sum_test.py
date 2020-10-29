import unittest
from leetcode import solution_1_two_sum


class SolutionTest(unittest.TestCase):
    def test_one(self):
        self.assertEqual(solution_1_two_sum.Solution.two_sum([2, 7, 11, 15], 9), [0, 1])


if __name__ == '__main__':
    unittest.main()
