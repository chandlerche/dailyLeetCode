class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def possible(x):
            return sum(math.ceil(n/x) for n in piles) <= h
        
        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            if not possible(mid):
                left = mid + 1
            else:
                right = mid
        return left