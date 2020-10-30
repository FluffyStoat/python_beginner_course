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
# range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1)
# or INT_MIN (−231) is returned.
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
        dictionary: str = "+- .1234567890"
        message = message.strip()

        for symbol in message:
            exists: bool = False

            if symbol in dictionary:
                exists = True

            if symbol == " ":
                break

            if exists:
                symbols.append(symbol)
            else:
                break

        if len(symbols) == 0:
            return 0

        sign: str = "+"
        is_float: bool = False
        digits: List[int] = []

        for symbol in symbols:
            if symbol == "-":
                sign = "-"
            elif symbol == ".":
                is_float = True
            else:
                digits.append(int(symbol))

        print(f"symbols: {symbols}\ndigits: {digits} sign: {sign} is_float: {is_float}")
        return None


def main():
    solution: Solution = Solution()

    print("42:")
    print(f'{solution.my_atoi("42")}')

    print("   -42:")
    print(f'{solution.my_atoi("   -42")}')

    print("4193 with words:")
    print(f'{solution.my_atoi("4193 with words")}')

    print("-91283472332:")
    print(f'{solution.my_atoi("-91283472332")}')

    print("-56.73 472332")
    print(f'{solution.my_atoi("-56.73 472332")}')


if __name__ == "__main__":
    main()
