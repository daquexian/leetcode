import sys

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits)):
            digits[~i] += 1
            if digits[~i] == 10:
                digits[~i] = 0
                if i == len(digits) - 1:
                    digits.insert(0, 1)
            else:
                break
        return digits

digits = eval(sys.argv[1])
print Solution().plusOne(digits)
