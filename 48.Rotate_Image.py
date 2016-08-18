# This is the solution of No.48 problem in LeetCode, https://leetcode.com/problems/rotate-image/

import sys

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n / 2):
            for j in range(i, n - i - 1):
                matrix[i][j], matrix[j][n - 1 - i], matrix[n - 1 - i][n - 1 - j], matrix[n - 1 - j][i] = matrix[n - 1 - j][i], matrix[i][j], matrix[j][n - 1 - i], matrix[n - 1- i][n - 1 - j]
        
matrix = eval(sys.argv[1])
Solution().rotate(matrix)
print matrix
