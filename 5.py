class Solution(object):
    # 要记住把res先创好，且设为全局变量
    res = ''
    def longestPalindrome(self, s):
        if s is None: return ''
        for i in range(len(s)):
            self.helper(s , i , i)
            self.helper(s , i , i+1)
        return self.res

    def helper(self , s , left , right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # 当两个字母不相等时，只需截取其后面的字符串即可，左边+1处理，右边因为本来就是左闭右开，所以保持不动即可
        cur = s[left + 1: right]
        if len(cur) > len(self.res):
            self.res = cur