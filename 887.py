class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dp = [0] * (K + 1)
        m = 0
        while dp[K] < N:
            m += 1
            for k in range(K, 0, -1):
                # print(m, k)
                dp[k] = dp[k - 1] + dp[k] + 1
        return m