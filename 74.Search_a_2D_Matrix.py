import sys

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        m, n = 0, len(matrix[0]) - 1
        while matrix[m][n] != target:
            t = matrix[m][n]
            if t < target:
                m += 1
            elif t > target:
                n -= 1
            if m >= len(matrix) or n < 0:
                return False
        return True

matrix = eval(sys.argv[1])
target = eval(sys.argv[2])

print(Solution().searchMatrix(matrix, target))
