class Solution:
    def insert(self, intervals: [[int]], newInterval: [int]) -> [[int]]:
        result = []
        i = 0
        # Add all intervals that end before the new interval starts
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        
        # Merge all overlapping intervals with the new interval
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
            i += 1
        result.append(newInterval)
        
        # Add the rest of the intervals
        while i < len(intervals):
            result.append(intervals[i])
            i += 1
        
        return result

# Test the implementation
tmp = Solution()
print(tmp.insert(intervals = [[1,3],[6,9]], newInterval = [2,5]))
