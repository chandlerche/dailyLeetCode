class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n = len(board)
        dp = [[[0,0] for i in range(n + 1)] for i in range(n + 1)]
        # 把S看成1方便处理
        dp[n - 1][n - 1] = [1,1]
        for x in range(n - 1, -1, -1):
            for y in range(n - 1, -1, -1):
                # 计算转移的最大值
                max_sum = max(dp[x + 1][y + 1][0], dp[x][y + 1][0], dp[x + 1][y][0])
                if board[x][y] != 'X':
                    # 确保有路可以走过来
                    if max_sum or (x, y) == (n - 1,n - 1):
                        dp[x][y][0] += max_sum + (int(board[x][y]) if board[x][y] not in ['S','E'] else 0)
                        dp[x][y][0] %= (10 ** 9 + 7)
                        # 等于最大值的状态的路的数量都加过来
                        for dx, dy in {(1,0),(1,1),(0,1)}:
                            if dp[x + dx][y + dy][0] == max_sum:
                                dp[x][y][1] += dp[x + dx][y + dy][1]
                else:
                    dp[x][y] = [0,0]
        return [dp[0][0][0] - 1 if dp[0][0][0] != 0 else 0, dp[0][0][1] % (10 ** 9 + 7)]