class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])
        hp = []
        visited = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                    heapq.heappush(hp, (heightMap[i][j], i, j))
                    visited[i][j] = True
        
        ans = 0
        while hp:
            h, r, c = heapq.heappop(hp)
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    if h > heightMap[nr][nc]:
                        ans += h - heightMap[nr][nc]
                    visited[nr][nc] = True
                    heapq.heappush(hp, (max(h, heightMap[nr][nc]), nr, nc))
        return ans