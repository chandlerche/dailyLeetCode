class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        n = len(s)
        s = ' '  + s
        dp = [0 for _ in range(n+1)]
        dp[0] = 1
        mod = int(1e9+7)
        for i in range(1, n + 1):
            for j in range(i-1, max(-1, i-10), -1):
                if s[j+1] != '0':
                    if int(s[j+1:i+1])<=k:
                        dp[i] += dp[j]
                        if dp[i] >= mod:
                            dp[i] -= mod
                    else:
                        break
        return dp[n]