import sys

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res = ''
        candidates = list(range(1, n + 1))
        f = reduce(lambda x, y:x * y, range(1, n)) if n > 1 else 1 # (n - 1)!
        while True:
            digit = candidates[(k - 1) / f]
            res += str(digit)
            candidates.remove(digit)
            k %= f
            if n == 1:
                break
            f /= (n - 1)
            n -= 1
        return res

n = eval(sys.argv[1])
k = eval(sys.argv[2])
print Solution().getPermutation(n, k)
