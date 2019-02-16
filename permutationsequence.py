#!/usr/bin/env python3


import math


class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        numbers = [i for i in range(1, n + 1)]
        permutation = ""
        k -= 1

        while n > 0:
            n -= 1
            index, k = divmod(k, math.factorial(n))
            permutation += str(numbers[index])
            numbers.remove(numbers[index])

        return permutation


if __name__ == "__main__":
    s = Solution()
    n = 3
    k = 3
    result = s.getPermutation(n, k)
    print(result)
