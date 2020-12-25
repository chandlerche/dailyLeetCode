class Solution {
    public int subarraysWithKDistinct(int[] A, int K) {
        return subarraysWithMostK(A, K) - subarraysWithMostK(A, K - 1);
    }
    private int subarraysWithMostK(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        int count = 0;
        int res = 0;
        int left = 0;
        int right = 0;
        while (right < nums.length) {
            map.put(nums[right], map.getOrDefault(nums[right], 0) + 1);
            if (map.get(nums[right]) == 1) {
                count++;
            }
            right++;
            while (count > k) {
                map.put(nums[left], map.get(nums[left]) - 1);
                if (map.get(nums[left]) == 0){
                    count--;
                }
                left++;
            }
            res += right - left + 1;
        }
        return res;
    }
}