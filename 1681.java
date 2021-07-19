class Solution {
    int n;
    Integer memo[] = new Integer[1 << 16];

    public int minimumIncompatibility(int[] nums, int k) {
        n = nums.length / k;
        int res = dfs(nums, 0, 0, 0, n, k, 1000, 0);
        return res == 1000 ? -1 : res;
    }

    private int dfs(int nums[], int state, int seen, int pos, int N, int K, int min, int max) {
        if (N == 0) {
            return max - min + ((memo[state] != null) ? memo[state] : (memo[state] = (((K == 1) ? 0 : dfs(nums, state, 0, 0, n, K - 1, 1000, 0)))));
        }
        int res = 1000;
        for (int i = pos; i < nums.length; i++) {
            if (N == n && nums.length - i < n * K) break;
            if ((state & (1 << i)) != 0 || (seen & (1 << nums[i])) != 0) continue;
            res = Math.min(dfs(nums, state | (1 << i), seen | (1 << nums[i]), i + 1, N - 1, K, Math.min(min, nums[i]), Math.max(max, nums[i])), res);
        }
        return res;
    }
}