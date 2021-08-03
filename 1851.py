class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        heap = []
        intervalsLen = len(intervals)
        queriesLen = len(queries)
        ret = [-1] * queriesLen

        intervals = sorted(intervals, key = lambda x: x[0])
        queriesSort = []
        for queriesIdx in range(queriesLen):
            queriesSort.append([queries[queriesIdx], queriesIdx])
        queriesSort = sorted(queriesSort, key = lambda x: x[0])

        intervalsIdx = 0
        for queriesIdx in range(queriesLen):
            while intervalsIdx < intervalsLen and intervals[intervalsIdx][0] <= queriesSort[queriesIdx][0]:
                heapq.heappush(heap, [intervals[intervalsIdx][1] - intervals[intervalsIdx][0] + 1, intervals[intervalsIdx][0], intervals[intervalsIdx][1]])
                intervalsIdx += 1

            while heap and heap[0][2] < queriesSort[queriesIdx][0]:
                heapq.heappop(heap)
            
            if heap:
                ret[queriesSort[queriesIdx][1]] = heap[0][0]
        
        return ret