class Solution {
    public int findMaxValueOfEquation(int[][] A, int k) {
        Deque <int[]> deque = new LinkedList<>();
        int res = Integer.MIN_VALUE;
        for(int tmp[]: A) {
            while(!deque.isEmpty() && tmp[0] - deque.peekFirst()[0] > k) 
                deque.pollFirst();
            if(!deque.isEmpty()) 
                res = Math.max(res, tmp[0] + tmp[1] + deque.peekFirst()[1] - deque.peekFirst()[0]);
            while(!deque.isEmpty() && deque.peekLast()[1] - deque.peekLast()[0] <= tmp[1] - tmp[0]) 
                deque.pollLast();
            deque.offerLast(tmp);
        }
        return res;
    }
}