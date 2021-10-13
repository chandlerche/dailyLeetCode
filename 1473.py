class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        @lru_cache(None)
        def dfs( idx, cur, parts):#求在0~idx区间，以cur作为最后颜色，划分parts个区域的代价
            if parts > idx + 1:#剪枝
                return inf
            if houses[ idx] and houses[ idx] != cur:#与指定颜色不符
                return inf
            else:
                if idx == 0:
                    res = 0 if parts == 1 else inf
                else:
                    res=min( dfs( idx - 1, pre, parts - 1 + ( pre == cur )) for pre in range( 1, n + 1))
                return res + (0 if houses[ idx] == cur else cost[ idx][ cur - 1])

        ans = min( dfs( m - 1, i, target) for i in range( 1, n + 1))
        return ans if ans != inf else -1