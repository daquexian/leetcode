import sys

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        MAX_INT = 1 << 31 - 1
        MIN_INT = -1 << 31
        if divisor == 0 or (dividend == MIN_INT and divisor == 1):
            return MAX_INT
        if dividend == 0:
            return 0
        sign = -1 if (divisor < 0) ^ (dividend < 0) else 1
        divisor, dividend = abs(divisor), abs(dividend)
        divisor_b = divisor
        while (divisor << 1) <= dividend:   # should check if divisor << 1 overflows in C/C++
            divisor <<= 1
        res = 0
        while divisor >= divisor_b:
            res <<= 1
            if divisor <= dividend:
                dividend -= divisor
                res |= 1
            divisor >>= 1
        res *= sign
        return res

dividend = eval(sys.argv[1])
divisor = eval(sys.argv[2])

print Solution().divide(dividend, divisor)
