# inspired by https://discuss.leetcode.com/topic/8981/short-code-by-c

import sys

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        i = j = flag = 0
        res = ''
        while i < len(a) or j < len(b) or flag == 1:
            digit = 0
            if i < len(a):
                digit += int(a[~i])
                i += 1
            if j < len(b):
                digit += int(b[~j])
                j += 1
            digit += flag
            flag = 1 if digit >= 2 else 0
            digit %= 2
            res = str(digit) + res
        '''
        if len(b) > len(a):
            return self.addBinary(b, a)
        res = ''
        flag = 0
        for i in range(len(b)):
            digit = int(a[~i]) + int(b[~i]) + flag
            if digit >= 2:
                digit %= 2
                flag = 1
            else:
                flag = 0
            res = str(digit) + res
        for i in range(len(b), len(a)):
            digit = int(a[~i]) + flag
            if digit == 2:
                digit = 0
                flag = 1
            else:
                flag = 0
            res = str(digit) + res
        if flag == 1:
            res = '1' + res
        '''
        return res

a = sys.argv[1]
b = sys.argv[2]
print Solution().addBinary(a, b)
