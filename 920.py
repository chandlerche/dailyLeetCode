class Solution:
    def numMusicPlaylists(self, N: int, L: int, K: int) -> int:
        mod = 10**9 + 7
        dp = [0] + [0]*N 
        tmp = [1] + [0]*N
        for i in range(1, L+1):
            for j in range(1, N+1):
                dp[j] = tmp[j-1]*(N-j+1) + tmp[j]*max(j-K, 0)
            tmp = dp[:]
        return dp[N] % mod