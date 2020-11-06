# Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
#
# Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]
#
# Example 3:
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

import unittest
from typing import List

from leetcode.lc_2_add_two_numbers import Solution, ListNode


class SolutionTest(unittest.TestCase):
    def test_one(self):
        l1: ListNode = Solution.fill_nodes([2, 4, 3])
        l2: ListNode = Solution.fill_nodes([5, 6, 4])

        result: List[int] = SolutionTest.get_list(Solution.add_two_numbers(l1, l2))

        self.assertEqual(result, [7, 0, 8])

    def test_two(self):
        l1: ListNode = Solution.fill_nodes([0])
        l2: ListNode = Solution.fill_nodes([0])

        result: List[int] = SolutionTest.get_list(Solution.add_two_numbers(l1, l2))

        self.assertEqual(result, [0])

    def test_three(self):
        l1: ListNode = Solution.fill_nodes([9, 9, 9, 9, 9, 9, 9])
        l2: ListNode = Solution.fill_nodes([9, 9, 9, 9])

        result: List[int] = SolutionTest.get_list(Solution.add_two_numbers(l1, l2))

        self.assertEqual(result, [8, 9, 9, 9, 0, 0, 0, 1])

    @staticmethod
    def get_list(node: ListNode) -> List[int]:
        nodes_list: List[int] = []

        while node is not None:
            nodes_list.append(node.val)
            node = node.next

        return nodes_list


if __name__ == '__main__':
    unittest.main()
