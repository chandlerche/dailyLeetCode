class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:(x[0],-x[1]))
        n = len(intervals)
        res = n 
        right = intervals[0][1]
        for i in range(1,n):
            if intervals[i][1] <= right:
                res -= 1
            else:
                right = intervals[i][1]

        return res