import sys

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
	if len(matrix) == 0:
		return
	deleted_col = set()
	deleted_row = set()

	row_num = len(matrix)
	col_num = len(matrix[0])
	for i in range(col_num):
		for j in range(row_num):
			if matrix[j][i] == 0:
				deleted_col.add(i)
				deleted_row.add(j)
	for row in deleted_row:
		for i in range(col_num):
			matrix[row][i] = 0
	for col in deleted_col:
		for i in range(row_num):
			matrix[i][col] = 0
matrix = eval(sys.argv[1])
Solution().setZeroes(matrix)
print(matrix)
