class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        pairs = [(capital[i], profits[i]) for i in range(n)]
        pairs.sort(key=lambda it:it[0])
        q, idx = [], 0
        while k > 0:
            while idx < n and pairs[idx][0] <= w:
                heapq.heappush(q, -pairs[idx][1])
                idx += 1
            if len(q) > 0:
                w -= heapq.heappop(q)
            else:
                break
            k -= 1
        return w