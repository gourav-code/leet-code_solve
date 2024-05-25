"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([tmp.start for tmp in intervals])
        end = sorted([tmp.end for tmp in intervals])

        i,j = 0,0
        ans, count = 0,0
        while i < len(start):
            if start[i]< end[j]:
                count += 1
                i += 1
            else:
                count -= 1
                j += 1
            ans = max(ans, count)

        return ans
        