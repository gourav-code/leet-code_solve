class Solution:
    def merge(self, intervals: [[int]]) -> [[int]]:
        intervals.sort(key= lambda tmp: tmp[0])
        start = intervals[0]
        i = 1
        result = []
        while i<len(intervals):
            if start[1] >= intervals[i][0]:
                start = [start[0], max(intervals[i][1], start[1])]
                i += 1
            else:
                result.append(start.copy())
                start = intervals[i].copy()
                i += 1

        result.append(start.copy())
        return result