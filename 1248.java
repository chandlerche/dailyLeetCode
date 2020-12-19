class Solution {
    public int numberOfSubarrays(int[] nums, int k) {
        int len = nums.length;
        int res = 0;
        int oddCount = 0;
        int arr[] = new int[len + 2];
        for (int i = 0; i < len; i++) {
            if ((nums[i] & 1) == 1) {
                arr[++oddCount] = i;
            }
        }
        arr[0] = -1;
        arr[oddCount + 1] = len;
        for (int i = 1; i + k < oddCount + 2; i++) {
            res += (arr[i] - arr[i - 1]) * (arr[i + k] - arr[i + k - 1]);
        }
        return res;
    }
}