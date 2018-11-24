#!/usr/bin/env python3


class Solution(object):
    def __init__(self):
        self.dict = {"1": ["*"], "2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], "5": ["j", "k", "l"], "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"], "0": [" "]}

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []
        combos = [""]
        for i in range(len(digits)):
            combos = self.mix(digits[i], combos)
        return combos

    def mix(self, digit, combos):
        return [j + i for i in self.dict[digit] for j in combos]


if __name__ == "__main__":
    s = Solution()
    digits = "23"
    result = s.letterCombinations(digits)
    print(result)
