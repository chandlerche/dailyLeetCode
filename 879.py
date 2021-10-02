class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        MOD = 10**9 + 7
        length = len(group)
        dp = [[[0] * (minProfit + 1) for _ in range(n + 1)] for _ in range(length + 1)]
        #i,j,k分别表示，选择前i个工作，且员工数量不超过j时，所创造的总利润大于等于k的计划数
        dp[0][0][0] = 1#啥也不干也是一种方案
        for i in range(1, length + 1):
            #第i个工作的所需的人数及创造的利润数
            members, earn = group[i - 1], profit[i - 1]
            for j in range(n + 1):
                for k in range(minProfit + 1):
                    #所需的员工数量大于j，则说明无法选择当前这个工作
                    if j < members:
                        dp[i][j][k] = dp[i - 1][j][k]
                    else:
                        #这样好理解一点，前置任务所创造的利润+第i个任务的利润要大于等于k
                        #第i个任务自己的利润就已经大于等于k了，则所有前置任务的利润只需要大于等于k-earn就行
                        #由于利润不能为负数，所有从0开启
                        if k <= earn:
                            dp[i][j][k]=dp[i-1][j][k]+dp[i-1][j - members][0] %MOD
                        else:
                            dp[i][j][k] = (dp[i - 1][j][k] + dp[i - 1][j - members][k - earn]) % MOD
        #遍历一遍，在选择前length个工作，且员工数量不超过[0,n]时，所创造的总利润大于等于minProfit的计划数
        total = sum(dp[length][j][minProfit] for j in range(n + 1))
        return total % MOD