class Solution:
  def shortestSuperstring(self, A: List[str]) -> str:
    n = len(A)
    m = 1 << n
    dp   = [['' for i in range(n)] for j in range(m)]
    cost = [['' for i in range(n)] for j in range(n)]
        
    for i in range(n):
      for j in range(n):
        cost[i][j] = A[j]
        for k in range(len(A[j]), 0, -1):
          if A[i].endswith(A[j][:k]):
            cost[i][j] = A[j][k:]
            break
        
    for i in range(n):
      dp[1<<i][i] = A[i]
        
    for s in range(m):
      for i in range(n):
        if ((s >> i) & 0x1) == 0x1: continue
        up = s ^ (1 << i)
        for j in range(n):
          if ((s >> j) & 0x1) == 0x0: continue
          tmpStr = dp[s][j] + cost[j][i]
          if len(dp[up][i]) == 0 or len(dp[up][i]) > len(tmpStr):
            dp[up][i] = tmpStr
            
    return min(dp[-1], key=len)