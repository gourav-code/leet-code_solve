"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: [Interval]) -> bool:
        intervals.sort(key= lambda tmp: tmp.start)

        for i in range(1,len(intervals)):
            tmp1 = intervals[i-1]
            tmp2 = intervals[i]
            if tmp1.end > tmp2.start:
                return False

        return True