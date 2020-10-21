class Solution {
    public int coinChange(int[] coins, int amount) {
        int nums = coins.length;
        int[][] dp = new int[nums + 1][amount + 1];
        for (int i = 0; i < dp.length; i++) {
            Arrays.fill(dp[i], amount+1);
            if (i > 0) dp[i][0] = 0;
        }
        for (int i = 1; i <= nums; i++) {
            for (int j = 1; j <= amount; j++) {
                if (j < coins[i - 1]) dp[i][j] = dp[i - 1][j];
                else dp[i][j] = Math.min(dp[i - 1][j], dp[i][j - coins[i - 1]] + 1);
            }
        }
        return dp[nums][amount]== amount+1? -1:dp[nums][amount];
    }
}