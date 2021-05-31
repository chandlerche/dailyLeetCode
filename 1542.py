class Solution:
    def longestAwesome(self, s: str) -> int:
        string = "0" * 10 # 表示0 - 9 出现的次数
        res = 1
        dict1 = {0: -1}
        for i in range(len(s)):
            index = int(s[i])
            if string[index] == "0":
                string = string[:index] + "1" + string[index + 1:]
            else:
                string = string[:index] + "0" + string[index + 1:]
            # 能够组成回文串的是0000000000， 0000000010， 0000000100,... 并将其转化成十进制
            for j in range(10):
                # 当前值与上述值对应位相减，如果结果在dict1中说明对应的索引之间的子串满足条件，不在说明没有满足条件的子串
                helper = (2 ** j) ^ int(string, 2)
                if helper in dict1:
                    res = max(res, i - dict1[helper])
            if int(string, 2) in dict1:
                res = max(res, i - dict1[int(string, 2)])
            else:
                dict1[int(string, 2)] = i
        return res