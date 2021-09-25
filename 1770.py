class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        @lru_cache(len(multipliers))
        def dfs(left, right, idx) -> int:
            if idx >= len(multipliers):
                return 0
            multiplier = multipliers[idx]
            idx += 1
            return max(nums[left] * multiplier + dfs(left + 1, right, idx),
                       nums[right] * multiplier + dfs(left, right - 1, idx))

        return dfs(0, len(nums) - 1, 0)