class Solution {
    public int numberWays(List<List<Integer>> hats) {
        int n = hats.size();
        boolean[][] valid = new boolean[50][n];
        for (int i = 0; i < n; ++i)
            for (int h : hats.get(i)) {
                valid[h][i] = true;
            }
        int mod = 1000000007;
        int m = (1 << n);
        int[][] dp = new int[50][m];
        dp[0][0] = 1;
        for (int h = 1; h <= 40; ++h) {
            for (int mask = 0; mask < m; ++mask) {
                dp[h][mask] = (dp[h][mask] + dp[h - 1][mask]) % mod;
                for (int i = 0; i < n; ++i) {
                    if ((mask & (1 << i)) != 0 && valid[h][i])
                        dp[h][mask] = (dp[h][mask] + dp[h - 1][mask ^ (1 << i)]) % mod;
                }
            }
        }
        return dp[40][m - 1];
    }
}