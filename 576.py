class Solution(object):
    def findPaths(self, m, n, N, i, j):
        dp = [{} for _ in range(N + 1)]
        dp[0][(i, j)] = 1
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        ans = 0
        for step in range(1, N + 1):
            for r, c in dp[step - 1]:
                count = dp[step - 1][(r, c)]
                for dr, dc in dirs:
                    nr, nc = dr + r, dc + c
                    if nr >= m or nc >= n or nr < 0 or nc < 0:
                        ans += count
                        ans %= (10 ** 9 + 7)
                    elif (nr, nc) in dp[step]:
                        dp[step][(nr, nc)] += count
                    else:
                        dp[step][(nr, nc)] = count
        return ans