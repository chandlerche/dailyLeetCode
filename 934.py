class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        m = len(A)
        n = len(A[0])
        distances = [[1,0],[-1,0],[0,1],[0,-1]]
        used = [[False]*n for _ in range(m)]
        def dfs(i,j):
            used[i][j]=True
            for d in distances:
                newi = i+d[0]
                newj = j+d[1]
                if 0<=newi<m and 0<=newj<n and A[newi][newj]==1 and used[newi][newj]==False:
                    dfs(newi,newj)
        def bfs():
            res = 0
            q = []
            for i in range(m):
                for j in range(n):
                    if used[i][j]:
                        q.append((i,j))
            while q:
                tmp = []
                for coord in q:
                    for d in range(4):
                        newx = coord[0]+distances[d][0]
                        newy = coord[1]+distances[d][1]
                        if 0<=newx<m and 0<=newy<n :
                            if A[newx][newy]==1 and used[newx][newy]==False:
                                used[newx][newy] = True
                                return res
                            if used[newx][newy]==False:
                                used[newx][newy]= True
                                tmp.append((newx,newy))
                q = tmp
                res+=1
        indx,indy=-1,-1
        for i in range(m):
            if indx!=-1:break
            for j in range(n):
                if A[i][j]==1 and used[i][j]==False:
                    indx,indy = i,j
                    break
        dfs(indx,indy)
        return bfs()