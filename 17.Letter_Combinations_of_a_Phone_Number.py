# This is the solution of No.17 in LeetCode, https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# This is relatively easy in Python :)

import sys

class Solution(object):
    def letterCombinations(self, digits):
        if digits == '':
            return []
        from itertools import product
        letters = [[],
                [],
                ['a', 'b', 'c'],
                ['d', 'e', 'f'],
                ['g', 'h', 'i'],
                ['j', 'k', 'l'],
                ['m', 'n', 'o'],
                ['p', 'q', 'r', 's'],
                ['t', 'u', 'v'],
                ['w', 'x', 'y', 'z']]
        demandLetters = [letters[int(x)] for x in digits]
        return [''.join(x) for x in product(*(demandLetters))]

digits = sys.argv[1]
print Solution().letterCombinations(digits)
