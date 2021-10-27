class Solution:
    def distinctSubseqII(self, S: str) -> int:
        if not S:
            return 0
        n =len(S)
        mod = 10**9+7
        dp = [0]*(n)
        dp[0]=1
        pos = dict()
        pos[S[0]] = 0 # 字典保存索引
        for i in range(1,n):
            if S[i] not in pos: # 如果S[i]是新的字母
                dp[i] = (2*dp[i-1]+1)%mod
            else: # S[i]是已存在的字母的话，则 *S[i]和*S[pos[S[i]]]是重复的  dp[i] = (2*dp[i-1]-dp[pos[S[i]]-1])
                dp[i] = (2*dp[i-1]-dp[pos[S[i]]-1])%mod
            pos[S[i]] = i
        return dp[-1]