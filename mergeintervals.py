#!/usr/bin/env python3


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        res = []
        for i in sorted(intervals, key=lambda i: i.start):
            if res and i.start <= res[-1].end:
                res[-1].end = max(res[-1].end, i.end)
            else:
                res += i,
        return res


if __name__ == "__main__":
    s = Solution()
    intervals = [Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15, 18)]
    result = s.merge(intervals)
    for r in result:
        print(r.start, r.end)
