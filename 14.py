class Solution:
    def longestCommonPrefix(self, strs):
        if strs == None or len(strs) == 0:
            return ''
        for i in range(len(strs[0])):
            c = strs[0][i]
            for j in range(1 , len(strs)):
                '''
                i 0-2: 0
                c: d
                j 1-2: 1
                d != r
                这里其实利用前缀的特性，比较第一个字母，只要不等，那就“切一个空值”给他，以这种方式判死刑
                '''
                if i == len(strs[j]) or strs[j][i] != c:
                    return strs[0][:i]
        return strs[0] if strs else ''