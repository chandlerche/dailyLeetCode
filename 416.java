class Solution {
    public boolean canPartition(int[] nums) {
        
        int sum = 0;
        for (int num : nums) {
            sum += num;
        }
        
        if (sum % 2 != 0) {
            return false;
        }
        
        sum /= 2;
        
        boolean[] w = new boolean[sum + 1];
        w[0] = true;
        
        
        for (int num : nums) {
            for (int i = sum; i >= num; i--) {
                w[i] = w[i] || w[i - num]; 
            }
        }
        return w[sum];
    }
}