class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums = [1] + nums + [1]
        dp = [[0 for j in range(n + 2)] for i in range(n + 2)]
        for length in range(1, n + 3):
            for i in range(n - length + 3):
                j = i + length - 1
                for m in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], dp[i][m] + nums[i] * nums[m] * nums[j] + dp[m][j])
                # print(i, j, dp[i][j])
        return dp[0][n + 1]