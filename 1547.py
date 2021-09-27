class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.extend([0, n])
        cuts.sort()
        @lru_cache(None)
        def helper(i, j):
            if i + 1 == j:
                return 0
            res = 0x3f3f3f3f
            for k in range(i + 1, j):
                res = min(res, helper(i, k) + helper(k, j) + cuts[j] - cuts[i])
            return res
        return helper(0, len(cuts) - 1)