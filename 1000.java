class Solution {
    public int mergeStones(int[] stones, int K) {
        int n = stones.length;
        if ((n-1) % (K-1) != 0) return -1;
        int[][] dp = new int[n][n];
        int[] sum = new int[n+1];
        for (int i = 0 ; i < n ; i++){
            dp[i][i] = stones[i];
            sum[i+1] += sum[i]+stones[i];
        }
        for (int j = 1 ; j < n ; j++){
            for (int i = j-1 ; i >= 0 ; i--){
                dp[i][j] = dp[i][i]+dp[i+1][j];
                for (int cut = i+K-1 ; cut < j ; cut += K-1){
                    dp[i][j] = Math.min(dp[i][j], dp[i][cut]+dp[cut+1][j]);
                }
                if ((j-i) % (K-1) == 0) {
                    dp[i][j] += sum[j+1]-sum[i];
                }
            }
        }
        return dp[0][n-1]-sum[n];   
    }
}