import sys

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        arr = [0] * 3
        for num in nums:
            arr[num] += 1
        top = 0
        for i in range(len(arr)):
            for j in range(arr[i]):
                nums[top] = i
                top += 1

nums = eval(sys.argv[1])
Solution().sortColors(nums)
print(nums)
