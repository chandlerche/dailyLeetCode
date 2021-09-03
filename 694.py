def numDistinctIslands(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        shapes = set()
        directions = [(-1,0),(0,1),(1,0),(0,-1)]
        visited=set()
        def dfs(x, y, pos, island_direction):
            for dx, dy in directions:
                nx,ny=x+dx,y+dy
                if 0<=nx <row and 0<= ny <col and grid[nx][ny] and (nx,ny) not in visited:
                    temp_direction = (pos[0]+dx, pos[1]+dy)
                    visited.add((nx,ny))
                    island_direction.append(temp_direction)
                    dfs(nx, ny, temp_direction,island_direction)
            return tuple(island_direction)
        
        for x in range(row):
            for y in range(col):
                if grid[x][y] and (x,y) not in visited:
                    visited.add((x,y))
                    shapes.add(dfs(x,y,(0,0),[(0,0)]))
        return len(shapes)