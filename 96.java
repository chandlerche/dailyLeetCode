class Solution {
    public int numTrees(int n) {

        if(n <= 2) return n;

        int[] dp = new int[n + 1];
        dp[0] = 1;
        dp[1] = 1;
        dp[2] = 2;

        // 外层的循环为了填充这个dp数组
        for(int i = 3; i <=n ; i++ ){

            // 内层循环用来遍历各个元素用作根的情况
            for(int j = 1; j <= i; j++){
                dp[i] += dp[j - 1] * dp[i - j];
            }
        }
        return dp[n];
    }
}