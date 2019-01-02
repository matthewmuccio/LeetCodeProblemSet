#!/usr/bin/env python3


from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = defaultdict(list)

        for s in strs:
            res[self.hash(s)].append(s)

        return [v for v in res.values()]

    def hash(self, word):
        counts = [0] * 26

        for w in word:
            counts[ord(w) - ord("a")] += 1

        return str(counts)


if __name__ == "__main__":
    s = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = s.groupAnagrams(strs)
    print(result)
