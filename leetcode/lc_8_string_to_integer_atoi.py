# 8. String to Integer (atoi)

import re
# Implement atoi which converts a string to an integer.
# The function first discards as many whitespace characters as necessary until the first non-whitespace character
# is found. Then, starting from this character takes an optional initial plus or minus sign followed by as many
# numerical digits as possible, and interprets them as a numerical value.
#
# The string can contain additional characters after those that form the integral number, which are ignored and
# have no effect on the behavior of this function.
#
# If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence
# exists because either str is empty or it contains only whitespace characters, no conversion is performed.
#
# If no valid conversion could be performed, a zero value is returned.
#
# Note:
#
# Only the space character ' ' is considered a whitespace character.
# Assume we are dealing with an environment that could only store integers within the 32-bit signed integer
# range: [−2^31,  2^31 − 1]. If the numerical value is out of the range of representable values, INT_MAX (2^31 − 1)
# or INT_MIN (−2^31) is returned.
#
#
# Example 1:
#
# Input: str = "42"
# Output: 42
# Example 2:
#
# Input: str = "   -42"
# Output: -42
# Explanation: The first non-whitespace character is '-', which is the minus sign. Then take as many
# numerical digits as possible, which gets 42.
# Example 3:
#
# Input: str = "4193 with words"
# Output: 4193
# Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
# Example 4:
#
# Input: str = "words and 987"
# Output: 0
# Explanation: The first non-whitespace character is 'w', which is not a numerical digit or a +/- sign.
# Therefore no valid conversion could be performed.
# Example 5:
#
# Input: str = "-91283472332"
# Output: -2147483648
# Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer. Thefore INT_MIN (−231)
# is returned.
from typing import List, Optional, Match, AnyStr


class Solution:
    @staticmethod
    def atoi_short(s: str) -> int:
        groups: Optional[Match[AnyStr]] = re.compile("\\s*([+-]?\\d+)").match(s)
        if groups:
            v = int(groups.groups()[0])
            if v < -2 ** 31:
                return -2 ** 31
            elif v > 2 ** 31 - 1:
                return 2 ** 31 - 1
            return v
        return 0

    @staticmethod
    def atoi(msg: str) -> int:
        #  : 32 +: 43 -: 45 .: 46
        #  0: 48 1: 49 2: 50 3: 51 4: 52 5: 53 6: 54 7: 55 8: 56 9: 57
        # ord(symbol) chr(num)
        nums: List[int] = [ord(c) for c in msg]
        sign: int = 1
        digits: List[int] = []
        min_val: int = -2 ** 31
        max_val: int = 2 ** 31 - 1

        is_digit_found: bool = False
        is_sign_found: bool = False

        for num in nums:
            if 48 <= num <= 57:
                is_digit_found = True
                digits.append(num)
                continue
            if num in [43, 45]:
                if is_sign_found or is_digit_found:
                    break
                is_sign_found = True
                sign = -1 if num == 45 else 1
                continue
            if num == 32:
                if is_digit_found or is_sign_found:
                    break
                continue
            if num == 46:
                break

            break

        if len(digits) == 0:
            return 0

        result: int = sign * int(''.join([chr(d) for d in digits]))

        return result if min_val < result < max_val \
            else min_val if result < max_val else max_val


def main():
    solution: Solution = Solution()

    print('Slow version')
    print(f'"42": {solution.atoi("42")}')
    print(f'"   -42": {solution.atoi("   -42")}')
    print(f'"4193 with words": {solution.atoi("4193 with words")}')
    print(f'"-91283472332": {solution.atoi("-91283472332")}')
    print(f'"-56.73 472332": {solution.atoi("-56.73 472332")}')
    print(f'"+-12": {solution.atoi("+-12")}')
    print(f'"++12": {solution.atoi("++12")}')
    print(f'"--12": {solution.atoi("--12")}')
    print(f'"00000-42a1234": {solution.atoi("00000-42a1234")}')
    print(f'"-5-": {solution.atoi("-5-")}')

    print('Short version')
    print(f'"42": {solution.atoi_short("42")}')
    print(f'"   -42": {solution.atoi_short("   -42")}')
    print(f'"4193 with words": {solution.atoi_short("4193 with words")}')
    print(f'"-91283472332": {solution.atoi_short("-91283472332")}')
    print(f'"-56.73 472332": {solution.atoi_short("-56.73 472332")}')
    print(f'"+-12": {solution.atoi_short("+-12")}')
    print(f'"++12": {solution.atoi_short("++12")}')
    print(f'"--12": {solution.atoi_short("--12")}')
    print(f'"00000-42a1234": {solution.atoi_short("00000-42a1234")}')
    print(f'"-5-": {solution.atoi_short("-5-")}')


if __name__ == "__main__":
    main()
