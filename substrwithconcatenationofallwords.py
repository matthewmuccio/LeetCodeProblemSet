#!/usr/bin/env python3


from collections import Counter


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        result = []

        if len(s) == 0 or len(words) == 0:
            return result

        word_length = len(words[0])
        words_count = len(words)
        window_length = words_count * word_length

        temp = []

        for i in range(0, len(s) - window_length + 1):
            word_window = s[i:i + window_length]

            temp = [word_window[j:j + word_length] for j in range(0, window_length, word_length)]

            if Counter(temp) == Counter(words):
                result.append(i)

        return result


if __name__ == "__main__":
    s = Solution()
    s1 = "barfoothefoobarman"
    words = ["foo", "bar"]
    result = s.findSubstring(s1, words)
    print(result)
