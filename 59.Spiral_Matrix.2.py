import sys

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0] * n for i in range(n)]
        num = 1
        for loop in range((n + 1) / 2):
            length = n - 2 * loop
            num_per_loop = (length - 1) * 4 if length > 1 else 1
            for i in range(num_per_loop):
                top, left, bottom, right = loop, loop, loop + length - 1, loop + length - 1
                n1, n2, n3, n4 = length - 1, (length - 1) * 2, (length - 1) * 3, (length - 1) * 4
                if i < n1:
                    y, x = top, left + i
                elif i < n2:
                    y, x = top + (i - n1), right
                elif i < n3:
                    y, x = bottom, right - (i - n2)
                else:
                    y, x = bottom - (i - n3), left
                res[y][x] = num
                num += 1
        return res

n = eval(sys.argv[1])
print Solution().generateMatrix(n)
