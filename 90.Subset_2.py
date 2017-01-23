'''
https://leetcode.com/problems/subsets-ii/

Given a collection of integers that might contain duplicates, nums, return all
possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
'''


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        i = 0
        res = [[]]
        while i < len(nums):
            n = 1
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i, n = i + 1, n + 1
            new_list = []
            for j in range(n):
                new_list.extend([x + (j + 1) * [nums[i]] for x in res])
            res.extend(new_list)
            i += 1
        return res

nums = []
print(Solution().subsetsWithDup(nums))
