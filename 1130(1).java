class Solution {
    public int mctFromLeafValues(int[] arr) {
        //1. 如果栈顶元素比当前元素小，弹出栈顶元素，
        //   栈顶元素与当前元素和栈顶下一个元素中得最小值组合
        //2. 如果栈顶元素比当前元素大，入栈
        Stack<Integer> stack = new Stack<>();
        stack.push(Integer.MAX_VALUE);//哨兵
        int ans = 0;
        for (int i = 0; i < arr.length; i++){
            while (stack.peek() < arr[i])
                ans += stack.pop()*Math.min(arr[i],stack.peek());
            stack.push(arr[i]);
        }

        while(stack.size() > 2)
            ans += stack.pop()*stack.peek();
        
        return ans;
    }
}