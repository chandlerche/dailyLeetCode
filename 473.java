class Solution {
    public static boolean makesquare(int[] nums) {
        
        if(nums.length < 4){
            return false;
        }
        int sum = 0;
        for(int i = 0;i < nums.length;i++) {
            sum = sum+nums[i];
        }
        
        if(sum%4 != 0){
            return false;
        }
        Arrays.sort(nums);
        int[] nums1 = new int[nums.length];
        int j = 0;
        for(int i = nums.length-1;i >= 0;i--) {
            nums1[j] = nums[i];
            j++;
        }
        int[] bucket = new int[4];
       return makesquare(0,nums1,bucket,sum/4);
    }

    private static boolean makesquare(int i, int[] nums, int[] bucket ,int target) {
        
        if(i >= nums.length){
            return  bucket[0] == target && bucket[1] == target
                    && bucket[2] == target && bucket[3] == target;
        }
        for(int j = 0;j < 4;j++) {
            
            if(bucket[j] + nums[i] > target){
                continue;
            }
            bucket[j] = bucket[j]+nums[i];
            
            if(makesquare(i+1,nums,bucket,target)){
                return true;
            }
            bucket[j] = bucket[j]-nums[i];
        }
        return false;

    }
}