'''
Given a string containing only digits, restore it by returning all possible
valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
'''


class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        i = len(s) - 1
        dp = [[[] for j in range(5)] for i in range(len(s) + 1)]
        dp[len(s)][0] = [[]]
        while i >= 0:
            for j in range(1, 4):
                if i + j > len(s) or (j >= 2 and s[i] == '0') or \
                        (j == 3 and int(s[i:i + j]) > 255):
                    break
                for k in range(1, 5):
                    dp[i][k] += [[s[i:i + j]] + x for x in dp[i + j][k - 1]]

            i -= 1
        return [".".join(x) for x in dp[0][4]]

s = '25525511135'
print(Solution().restoreIpAddresses(s))
