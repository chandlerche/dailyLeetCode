class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        prt = list(range(row*col+2))
        def find(x):
            if prt[x]==x:
                return x
            return find(prt[x])
        def union(a,b):
            x,y = find(a),find(b)
            if x==y:
                return
            prt[x] = y
        mp = [[1]*col for _ in range(row)]
        cells.reverse()
        for d,(x,y) in enumerate(cells):
            i = x-1
            j = y-1
            if i==0:
                union(i*col+j,row*col)
            if i==row-1:
                union(i*col+j,row*col+1)
            mp[i][j] = 0
            for ni,nj in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if ni>=0 and nj>=0 and ni<row and nj<col and mp[ni][nj]==0:
                    union(i*col+j,ni*col+nj)
            if find(row*col)==find(row*col+1):
                return row*col-d-1
        return 0