class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        if(nums==null||nums.length<2) return nums;
        LinkedList<Integer> list = new LinkedList();
        int[] result = new int[nums.length-k+1];
        for(int i=0;i<nums.length;i++){
            while(!list.isEmpty()&&nums[list.peekLast()]<=nums[i]){
                list.pollLast();
            }
            list.addLast(i);
            if(list.peek()<=i-k){
                list.poll();   
            } 
            if(i-k+1>=0){
                result[i-k+1] = nums[list.peek()];
            }
        }
        return result;
    }
}