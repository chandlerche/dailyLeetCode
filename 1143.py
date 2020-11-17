class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1, n2 = len(text1), len(text2)
        pre = [0 for _ in range(n2 + 1)]
        dp = [0 for _ in range(n2 + 1)]
        for i in range(n1):
            for j in range(1, n2 + 1):
                if text1[i] == text2[j-1]:
                    dp[j] = pre[j-1] + 1
                else:
                    dp[j] = max(pre[j], dp[j-1])
                pre[j-1] = dp[j-1]
            pre[j] = dp[j]
        return dp[-1]