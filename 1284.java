class Solution {
    int m, n;
    int ans = 10;
    int[][] dir = new int[][]{{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    public int minFlips(int[][] mat) {
        m = mat.length;
        n = mat[0].length;
        int diff = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (mat[i][j] == 1) {
                    diff++;
                }
            }
        }
        dfs(mat, 0, 0, diff, 0);
        if (ans == 10) {
            return -1;
        } else {
            return ans;
        }
    }
    public void dfs(int[][] mat, int i, int j, int diff, int cnt) {
        if (j == n) {
            j = 0;
            i = i + 1;
            dfs(mat, i, j, diff, cnt);
            return;
        }
        if (diff == 0) {
            ans = Math.min(ans, cnt);
            return;
        }
        if (i == m) {
            return;
        }
        int newDiff = help(mat, i, j);
        dfs(mat, i, j + 1, diff + newDiff, cnt + 1);
        help(mat, i, j);
        dfs(mat, i, j + 1, diff, cnt);
    }
    
    public int help(int[][] mat, int i, int j) {
        int cnt = 0;
        if (mat[i][j] == 0) {
            cnt++;
        } else {
            cnt--;
        }
        mat[i][j] = 1 - mat[i][j];
        for (int[] d : dir) {
            int nx = i + d[0], ny = j + d[1];
            if (nx < 0 || nx >= m || ny < 0 || ny >= n) {
                continue;
            }
            if (mat[nx][ny] == 0) {
                cnt++;
            } else {
                cnt--;
            }
            mat[nx][ny] = 1 - mat[nx][ny];
        }
        return cnt;
    }
}