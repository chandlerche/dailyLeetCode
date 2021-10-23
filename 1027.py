class Solution:
    def longestArithSeqLength(self, A):
        n = len(A)
        max_len = 2

        # dp[i]: A[i]表示以A[i]为等差数列终点
        # dp[i] = {}, {}的key为A[i]为终点的等差数列的差值diff,value表示该等差数列的长度
        dp = [{} for _ in range(n)]

        # 注意双重循环的start和end, i为被减数的索引，j为减数的索引，j<i
        for i in range(1, n):
            for j in range(i):
                k = A[i] - A[j]         # 差值 = 后值 - 前值
                # dp[j].get(k, 1)：字典dp[j]如果存在key=k,返回对应value，否则返回默认值1
                m = dp[j].get(k, 1) + 1
                dp[i][k] = m
            max_len = max(max_len, max(dp[i].values()))
        return max_len