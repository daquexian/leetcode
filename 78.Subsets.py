# similar to No.77

import sys

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        i = 0
        l = len(nums)
        s = [0] * l
        res = []
        while i >= 0:
            s[i] += 1
            if s[i] > l:
                i -= 1
                continue
            res.append(s[:i + 1])
            if i < l - 1:
                i += 1
                s[i] = s[i - 1]
        for i, x in enumerate(res):
            res[i] = map(lambda j: nums[j - 1], x)
        res.append([])
        return res

nums = eval(sys.argv[1])
print(Solution().subsets(nums))
