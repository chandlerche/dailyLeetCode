class Solution {
    public int maxWidthRamp(int[] A) {
        int len=A.length;
        Stack<Integer> stack=new Stack<>();
        stack.push(0);
        for(int i=1;i<len;i++){
            if(A[stack.peek()]>A[i]){
                stack.push(i);
            }
        }
        int max=0;
        for(int i=len-1;i>=0;i--){
            while(!stack.isEmpty()&&A[stack.peek()]<=A[i]){
                max=Math.max(max,i-stack.pop());
            }
        }
        return max;
    }
}