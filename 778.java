class Solution {
    private int[][] DIR = {{-1, 0}, {1, 0}, {0, 1}, {0, -1}};
    public int swimInWater(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        boolean[][] visited = new boolean[m][n];
        int res = 0;
        PriorityQueue<int[]> pqueue = new PriorityQueue<>((a, b) -> (grid[a[0]][a[1]] - grid[b[0]][b[1]]));
        pqueue.offer(new int[]{0, 0});
        visited[0][0] = true;
        while (!pqueue.isEmpty()) {
            int[] pos = pqueue.poll();
            res = Math.max(res, grid[pos[0]][pos[1]]);
            if (pos[0] == m - 1 && pos[1] == n - 1) {
                return res;
            }
            for (int[] dir : DIR) {
                int x = pos[0] + dir[0];
                int y = pos[1] + dir[1];
                if (x < 0 || y < 0 || x > m - 1 || y > n - 1 || visited[x][y]) {
                    continue;
                }
                pqueue.offer(new int[]{x, y});
                visited[x][y] = true;
            }
        }
        return -1;
    }
}