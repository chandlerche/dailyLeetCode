class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        row = len(matrix)
        col = len(matrix[0])
        dp = [[0] * col for _ in range(row)]
        dp[0] = matrix[0]
        for i in range(1,row):
            for j in range(col):
                if(j == 0):
                    dp[i][j] = min(dp[i-1][0], dp[i-1][1]) + matrix[i][j]
                elif (j == col - 1):
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + matrix[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i-1][j+1]) + matrix[i][j]
        return min(dp[row-1])