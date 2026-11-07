
class Solution:
    def myAtoi(self, s: str) -> int:

        INT_MIN = -(2**31)
        INT_MAX = 2**31 - 1

        i = 0
        n = len(s)

        # Step 1: Skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1

        # Step 2: Check the sign
        sign = 1

        if i < n and s[i] == '-':
            sign = -1
            i += 1
        elif i < n and s[i] == '+':
            i += 1

        # Step 3: Convert digits into integer
        num = 0

        while i < n and '0' <= s[i] <= '9':
            digit = ord(s[i]) - ord('0')

            num = num * 10 + digit

            # Step 4: Check overflow
            if sign * num <= INT_MIN:
                return INT_MIN

            if sign * num >= INT_MAX:
                return INT_MAX

            i += 1

        return sign * num
