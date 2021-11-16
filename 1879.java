class Solution {

    private int[] cache;
    private int n;
    private int ans = Integer.MAX_VALUE;

    private void dfs(int[] nums1,int[] nums2,int index,int mask,int result){
        if(n == index){
            ans = Math.min(ans,result);
            return;
        }
        if(cache[mask] <= result){
            return;
        }
        cache[mask] = result;
        for(int i = 0;i < n;i++){
            if((mask >> i & 1) == 0){
                dfs(nums1,nums2,index + 1,mask | (1 << i),result + (nums1[index] ^ nums2[i]));
            }
        }
    }

    public int minimumXORSum(int[] nums1, int[] nums2) {
        n = nums1.length;
        cache = new int[1 << n];
        Arrays.fill(cache,Integer.MAX_VALUE);
        dfs(nums1,nums2,0,0,0);
        return ans;
    }
}