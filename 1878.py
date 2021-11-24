class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        
        def helper(l_x, l_y, r_x, r_y):
            ans = 0
            length = r_y - l_y
            for i in range(length//2+1):
                ans += grid[l_x - i][l_y + i]
                ans += grid[l_x + i][l_y + i]
                ans += grid[r_x - i][r_y - i]
                ans += grid[r_x + i][r_y - i]
            ans -= grid[l_x][l_y] + grid[r_x][r_y] + grid[l_x - i][l_y + i] + grid[l_x + i][l_y+ i]
            return ans

        ans = set()
        for i in range(m):
            for j in range(n):
                ans.add(grid[i][j])
                for other in range(j+2, n, 2): # 只能是相差奇数
                    center = (j + other) // 2
                    upper = i - (other - j) // 2
                    below = i + (other - j) // 2
                    if upper < 0 or below >= m: break
                    score = helper(i, j, i, other)
                    ans.add(score)
                
        return sorted(ans, reverse=True)[:3] # TODO 可以优化这个