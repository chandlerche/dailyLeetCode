class Solution {

    private final int MAXN = 30;

    // dp[i][j][k][0] 表示i个运动员第一个最佳运动员在位置j第二个最佳运动员在位置k时它们相遇的最早回合数
    // dp[i][j][k][1] 表示i个运动员第一个最佳运动员在位置j第二个最佳运动员在位置k时它们相遇的最晚回合数
    // 0 min 1 max
    private int[][][][] dp = new int[MAXN][MAXN][MAXN][2];

    public int[] earliestAndLatest(int n, int fir, int sec) {
        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= n; j++) {
                for (int k = 0; k <= n; k++) {
                    dp[i][j][k][0] = dp[i][j][k][1] = -1;
                }
            }
        }
        dfs(n, fir, sec, 1);
        return new int[]{dp[n][fir][sec][0], dp[n][fir][sec][1]};
    }

    private void dfs(int n, int a, int b, int r) {
        if (dp[n][a][b][0] != -1) {
            return;
        }
        if (a == n - b + 1) {
            dp[n][a][b][0] = dp[n][a][b][1] = r;
            return;
        }

        // lvl : 都在a之前对打的情况
        // lvm : 一个在a之前一个在ab之间对打的情况
        // lvr : 一个在a之前一个在r之后对打的情况
        // mvm : 都在ab之间对打的情况
        // mvr : 一个在ab之间一个在r之后对打的情况
        int m = (n + 1) / 2;
        int lvl = 0, lvm = 0, lvr = 0;
        int mvm = 0, mvr = 0;
        for (int i = 1; i <= n; i++) {
            int rival = n - i + 1;
            if (i == a || i == b) continue;
            if (rival == a || rival == b) continue;
            if (n % 2 == 1 && i == m) continue;
            if (i < a && rival < a) lvl++;
            if (i < a && rival > a && rival < b) lvm++;
            if (i < a && rival > b) lvr++;
            if (i > a && i < b && rival > a && rival < b) mvm++;
            if (i > a && i < b && rival > b) mvr++;
        }

        lvl /= 2;
        mvm /= 2;
        int np = (n % 2 == 1 && m < a) ? 1 : 0;
        int nm = (n % 2 == 1 && m > a && m < b) ? 1 : 0;
        for (int i = 0; i <= lvm; i++) {
            for (int j = 0; j <= lvr; j++) {
                for (int k = 0; k <= mvr; k++) {
                    int prev = lvl + i + j + np;
                    int mid = mvm + k + (lvm - i) + nm;
                    int nn = (n + 1) / 2, na = prev + 1, nb = prev + 1 + mid + 1;
                    dfs(nn, na, nb, r + 1);
                    if (dp[n][a][b][0] == -1 || dp[nn][na][nb][0] < dp[n][a][b][0])
                        dp[n][a][b][0] = dp[nn][na][nb][0];
                    if (dp[n][a][b][1] == -1 || dp[nn][na][nb][1] > dp[n][a][b][1])
                        dp[n][a][b][1] = dp[nn][na][nb][1];
                }
            }
        }
    }
}