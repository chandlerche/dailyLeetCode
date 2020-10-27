class Solution {
    public boolean PredictTheWinner(int[] nums) {
        int sum = 0;
        for(int n : nums)
            sum += n;
        int len = nums.length;
        int[][] dp = new int[len][len];
        for(int i = 0; i < len; i++)
            dp[i][i] = nums[i];
        for(int j = 1; j < len; j++)
            dp[j-1][j] = Math.max(dp[j-1][j-1], dp[j][j]);
        for(int i = 2; i < len; i++)
            for(int row = 0; i + row < len; row++)
                dp[row][row+i]  = Math.max(nums[row] + Math.min(dp[row+1][i+row-1], dp[row+2][i+row]),
                        nums[i+row] + Math.min(dp[row][i+row-2], dp[row+1][i+row-1]));
        return dp[0][len-1] >= (sum - dp[0][len-1]);
    }
}