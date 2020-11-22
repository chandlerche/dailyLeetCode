public class Solution {
    public int maxDotProduct(int[] nums1, int[] nums2) {
        int len1 = nums1.length;
        int len2 = nums2.length;
        int dp[][] = new int[len1 + 1][len2 + 1];
        int max = Integer.MIN_VALUE;
        for (int i = 1; i <= len1; i++) {
            for (int j = 1; j <= len2; j++) {
                max = Math.max(max, dp[i - 1][j - 1] + nums1[i - 1] * nums2[j - 1]);
                dp[i][j] = Math.max(Math.max(dp[i][j - 1], dp[i - 1][j]), dp[i - 1][j - 1] + nums1[i - 1] * nums2[j - 1]);
            }
        }
        return max;
    }
}