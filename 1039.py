from typing import List


class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:
        n = len(A)
        dp = [[float('inf')] * n for _ in range(n)]
        for j in range(n):
            for i in reversed(range(j)):
                if j - i < 2:
                    dp[i][j] = 0
                else:
                    for k in range(i+1, j):
                        dp[i][j] = min(dp[i][j], A[i]*A[j]*A[k]+dp[i][k]+dp[k][j])
        return dp[0][n-1]