import sys

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
	if x == 0:
		return 0
        i = 1
        while not (i * i <= x and (i + 1) ** 2 > x):
		i = (i + x / i) / 2
	return i	

x = eval(sys.argv[1])
print(Solution().mySqrt(x))
