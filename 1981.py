class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        m = len(mat)
        res = 0
        for i in range(m):
            res += min(mat[i])
        if res > target:
            return abs(target - res)
        maxm = target + 71
        ls = set()
        dp = [[-1 for j in range(maxm)] for i in range(m)]
        for i in range(len(mat[0])):
            if mat[0][i] < maxm:
                dp[0][mat[0][i]] = abs(target - mat[0][i])
                ls.add(mat[0][i])
        for i in range(1, m):
            rs = set()
            for j in ls:
                for k in range(len(mat[i])):
                    if j + mat[i][k] < maxm:
                        dp[i][j + mat[i][k]] = abs(target - (j + mat[i][k]))
                        rs.add(j + mat[i][k])
            ls = rs
        ls = list(ls)
        res = dp[m - 1][ls[0]]
        for i in ls:
            res = min(res, dp[m - 1][i])
        return res
