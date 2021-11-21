class Solution:
    def numPermsDISequence(self, S: str) -> int:
        l=len(S)
        dp=[[0  for _ in range(l+1)] for _ in range(l+1)]
        dp[0][0]=1
        for i in range(1,l+1):
            for j in range(i+1):
                if S[i-1]=='D':
                    for k in range(j,i):
                        dp[i][j]=(dp[i][j]+dp[i-1][k])%1000000007
                else:
                    for k in range(0,j):
                        dp[i][j]=(dp[i][j]+dp[i-1][k])%1000000007
        res=0
        for i in range(l+1):
            res=(res+dp[l][i])%1000000007
        return res