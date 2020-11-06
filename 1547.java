class Solution {
    public int minCost(int n, int[] cuts) {
        Arrays.sort(cuts);
        int m = cuts.length;
        int[][] dp = new int[m+1][m+1];
        for (int i = 0; i < m; i++)
            Arrays.fill(dp[i], Integer.MAX_VALUE);
        for (int i = 0; i < m; i++)
            dp[i][i] = 0;
        for(int i = m - 1; i >= 0; i--) {
            for(int j = i + 1; j < m + 1; j++) {
                for(int k = i; k < j; k++) {
                    int cost = (j == m ? n : cuts[j]) - (i == 0 ? 0 : cuts[i-1]);
                    dp[i][j] = Math.min(dp[i][j], dp[i][k] + dp[k+1][j] + cost);
                }
            }
        }
        return dp[0][m];
    }
}