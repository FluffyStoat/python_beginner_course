# 8. String to Integer (atoi)

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
from typing import List


class Solution:
    @staticmethod
    def my_atoi(message: str) -> int:
        symbols: List[str] = []

        dictionary: str = "-+ .1234567890"
        int_min: int = pow(-2, 31)
        int_max: int = pow(2, 31) - 1

        message = message.strip()
        sign: str = None

        for symbol in message:
            if symbol in dictionary:
                if symbol == " " or symbol == ".":
                    break

                if symbol == "-" or symbol == "+":
                    if sign is not None or len(symbols) > 0:
                        break

                    if sign is None:
                        sign = symbol
                        continue
                    else:
                        return 0

                symbols.append(symbol)
            else:
                break

        if len(symbols) == 0:
            return 0

        value: int = int(''.join(symbols))

        if sign == "-":
            value = value * (-1)

        if value < int_min:
            value = int_min

        if value > int_max:
            value = int_max

        return value


def main():
    solution: Solution = Solution()

    print(f'"42": {solution.my_atoi("42")}')
    print(f'"   -42": {solution.my_atoi("   -42")}')
    print(f'"4193 with words": {solution.my_atoi("4193 with words")}')
    print(f'"-91283472332": {solution.my_atoi("-91283472332")}')
    print(f'"-56.73 472332": {solution.my_atoi("-56.73 472332")}')
    print(f'"+-12": {solution.my_atoi("+-12")}')
    print(f'"++12": {solution.my_atoi("++12")}')
    print(f'"--12": {solution.my_atoi("--12")}')
    print(f'"00000-42a1234": {solution.my_atoi("00000-42a1234")}')
    print(f'"-5-": {solution.my_atoi("-5-")}')


if __name__ == "__main__":
    main()
