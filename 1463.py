class Solution:
    # DP做法
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dirs = [-1, 0, 1]
        dp = [[[float("-inf")]*cols for _ in range(cols)] for _ in range(rows)]
        dp[0][0][-1] = grid[0][0] + grid[0][-1]
        for i in range(1, rows):
            for l in range(cols):
                for r in range(cols):
                    for dir1 in dirs:
                        for dir2 in dirs:
                            ll, rr = l+dir1, r+dir2
                            if ll==rr or not (0<=ll<cols) or not (0<=rr<cols):
                                continue
                            gain = dp[i-1][l][r] + grid[i][ll] + grid[i][rr]
                            dp[i][ll][rr] = max(dp[i][ll][rr], gain)
        return max([max(i) for i in dp[-1]])