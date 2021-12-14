import java.util.ArrayDeque;
import java.util.Deque;

public class Solution {
    public int[] findMaximums(int[] nums) {
        int n = nums.length;
        int[] left = new int[n], right = new int[n];
        Deque<Integer> stk = new ArrayDeque<>();
        for (int i = 0; i < n; i++) {
            while (!stk.isEmpty() && nums[stk.peek()] >= nums[i]) {
                int top = stk.pop();
                left[top] = stk.isEmpty() ? -1 : stk.peek();
                right[top] = i;
            }
            
            stk.push(i);
        }
        
        while (!stk.isEmpty()) {
            int top = stk.pop();
            left[top] = stk.isEmpty() ? -1 : stk.peek();
            right[top] = n;
        }
        
        int[] res = new int[n];
        for (int i = 0; i < n; i++) {
            int len = right[i] - left[i] - 2;
            res[len] = Math.max(res[len], nums[i]);
        }
        for (int i = n - 2; i >= 0; i--) {
            res[i] = Math.max(res[i], res[i + 1]);
        }
        
        return res;
    }
}