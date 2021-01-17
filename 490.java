public class Solution {
    public boolean hasPath(int[][] maze, int[] start, int[] destination) {
        if(maze.length == 0 || maze[0].length == 0) return false;
        if(start[0] == destination[0] && start[1] == destination[1]) return true;
        
        m = maze.length; n = maze[0].length;
        boolean[][] visited = new boolean[m][n];
        return dfs(maze, start, destination, visited);
    }
    int m, n;
    int[][] dirs = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    private boolean dfs(int[][] maze, int[] cur, int[] dest, boolean[][] visited) {
        // already visited
        if(visited[cur[0]][cur[1]]) return false;
        // reach destination
        if(Arrays.equals(cur, dest)) return true;
        
        visited[cur[0]][cur[1]] = true;
        for(int[] dir : dirs) {
            int nx = cur[0], ny = cur[1];
            while(notWall(nx + dir[0], ny + dir[1]) && maze[nx+dir[0]][ny+dir[1]] != 1) {
                nx += dir[0]; ny += dir[1];
            }
            if(dfs(maze, new int[] {nx, ny}, dest, visited)) return true;
        }
        return false;
    }
    
    private boolean notWall(int x, int y) {
        return x >= 0 && x < m && y >= 0 && y < n;
    }
}