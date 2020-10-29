# 1. Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to
# target. You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
#
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

# Constraints:
# 2 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
# Only one valid answer exists.
from typing import List, Dict


class Solution:
    def __init__(self):
        print("[LeetCode] 1. Two Sum")

    @staticmethod
    def fast_two_sum(nums: List[int], target: int) -> List[int]:
        size: range = range(len(nums))
        vals: Dict[int, int] = {}
        vals.fromkeys(size)
        for i in size:
            try:
                if vals[target - nums[i]] != i:
                    return [vals[target - nums[i]], i]
            except KeyError:
                vals[nums[i]] = i
        for i in size:
            try:
                if vals[target - nums[i]] != i:
                    return [i, vals[target - nums[i]]]
            except KeyError:
                continue
        return []

    @staticmethod
    def two_sum(nums: List[int], target: int) -> List[int]:
        try:
            check_constraints(nums, target)
        except NameError:
            print("Constraints error!")
            raise

        result: List[int] = []
        size: int = len(nums)

        for curr, value in enumerate(nums):
            if curr >= size:
                break

            difference: int = target - value

            try:
                pair: int = nums.index(difference, curr + 1)
                result.append(curr)
                result.append(pair)
                break
            except ValueError:
                continue

        return result


def check_constraints(nums: List[int], target: int) -> None:
    # Constraints:
    # 2 <= nums.length <= 10^5
    # -10^9 <= nums[i] <= 10^9
    # -10^9 <= target <= 10^9

    size: int = len(nums)

    if size < 2 or size > pow(10, 5):
        raise NameError("Wrong constraint 2 <= nums.length <= 10^5")

    for val in nums:
        if val < pow(-10, 9) or val > pow(10, 9):
            raise NameError("Wrong constraint -10^9 <= nums[i] <= 10^9")

    if target < pow(-10, 9) or target > pow(10, 9):
        raise NameError("Wrong constraint -10^9 <= target <= 10^9")


def main():
    solution: Solution = Solution()
    nums: List[int] = [3, 2, 4]
    target: int = 6

    result: List[int] = solution.fast_two_sum(nums, target)
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
