import sys

class Solution(object):
    res = []
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        i = 0
        s = [0] * k
        res = []
        while True:
            s[i] += 1
            if s[i] > n:
                i -= 1
                if i >= 0:
                    continue
                break
            if i == k - 1:
                res.append(s[:])    
            else:
                i += 1
                s[i] = s[i - 1]
        
        return res
        

        '''
        self.get_comb(n, k, [])
        return self.res
        
        
    def get_comb(self, n, k, now):
        if len(now) == k:
            self.res.append(now)
            return
        top = now[-1] if len(now) > 0 else 0
        for i in range(top + 1, n + 1):
            self.get_comb(n, k, now + [i])
            '''

n = eval(sys.argv[1])
k = eval(sys.argv[2])
print(Solution().combine(n, k))
