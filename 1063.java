class Solution {
    public int validSubarrays(int[] nums) {
        int res = nums.length;
        if(nums.length <= 1) {
            return res;
        }
        Deque<Integer> stack = new ArrayDeque<>();
        stack.push(nums[0]);
        for(int i = 1; i < nums.length; i++) {
            int num = nums[i];
            while(!stack.isEmpty() && num < stack.peek()) {
                stack.pop();
            }
            res += stack.size();
            stack.push(num);
        }
        return res;
    }
}