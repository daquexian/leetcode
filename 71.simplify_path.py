import sys

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        s = []
        name_list = path.split('/')
        res = '/'
        for name in name_list:
            if name == '..':
                if len(s) > 0:
                    s.pop()
            elif name != '.' and name != '':
                s.append(name)

        for i in range(len(s)):
            res += s[i]
            if i != len(s) - 1:
                res += '/'
        return res

path = sys.argv[1]
print(Solution().simplifyPath(path))
