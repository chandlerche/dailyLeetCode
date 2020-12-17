class Solution {
    public int longestOnes(int[] nums, int K) {
        int max = 0;
        int ll = 0;
        int rr = 0;
        int zero = 0;
        while(rr < nums.length){
            if(nums[rr] == 0){
                zero++;
            }
            while(zero > K){
                if(nums[ll++] == 0){
                    zero--;
                }
            }
            max = Math.max(max, rr - ll + 1);
            rr++;
        }
        return max;
    }
}