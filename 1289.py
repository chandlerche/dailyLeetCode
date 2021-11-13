class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        dp = [[0]*len(arr) for _ in range(len(arr))]
        dp[0] = arr[0]
        for i in range(1, len(arr)):
            min_sum = min(dp[i-1])
            for j in range(len(arr)):
                if dp[i-1][j] != min_sum:
                    dp[i][j] = min_sum + arr[i][j]
                else:
                    dp[i][j] = arr[i][j] + min(dp[i-1][:j]+dp[i-1][j+1:])
        return min(dp[-1])