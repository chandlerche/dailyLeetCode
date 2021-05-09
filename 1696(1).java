class Solution {
    public int maxResult(int[] nums, int k) {
        int res = nums[0];
        PriorityQueue<int[]> pq = new PriorityQueue<>((a,b)->b[0]-a[0]);
        pq.add(new int[]{res, 0});
        for (int i = 1; i < nums.length; i++) {
            while (i - pq.peek()[1] > k) {
                pq.poll();
            }
            res = pq.peek()[0] + nums[i];
            pq.add(new int[]{res, i});
        }
        return res;
    }
}