class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        mod = 10 ** 9 + 7
        dp = [[0 for _ in range(k + 1)] for _ in range(n)]
        dp_sum = [[0 for _ in range(k + 1)] for _ in range(n)]
        # dp_sum[i][j] = dp[i][j] + dp[i - 1][j] * 2 + dp[i - 2][j] * 3 ...
        
        for j in range(1, k + 1):
            cnt_sum = 0
            for i in range(1, n):
                if j > i:
                    continue
                dp[i][1] = 1
                if i == j or j == 1:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp_sum[i - 1][j - 1]
                
                dp[i][j] %= mod
                cnt_sum += dp[i][j]
                dp_sum[i][j] = (dp_sum[i - 1][j] + cnt_sum) % mod

        return sum([dp[x][k] * (n - x) % mod for x in range(1, n)]) % mod