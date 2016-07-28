# This is the solution of No.36 problem in LeetCode, https://leetcode.com/problems/valid-sudoku/
# It's relatively easy.

import sys

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        x = y = 1
        for i in range(3):
            for j in range(3):
                is_occupied = [False] * 9
                x, y = 1 + 3 * i, 1 + 3 * j
                for k in range(-1, 2):
                    for l in range(-1, 2):
                        if board[x + k][y + l] != '.':
                            num = ord(board[x + k][y + l]) - ord('1')
                            if is_occupied[num]:
                                return False
                            is_occupied[num] = True
        for i in range(9):
            is_occupied = [False] * 9
            for j in range(9):
                if board[i][j] != '.':
                    num = ord(board[i][j]) - ord('1')
                    if is_occupied[num]:
                        return False
                    is_occupied[num] = True
        for j in range(9):
            is_occupied = [False] * 9
            for i in range(9):
                if board[i][j] != '.':
                    num = ord(board[i][j]) - ord('1')
                    if is_occupied[num]:
                        return False
                    is_occupied[num] = True
        return True
