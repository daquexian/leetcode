import sys

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        rows = len(matrix)
        if rows == 0:
            return []
        cols = len(matrix[0])
        res = []
        left, right, top, bottom = 0, cols - 1, 0, rows - 1
        while rows > 1 and cols > 1:
            value1, value2, value3 = cols - 1, cols + rows - 2, 2 * cols + rows - 3
            for i in range(2 * rows + 2 * cols - 4):
                if i < value1:
                    res.append(matrix[top][left + i])
                elif i < value2:
                    res.append(matrix[top + (i - value1)][right])
                elif i < value3:
                    res.append(matrix[bottom][right - (i - value2)])
                else:
                    res.append(matrix[bottom - (i - value3)][left])
            cols -= 2
            rows -= 2
            left, right, top, bottom = left + 1, left + 1 + cols - 1, top + 1, top + 1 + rows - 1
        if rows == 1 and cols > 0:
            res.extend(matrix[top][left:right+1])
        elif cols == 1 and rows > 0:
            res.extend([matrix[top + i][left] for i in range(rows)])
        return res
