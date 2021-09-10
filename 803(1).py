class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        drop = []
        current = 0
        for hit in hits:
            grid[hit[0]][hit[1]] = grid[hit[0]][hit[1]] - 1
        for j in range(len(grid[0])):
            current = current + visit(0, j, grid)
        total = current
        for i in range(len(hits)-1, -1, -1):
            x, y = hits[i][0], hits[i][1]
            grid[x][y] = grid[x][y] + 1
            if not grid[x][y]:
                drop.append(0)
                continue
            if x!=0 and not judge(x-1, y, grid) + judge(x+1, y, grid) + \
                    judge(x, y-1, grid) + judge(x, y+1, grid):
                drop.append(0)
                continue
            current = visit(x, y, grid)
            total = total + current
            drop.append(current - 1)
        drop.reverse()
        return drop