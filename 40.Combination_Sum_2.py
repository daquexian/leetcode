# This is the solution of No.40 problem in LeetCode, https://leetcode.com/problems/combination-sum-ii/
# The solution is the same as that of No.39, except line 14 and 26

import sys

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret = []
        candidates.sort()
        self.__combinationSum(ret, [], candidates, target)
        return ret
    
    def __combinationSum(self, ret, ans, candidates, target):
        for i in range(len(candidates)):
            if i > 0 and candidates[i] == candidates[i - 1]:
                continue
            x = candidates[i]
            if target >= x:
                new_ans = ans + [x]
                if target > x:
                    self.__combinationSum(ret, new_ans, candidates[i + 1:], target - x)
                else:
                    ret.append(new_ans)

candidates = eval(sys.argv[1])
target = eval(sys.argv[2])

print Solution().combinationSum2(candidates, target)
