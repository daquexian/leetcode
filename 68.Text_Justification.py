import sys

class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        length = 0
        words_line = []
        res = []
        i = 0
        while i < len(words):
            word = words[i]
            if length + len(word) <= maxWidth:
                length += 1 + len(word)
                words_line.append(word)
                i += 1
            else:
                space_len = maxWidth - length + 1
                if len(words_line) > 1:
                    spaces = self.splitEvenly(space_len, len(words_line) - 1)
                    new_line = ""
                    for j in range(len(words_line)):
                        w = words_line[j]
                        new_line += w
                        if j != len(words_line) - 1:
                            new_line += ' ' + ' ' * spaces[j]
                else:
                    new_line = words_line[0] + ' ' * space_len
                res.append(new_line)
                words_line = []
                length = 0
        new_line = ''
        if len(words_line) > 0:
            for i in range(len(words_line)):
                w = words_line[i]
                new_line += w
                if i != len(words_line) - 1:
                    new_line += ' '
            new_line += ' ' * (maxWidth - len(new_line))
            res.append(new_line)
        return res

    def splitEvenly(self, length, num):
        a = length % num
        ret = [length / num + 1] * a + [length / num] * (num - a)
        return ret

words = eval(sys.argv[1])
maxWidth = eval(sys.argv[2])

res = Solution().fullJustify(words, maxWidth)
print res
print [len(x) for x in res]
