class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @lru_cache(None)
        def dfs(i: int, t: int) -> int:
            if i == len(nums):
                return 1 if t == 0 else 0
            return dfs(i + 1, t - nums[i]) + dfs(i + 1, t + nums[i])

        return dfs(0, target)