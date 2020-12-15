class Solution {
    public int numSubarraysWithSum(int[] A, int S) {
        int res = 0;
        int[] map = new int[A.length+1];
        map[0] = 1;
        int sum = 0;
        for(int e:A){
            sum+=e;
            if(sum>=S)
                res+=map[sum-S];
            map[sum]++;
        }
        return res;
    }
}