# This is the solution of No.37 problem in LeetCode, https://leetcode.com/problems/sudoku-solver/
# Solve this problem by dfs (backtracking as well)
# Reduce time by using extra spaces to store which numbers are avaliable, just like the skill used in eight queens problem.

import sys

class Solution(object):
    (row, col, block) = ([[True] * 10 for i in range(9)] for j in range(3))
    flag = False
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        # the two lines following are used for make it easy to test the code on my own computer
        #for i in range(9):
        #    board[i] = list(board[i])
        (self.row, self.col, self.block) = ([[True] * 10 for i in range(9)] for j in range(3))
        self.flag = False
        for x in range(9):
            for y in range(9):
                if board[y][x] != '.':
                    num = int(board[y][x])
                    self.row[y][num] = self.col[x][num] = self.block[self.blockNum(x, y)][num] = False
        
        self.dfs(board, 0, 0)

    def dfs(self, board, x, y):
        if y == 9:
            self.flag = True
        if not self.flag:
            if board[y][x] == '.':
                for n in range(1, 10):
                    if self.isValid(x, y, n):                                                           # if n is avaliable
                        self.row[y][n] = self.col[x][n] = self.block[self.blockNum(x, y)][n] = False    # mark n as unavaliable
                        board[y][x] = str(n)                                                            # fill n in board
                        self.dfs(board, x + 1 if x < 8 else 0, y if x < 8 else y + 1)
                        if not self.flag:                                                               # restore board only if it isn't completed
                            board[y][x] = '.'
                            self.row[y][n] = self.col[x][n] = self.block[self.blockNum(x, y)][n] = True
            else:
                        self.dfs(board, x + 1 if x < 8 else 0, y if x < 8 else y + 1)

    def isValid(self, x, y, num):
        return self.row[y][num] and self.col[x][num] and self.block[self.blockNum(x, y)][num]
        
    def blockNum(self, x, y):
        return y / 3 * 3 + x / 3

board = eval(sys.argv[1])
Solution().solveSudoku(board)
print board
