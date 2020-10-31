class Solution:
    def dfs(self, piles, n, i, j):
        if i >= n:
            return 0
        if (i, j) in self.vis:
            return self.vis[(i, j)]

        j = min(j, n - i)
        stones = sum(piles[i:])
        if n - i == j:  
            self.vis[(i, j)] = stones
            return stones

        min_dp = 1e10
        for k in range(1, j + 1): 
            min_dp = min(min_dp, self.dfs(piles, n, i + k, max(j, 2 * k)))
        self.vis[(i, j)] = stones - min_dp
        return stones - min_dp

    def stoneGameII(self, piles: List[int]) -> int:
        self.vis = {}
        return self.dfs(piles, len(piles), 0, 2)