class Solution {
    public int constrainedSubsetSum(int[] nums, int k) {
        int n = nums.length;
        int[] f = new int[n];
        LinkedList<Integer> q = new LinkedList<>();
        int res = Integer.MIN_VALUE;
        for(int i = 0; i < n; i++){
            f[i] = nums[i];
            if(q.size() > 0 && q.peekFirst() < i-k) q.pollFirst();
            if(q.size() > 0) f[i] = Math.max(f[i], f[q.peekFirst()] + nums[i]);
            while(q.size() > 0 && f[q.peekLast()] <= f[i]) q.pollLast();
            q.offerLast(i);
            res = Math.max(res, f[i]);
        }
        return res;
    }
}