import sys

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        sorted_strs = map(lambda x: ''.join(sorted(x)), strs)
        str_dict = {}
        l = len(strs)
        for i in range(l):
            if not sorted_strs[i] in str_dict:
                str_dict[sorted_strs[i]] = []
            str_dict[sorted_strs[i]].append(strs[i])
        return str_dict.values()
#        return list(str_dict)

strs = eval(sys.argv[1])
print Solution().groupAnagrams(strs)
#Solution().groupAnagrams(strs)
