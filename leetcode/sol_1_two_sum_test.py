import unittest
from leetcode import sol_1_two_sum

# Example
# 1: Input: nums = [2, 7, 11, 15], target = 9
#    Output: [0, 1]
#    Output: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example
# 2: Input: nums = [3, 2, 4], target = 6
#    Output: [1, 2]
# Example
# 3: Input: nums = [3, 3], target = 6
#    Output: [0, 1]


class SolutionTest(unittest.TestCase):
    def test_one(self):
        self.assertEqual(sol_1_two_sum.Solution.two_sum([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(sol_1_two_sum.Solution.fast_two_sum([2, 7, 11, 15], 9), [0, 1])

    def test_two(self):
        self.assertEqual(sol_1_two_sum.Solution.two_sum([3, 2, 4], 6), [1, 2])
        self.assertEqual(sol_1_two_sum.Solution.fast_two_sum([3, 2, 4], 6), [1, 2])

    def test_three(self):
        self.assertEqual(sol_1_two_sum.Solution.two_sum([3, 3], 6), [0, 1])
        self.assertEqual(sol_1_two_sum.Solution.fast_two_sum([3, 3], 6), [0, 1])


if __name__ == '__main__':
    unittest.main()
