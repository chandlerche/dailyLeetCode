class Solution {
    public int lastStoneWeightII(int[] stones) {
        int sum=0;
        for(int st:stones)
            sum+=st;
        for(int i=(sum>>1);;i--){
            if(helper(stones,0,0,i))
                return sum-2*i;
        }
    }
    
    boolean helper(int[] nums,int idx,int sum,int target){
        if(sum==target)
            return true;
        if(sum>target)
            return false;
        if(idx==nums.length)
            return false;
        return helper(nums,idx+1,sum+nums[idx],target)
            ||helper(nums,idx+1,sum,target);
    }
}