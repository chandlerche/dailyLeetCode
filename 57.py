class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        n = len(intervals)
        while i < n and newInterval[0] > intervals[i][1]:
            i += 1
        left = i
        while i < n and newInterval[1] >= intervals[i][0]:
            i += 1
        right = i
        #print(left, right)
        if left >= n:
            res = intervals + [newInterval]
        elif left == right:
            #print(intervals)
            intervals.insert(left, newInterval)
            res = intervals
        else:
            res = intervals[:left] + [
                [min(intervals[left][0], newInterval[0]), max(intervals[right - 1][1], newInterval[1])]] + intervals[
                                                                                                           right:]
        return res