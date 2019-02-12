#!/usr/bin/env python3


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        new = []
        i = 0

        for i, it in enumerate(intervals):
            if newInterval.end < it.start:
                i -= 1; break
            elif it.end < newInterval.start:
                new += it,
            else:
                newInterval.start = min(it.start, newInterval.start)
                newInterval.end = max(it.end, newInterval.end)

        return new + [newInterval] + intervals[i + 1:]


if __name__ == "__main__":
    s = Solution()
    intervals = [Interval(1, 3), Interval(6, 9)]
    newInterval = Interval(2, 5)
    result = s.insert(intervals, newInterval)
    for r in result:
        print(r.start, r.end)
