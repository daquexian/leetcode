import sys

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.row, self.col, self.cl1, self.cl2, self.res = [True] * n, [True] * n, [True] * (2 * n - 1), [True] * (2 * n - 1), 0
        for i in range(n):
            self.__solve(n, i, 0)
        return self.res

    def __solve(self, n, i, j):
        row_num, col_num, cl1_num, cl2_num = self.get_row(i, j, n), self.get_col(i, j, n), self.get_cl1(i, j, n), self.get_cl2(i, j, n)
        if self.row[row_num] and self.col[col_num] and self.cl1[cl1_num] and self.cl2[cl2_num]:
            self.row[row_num] = self.col[col_num] = self.cl1[cl1_num] = self.cl2[cl2_num] = False
            #self.ans[row_num][col_num] = 'Q'
            if col_num == n - 1:
		self.res += 1
                #self.res.append([''.join(x) for x in self.ans])
            else: 
                for k in range(n):
                    self.__solve(n, k, col_num + 1)
            #self.ans[row_num][col_num] = '.'
            self.row[row_num] = self.col[col_num] = self.cl1[cl1_num] = self.cl2[cl2_num] = True

    def get_cl1(self, i, j, n):
        return i - j + n - 1
    def get_cl2(self, i, j, n):
        return i + j
    def get_row(self, i, j, n):
        return i
    def get_col(self, i, j, n):
        return j

n = eval(sys.argv[1])
print Solution().solveNQueens(n)
