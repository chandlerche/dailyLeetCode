class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        N = len(cuboids)
        # 先对每个正方体进行排序(倒序)
        for i in range(N):
            cuboids[i].sort(reverse=True)
        # 对所有正方体（降序）按照第一个元素、第二个元素、第三个元素的优先级进行排序
        cuboids.sort(reverse=True)

        dp = [0] * N
        # 动态规划
        for i in range(0, N):
            dp[i] = cuboids[i][0]
            for j in range(0, i):
                # 当满足条件时，dp[i]进行状态转移
                if cuboids[j][0] >= cuboids[i][0] and cuboids[j][1] >= cuboids[i][1] and cuboids[j][2] >= cuboids[i][2]:
                    dp[i] = max(dp[i], dp[j] + cuboids[i][0])
        return max(dp)