class Solution {
    public int[] mostCompetitive(int[] nums, int k) {
        if (k == nums.length) {return nums;}
        int[] ans = new int[k];
        int top = 0;
        int n = nums.length;
        for (int i=0; i<n; i++) {
            while (top>0 && nums[i]<ans[top-1] && top+n-i-1>=k) {
                ans[top---1] = 0;
            }                
            if (top < k) {
                ans[top++] = nums[i];
            }
        }
        return ans;
    }
}