import sys

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = ''
        for i in range(len(num2)):
            for j in range(len(num1)):
                digit_product = self.multiply_digit(num1[i], num2[j])
                result = self.str_plus(result, digit_product)

    def str_plus(self, num1, num2):
        flag = 0
        ret = ''
        i = 0
        maxlen = max(len(num1), len(num2))
        while i < maxlen:
            if i >= len(num1):
                digitnum = int(num2[i]) + flag
            elif i >= len(num2):
                digitnum = int(num1[i]) + flag
            else:
                digitnum = int(num1[i]) + int(num2[i]) + flag
            if digitnum >= 10:
                digitnum %= 10
                flag = 1
            else:
                flag = 0
            ret = str(digitnum) + ret
        if flag == 1:
            ret = '1' + ret

    def multiply_digit(self, digit1, digit2):
        """
        :type digit1: str
        :type digit2: str
        :rtype: str
        """
        return str(int(digit1) * int(digit2))
