class Solution(object):
    def minimumMoves(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        dp = [[100] * n for _ in range(n)]
                
        for i in range(n-1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, n):
                if j == n:
                    break
                dp[i][j] = 1 + (dp[i+1][j] if i+1<n else 0)
                for k in range(i+1, j+1):
                    if arr[i] == arr[k]:
                        if k == i + 1:
                            dp[i][j] = min(dp[i][j], 1 + (dp[k+1][j] if k+1<=j else 0))
                        else:
                            dp[i][j] = min(dp[i][j], dp[i+1][k-1] + (dp[k+1][j] if k+1<=j else 0))
        return dp[0][n-1]