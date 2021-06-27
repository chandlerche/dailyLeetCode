class Solution {
    public int maxSum(int[] nums1, int[] nums2) {
        // 找到相同的值，分别计算每一个间隔的最大值
        int l1 = 0, l2 = 0;
        // 关键是要设置为 long 型
        long sum1 = 0, sum2 = 0;
        long ans = 0;
        int mod =1000000007;
        while (l1 < nums1.length && l2 < nums2.length) {
            if (nums1[l1] < nums2[l2]) {
                sum1 += nums1[l1++];
            } else if (nums1[l1] > nums2[l2]) {
                sum2 += nums2[l2++];
            } else {
                // 相等，交点
                ans += (Math.max(sum1, sum2) + nums1[l1]);
                sum1 = 0;
                sum2 = 0;
                l1++;
                l2++;
            }
        }
        while (l1 < nums1.length) sum1 += nums1[l1++];
        while (l2 < nums2.length) sum2 += nums2[l2++];
        ans += Math.max(sum1, sum2);
        ans %= mod;
        return (int) ans;
    }
}