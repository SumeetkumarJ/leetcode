
class Solution:
    def myPow(self, x: float, n: int) -> float:
        negative = n < 0
        n = abs(n)

        result = 1.0

        while n > 0:
            if n % 2 == 1:
                result *= x

            x *= x
            n //= 2

        if negative:
            result = 1.0 / result

        return result
