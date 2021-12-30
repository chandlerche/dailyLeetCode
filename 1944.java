class Solution {
    public int[] canSeePersonsCount(int[] heights) {
        int n = heights.length;
        Stack<Integer> stack = new Stack<>();
        int[] ans = new int[n];
        for (int i = n - 1; i >= 0; i--) {
            while (!stack.isEmpty() && heights[i] > heights[stack.peek()]) {
                ans[i]++;
                stack.pop();
            }
            stack.push(i);
            if (stack.size() > 1) ans[i]++;
        }
        return ans;
    }
}