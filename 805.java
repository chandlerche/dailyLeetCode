class Solution {
    public boolean splitArraySameAverage(int[] A) {
        int len = A.length;
        int sum = 0;
        for(int i = 0; i < len; i++){
            sum += A[i];
        }
        Arrays.sort(A);        
        for(int i = 1; i <= len/2; i++){
            int remainder = sum * i % len;
            int target = sum * i / len;
            if(remainder == 0 && helper(A,0,i,target))
                return true;
        }
        return false;
    }
    
    public boolean helper(int[] A, int begin, int len, int target){
        if(len == 0) 
            return target == 0;
        if(target < len * A[begin])
            return false;
        for(int i = begin; i <= A.length - len; i++){
            if(i > begin && A[i] == A[i-1]) continue;
            if(helper(A, i+1, len-1, target- A[i]))
                return true;
        }
        return false;
    }
}