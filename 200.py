class Solution:
    m , n = 0 , 0 # 似乎这才是m和n要加self的原因，全局变量
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        self.m = len(grid)
        if self.m == 0: return 0
        self.n = len(grid[0])
        # 遍历每一个元素，其实这里就是表示指针一直后移
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == '1':
                    self.dfs(grid , i , j)
                    res += 1
        return res

    # dfs函数作用就是：把出现'1'的地方及其四周，所到之处一网打尽全变成'0'
    def dfs(self , grid , i , j):
        # 下面判断条件的顺序也有讲究，grid这句要最后写
        if i < 0 or j < 0 or i >= self.m or j >= self.n or grid[i][j] == '0': return
        grid[i][j] = '0'
        self.dfs(grid , i , j + 1)
        self.dfs(grid , i , j - 1)
        self.dfs(grid , i + 1 , j)
        self.dfs(grid , i - 1 , j)