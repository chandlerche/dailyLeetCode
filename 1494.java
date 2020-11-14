class Solution {
    public int minNumberOfSemesters(int n, int[][] dependencies, int k) {
        int[] pre = new int[n];
        for (int[] dependency : dependencies) {
            dependency[0]--;
            dependency[1]--;
            pre[dependency[1]] |= (1 << dependency[0]);
        }
        int all = 1 << n;
        int[] dp = new int[all];
        for (int i = 0; i < all; i++) dp[i] = n;
        dp[0] = 0;
        for (int state = 0; state < all; state++) {
            int next = 0; 
            for (int i = 0; i < n; i++) if ((state & pre[i]) == pre[i]) next |= 1 << i;
            next &= ~state;
            for (int sub = next; sub > 0; sub = (sub - 1) & next) {
                if (Integer.bitCount(sub) <= k) {
                    dp[state | sub] = Math.min(dp[state | sub], dp[state] + 1);
                }
            }
        }
        return dp[(1 << n) - 1];
    }
}