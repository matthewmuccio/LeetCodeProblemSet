#!/usr/bin/env python3


class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res = []
        curr = []
        num_letters = 0

        for w in words:
            if num_letters + len(w) + len(curr) > maxWidth:
                for i in range(maxWidth - num_letters):
                    curr[i % (len(curr) - 1 or 1)] += " "
                res.append("".join(curr))
                curr, num_letters = [], 0
            curr += [w]
            num_letters += len(w)

        return res + [' '.join(curr).ljust(maxWidth)]


if __name__ == "__main__":
    s = Solution()
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    result = s.fullJustify(words, maxWidth)
    print(result)
