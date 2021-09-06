class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        res=0
        row,column=len(grid),len(grid[0])
        moveset=[(0,1),(1,0),(-1,0),(0,-1)]
        def dfs(grid,i,j):
            if i < 0 or j<0 or i>=row or j>=column or grid[i][j] == 0:
                return 0            
            s=1
            grid[i][j]=0
            for cood in moveset:
                s+=dfs(grid,i+cood[0],j+cood[1])
            return s

        for i in range(row):
            for j in range(column):
                if grid[i][j]==1:
                    res=max(res,dfs(grid,i,j))            
        return res