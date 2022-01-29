class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not s or not p:
            return False
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = True
        #这一步是未雨绸缪(预处理)的一步，因为本题涉及情况较多，其中一种分支情况必须现在处理，不然后面会掣肘
        #这里处理的就是“s = "aab" p = "c*a*b"”中c*的情况，直接跳过c*，然后为i + 1重新初始化
        for i in range(len(p)):
            if p[i] == '*' and dp[0][i - 1]:
                dp[0][i + 1] = True
        
        for i in range(len(s)):
            for j in range(len(p)):
                #处理第一种情况：s和p当前的字母直接全等的情况，比如aa和aa
                if p[j] == s[i]:
                    dp[i + 1][j + 1] = dp[i][j] #这里+1是无所谓的，因为有dp[0][0]了而已，也可以-1形式
                #处理第二种情况：出现'.'的情况，和第一种一样处理
                if p[j] == '.':
                    dp[i + 1][j + 1] = dp[i][j]
                #处理第三种情况，出现'*'的情况，但这里又要分两组情况考虑！
                if p[j] == '*':
                    if p[j - 1] != s[i] and p[j - 1] != '.':
                        dp[i + 1][j + 1] = dp[i + 1][j - 1] #看两位前的状况
                    else: #情况2的三种分支情况我们合起来写，有一个为True即为True
                        dp[i + 1][j + 1] = dp[i + 1][j] or dp[i][j + 1] or dp[i + 1][j - 1]
        return dp[len(s)][len(p)]