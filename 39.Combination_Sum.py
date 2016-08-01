# This is the solution of No.39 problem in LeetCode, https://leetcode.com/problems/combination-sum/

import sys

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret = []
        self.__combinationSum(ret, [], candidates, target)
        return ret
    
    def __combinationSum(self, ret, ans, candidates, target):
        for i in range(len(candidates)):
            x = candidates[i]
            if target >= x:
                new_ans = ans + [x]
                if target > x:
                    self.__combinationSum(ret, new_ans, candidates[i:], target - x)
                else:
                    ret.append(new_ans)

candidates = eval(sys.argv[1])
target = eval(sys.argv[2])

print Solution().combinationSum(candidates, target)
