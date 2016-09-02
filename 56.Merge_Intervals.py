import sys

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals = sorted(intervals, key=lambda x:x.start)
        i = 0
        while i < len(intervals):
            interval = intervals[i]
            if i < len(intervals) - 1:
                next_interval = intervals[i + 1]
                if next_interval.start <= interval.end:
                    interval.end = max(interval.end, next_interval.end)
                    intervals.remove(next_interval)
                    continue
            i += 1
        return intervals

intervals = eval(sys.argv[1])


