class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        """
        完全背包问题
        f[i][j]表示考虑[1,...,i]成本为恰好j的最大整数
        f[i][j] = max(f[i-1][j], f[i-1][j-cost[i-1]] + "i", f[i-1][j-2*cost[i-1]] + "i" * 2, ..., f[i-1][j-k*cost[i-1]] + "i" * k)
        f[i][j-cost[i-1]] =  max(f[i-1][j-cost[i-1]],       f[i-1][j-2*cost[i-1]] + "i", ...,     f[i-1][j-k*cost[i-1]] + "i" * (k-1))
        f[i][j] = max(f[i-1][j], f[i][j-cost[i-1]] + "i")
        """
        f = [""] * (target + 1)
        for i in range(9, 0, -1):
            for j in range(target + 1):
                if (j - cost[i - 1] > 0 and f[j - cost[i - 1]]) or j - cost[i - 1] == 0:
                    tmp = f[j - cost[i - 1]] + str(i)
                    if len(f[j]) < len(tmp) or (len(f[j]) == len(tmp) and tmp > f[j]):
                        f[j] = tmp
        return f[target] if f[target] else "0"