class Solution {
    public int longestWPI(int[] hours) {
        int res = 0, sum = 0;
        Deque<Integer> stack = new ArrayDeque<>();
        stack.add(0);
        int[] cnt = new int[hours.length + 1];
        for(int i = 0; i < hours.length; i++){
            sum += hours[i] > 8 ? 1 : -1;
            cnt[i + 1] = sum;
            if(stack.isEmpty() || sum < cnt[stack.peek()]) {
                stack.push(i + 1);
            }
        }
        for(int i = hours.length; i > res ; i--){
            while(!stack.isEmpty() && cnt[stack.peek()] < cnt[i]){
                res = Math.max(res, i - stack.peek());
                stack.pop();
            }
        }
        return res;
    }
}