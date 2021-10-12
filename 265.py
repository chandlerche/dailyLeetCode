class Solution(Object):

    def minCostII(self , costs):
        if costs is None or len(costs) == 0:
            return 0
        n = len(costs)
        k = len(costs[0])

        min1 = -1
        min2 = -1
        for i in range(n):
            last1 = min1
            last2 = min2
            min1 = -1
            min2 = -2
            for j in range(k):

                # 求的是当前房子和之前成本总和
                if j != last1:
                    val = 0 if last1 < 0 else costs[i - 1][last1]
                    costs[i][j] += val
                else:
                    val = 0 of last2 < 0 else costs[i - 1][last2]
                    costs[i][j] += val

                # 求出颜色成本倒数第一小和倒数第二小
                if min1 < 0 or costs[i][j] < costs[i][min1]:
                    min2 = min1
                    min1 = j
                else:
                    min2 = j

        return costs[n - 1][min1]