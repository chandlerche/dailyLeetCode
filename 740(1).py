class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # 统计每个数字出现的次数、去重、排序
        dic = Counter(nums)
        nums = list(set(nums))
        nums.sort()
        
        # dp[i][0]: nums[0：i+1]中，不删除nums[i]所能获得的最大点数
        # dp[i][1]: 删除nums[i]所能获得的最大点数和
        dp = [[0 for i in range(2)] for _ in range(len(nums))]
        dp[0][0] = 0
        dp[0][1] = nums[0] * dic[nums[0]]

        for i in range(1, len(dp)):
            if nums[i] - nums[i-1] == 1:
                # 与上一元素相差1，则删除nums[i]的情况dp[i][1]，依赖于不删除nums[i-1]的情况，即dp[i-1][0]。
                dp[i][1] = dp[i-1][0] + nums[i] * dic[nums[i]]
            else:
                # 上一元素是否删除，与当前状态无关，选取前一状态获得的最大点数。
                dp[i][1] = max(dp[i-1][0],dp[i-1][1]) + nums[i] * dic[nums[i]]
            # 不删除当前元素，直接取前一状态的最大值。
            dp[i][0] = max(dp[i-1][0],dp[i-1][1])
        
        return max(dp[-1])