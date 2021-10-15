class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        dp = [1 for _ in range(K + 1)]
        diff = N - K
        for k in range(1, K + 1):
            if k == 1:
                dp[k] = (diff + 1) / W if diff + 1 < W else 1 
            else:
                if k -W - 1 > 0:
                    dp[k] = (W + 1) / W * dp[k - 1] - dp[k - W - 1] / W
                elif W <= diff + k - 1:
                    dp[k] = (W + 1) / W * dp[k - 1] - 1 / W
                else:
                    dp[k] = (W + 1) / W * dp[k - 1]
            # print(k, dp[k])
        return dp[K]