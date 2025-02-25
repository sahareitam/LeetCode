class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        res = []
        i = 0
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        new = newInterval
        while i < len(intervals) and newInterval[1] >= intervals[i][0]:
            new = [min(new[0], intervals[i][0]), max(new[1], intervals[i][1])]
            i += 1

        res.append(new)

        while i < len(intervals):
            res.append(intervals[i])
            i += 1

        return res
