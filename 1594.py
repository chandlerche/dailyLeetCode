class Solution:
    result = -1
    try_set = set()

    def dfs(self, grid: List[List[int]], n: int, m: int, i=0, j=0, res=1):
        key = tuple((i, j, res))
        if key in self.try_set:
            return

        if i == n - 1 and j == m - 1:
            v = res * grid[i][j]
            if v >= 0:
                self.result = max(self.result, v)
                return

        if i >= n or j >= m:
            return

        self.dfs(grid, n, m, i + 1, j, res * grid[i][j])
        self.dfs(grid, n, m, i, j + 1, res * grid[i][j])
        self.try_set.add(key)

        return

    def maxProductPath(self, grid: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        self.result = -1
        self.try_set = set()
        n = len(grid)
        m = len(grid[0])
        self.dfs(grid, n, m)
        return self.result % mod if self.result >= 0 else -1