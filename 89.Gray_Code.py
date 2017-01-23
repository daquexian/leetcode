class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        # my solution:
        '''
        if n == 0:
            return [0]
        delta, nums = [1], [0]
        k = 2

        for i in range(1, 2 ** n - 1):
            if i == k - 1:
                delta.append(k)
                k *= 2
            else:
                delta.append(-delta[k - i - 2])

        for d in delta:
            nums.append(nums[-1] + d)

        return nums
        '''
        # best solution! It's amazing, but I have to figure out why
        return [i ^ (i // 2) for i in range(n)]

n = 4
print(Solution().grayCode(n))
