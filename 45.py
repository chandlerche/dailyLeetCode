class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float('inf')] * (n) 
        dp[0] = 0
        for i in range(1,n):
            for k in range(i):
                if k + nums[k] >= i: # 可以转移
                    dp[i] = min(dp[i],dp[k]+1)
        return dp[-1]