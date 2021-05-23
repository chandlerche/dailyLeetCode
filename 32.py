class Solution(object):
    def longestValidParentheses(self, s):
        length = len(s)
        if length == 0:
            return 0
        dp = [0] * length
        for i in range(1,length):
        		#当遇到右括号时，尝试向前匹配左括号
            if s[i] == ')':
                pre = i - dp[i-1] -1;
                #如果是左括号，则更新匹配长度
                if pre>=0 and s[pre] == '(':
                    dp[i] = dp[i-1] + 2
                    #处理独立的括号对的情形 类似()()、()(())
                    if pre>0:
                        dp[i] += dp[pre-1]
        return max(dp);