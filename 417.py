class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        res = []
        if not matrix or len(matrix) == 0:
            return res

        directions = [[0,1], [0,-1], [1, 0], [-1,0]]

        m = len(matrix)
        n = len(matrix[0])

        canP = [[0] * n for _ in range(m)]
        canA = [[0] * n for _ in range(m)]

        def dfs(row, col, ocean):
            if not ocean[row][col]:
                ocean[row][col] = 1
                for direction in directions:
                    x = row + direction[0]
                    y = col + direction[1]
                    if x >= m or x < 0  or y >= n or y < 0 or matrix[x][y] < matrix[row][col]:
                        continue
                    dfs(x, y, ocean)

        for i in range(m):
            dfs(i, 0, canP)
            dfs(i, n-1, canA)

        for j in range(n):
            dfs(0, j, canP)
            dfs(m-1, j, canA)

        for i in range(m):
            for j in range(n):
                if canA[i][j] and canP[i][j]:
                    res.append([i,j])
        return res