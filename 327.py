from bisect import bisect_left, bisect_right, insort

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        # O(nlogn)
        cache = [0]
        s = 0
        res = 0
        for num in nums:
            s += num
            pl = bisect_left(cache, s-upper)
            pu = bisect_right(cache, s-lower)
            res += pu - pl
            insort(cache, s)
        return res