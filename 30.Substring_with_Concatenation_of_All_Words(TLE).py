# This is the solution of No.30 problem in LeetCode, https://leetcode.com/problems/substring-with-concatenation-of-all-words/
# It's not accepted, but TLE

import sys

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        words_dict = dict()
        count = len(words)
        for word in words:
            words_dict[word] = words_dict.get(word, 0) + 1
        word_len = len(words[0])
        res = []
        for i in range(word_len):
            time_dict = dict()
            j = k = i
            while k < len(s):
                word = s[k : k + word_len]
                if word in words_dict:
                    time_dict[word] = time_dict.get(word, 0) + 1
                    count -= 1
                    k += word_len
                    if time_dict[word] > words_dict[word]:
                        while True:
                            first_word = s[j : j + word_len]
                            j += word_len
                            time_dict[first_word] -= 1
                            count += 1
                            if first_word == word:
                                break
#                if word in words_dict and time_dict.get(word, 0) < words_dict[word]:
#                    time_dict[word] = time_dict.get(word, 0) + 1
#                    count -= 1
#                    k += word_len
#                elif word in words_dict:
#                    k += word_len
#                    time_dict[word] += 1
#                    count -= 1
#                    while True:
#                        first_word = s[j : j + word_len]
#                        j += word_len
#                        time_dict[first_word] -= 1
#                        count += 1
#                        if first_word == word:
#                            break
                else:
                    j += word_len
                    k = j
                    words_dict = dict()
                    time_dict = dict()
                    count = len(words)
                    for word in words:
                        words_dict[word] = words_dict.get(word, 0) + 1
                if count == 0:
                    res.append(j)
        return res
                    
s = sys.argv[1]
words = eval(sys.argv[2])
print Solution().findSubstring(s, words)

