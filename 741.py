class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        dp = [[[-sys.maxsize for _ in range(m)] for _ in range(m)] for _ in range(m)]
        for row1 in range(m):
            for col1 in range(m):
                for row2 in range(m):
                    col2 = row1 + col1 - row2
                    if col2 < 0 or col2 >= m:
                        continue
                    if grid[row1][col1] == -1 or grid[row2][col2] == -1:
                        continue
                    if row1 == 0 and col1 == 0:
                        dp[row1][col1][row2] = grid[0][0]
                        continue
                    # 1号向下，2号也向下
                    method1 = dp[row1][col1 - 1][row2] if col1 - 1 >= 0 and col2 - 1 >= 0 else -sys.maxsize
                    # 1号向右，2号向下
                    method2 = dp[row1 - 1][col1][row2] if row1 - 1 >= 0 and col2 - 1 >= 0 else -sys.maxsize
                    # 1号向下，2号向右
                    method3 = dp[row1][col1 - 1][row2 - 1] if col1 - 1 >= 0 and row2 - 1 >= 0 else -sys.maxsize
                    # 1号向右，2号向右
                    method4 = dp[row1 - 1][col1][row2 - 1] if row1 - 1 >= 0 and row2 - 1 >= 0 else -sys.maxsize
                    dp[row1][col1][row2] = max(method1, method2, method3, method4)
                    dp[row1][col1][row2] += grid[row1][col1]
                    if row1 != row2:
                        dp[row1][col1][row2] += grid[row2][col2]
        if dp[-1][-1][-1] < -sys.maxsize // 2:
            return 0
        return dp[-1][-1][-1]