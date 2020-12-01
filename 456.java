class Solution {
    public boolean find132pattern(int[] nums) {
        int n = nums.length;
        int last = Integer.MIN_VALUE;
        Stack<Integer> sta = new Stack<>();
        if(nums.length < 3)
            return false;
        for(int i=n-1; i>=0; i--){
            if(nums[i] < last)
                return true;
            while(!sta.isEmpty() && sta.peek() < nums[i]){
                last = sta.pop();
            }
            sta.push(nums[i]);
        }
        return false;
    }
}