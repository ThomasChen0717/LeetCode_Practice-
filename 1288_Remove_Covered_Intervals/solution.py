class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))

        max_end = 0 
        count = 0

        for interval in intervals: 
            if interval[1] <= max_end: 
                count += 1
            else: 
                max_end = max(max_end, interval[1])

        return len(intervals) - count
            