# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """

        # My solution:
        '''
        i = 0
        while i < len(intervals):
            interval = intervals[i]
            if interval.end >= newInterval.start:
                if interval.start <= newInterval.end:
                    interval.start = min(interval.start, newInterval.start)
                    interval.end = max(interval.end, newInterval.end)
                    j = i + 1
                    while j < len(intervals) and intervals[j].start <= interval.end:
                        interval.end = max(interval.end, intervals[j].end)
                        intervals.remove(intervals[j])
                else:
                    intervals.insert(i, newInterval)
                break
            i += 1
        if i == len(intervals):
            intervals.append(newInterval)
        return intervals
        '''

        # Best solution
        s, e = newInterval.start, newInterval.end
        left = [i for i in intervals if i.end < s]
        right = [i for i in intervals if i.start > e]
        if left + right != intervals:
            s = min(s, intervals[len(left)].start)
            e = max(e, intervals[~len(right)].end)
        return left + [Interval(s, e)] + right
