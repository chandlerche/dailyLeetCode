class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        @lru_cache(None)
        def dfs(start, finish, fuel):
            if fuel < 0:
                return 0
            res = 0
            if start == finish:
                res += 1
            for i in range(len(locations)):
                if i == start:
                    continue
                res += dfs(i, finish, fuel - abs(locations[start] - locations[i]))    
            return res%(10**9 + 7)    
        return dfs(start, finish, fuel)