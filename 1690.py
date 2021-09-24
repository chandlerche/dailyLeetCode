class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        dp = [0] * len(stones)
        sums = stones.copy()
        for i in range(1, len(stones)):
            for j in range(len(stones) - i):
                dp[j] = max(sums[j] - dp[j], sums[j + 1] - dp[j + 1])
                sums[j] += stones[j + i]
        return dp[0]