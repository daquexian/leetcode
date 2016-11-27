import sys

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
        res = []

        row_inc = [0, 1, 0, -1]
        col_inc = [1, 0, -1, 0]
        top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        # item = matrix[row][col], aka (col, row)
        row, col = 0, 0
        i = 0

        while left <= right and top <= bottom:
            res.append(matrix[row][col])

            next_col = col + col_inc[i]
            next_row = row + row_inc[i]
            if next_col < left or next_col > right or next_row < top or next_row > bottom:
                i = (i + 1) % 4
                if next_col < left:
                    bottom -= 1
                elif next_col > right:
                    top += 1
                elif next_row < top:
                    left += 1
                else:
                    right -= 1
            col += col_inc[i]
            row += row_inc[i]
        return res

        '''
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
        '''

matrix = eval(sys.argv[1])
print(Solution().spiralOrder(matrix))
