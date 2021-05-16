class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        import functools
        satisfaction.sort()
        
        @functools.lru_cache(None)
        def dfs(i, cur):
            if i == len(satisfaction):
                return 0
            return max(dfs(i + 1, cur), satisfaction[i] * cur + dfs(i + 1, cur + 1))
        
        return dfs(0, 1)