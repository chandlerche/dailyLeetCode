class Solution {
    public int minSubarray(int[] nums, int p) {
        HashMap<Integer,Integer> mp = new HashMap<Integer,Integer>();
        int tar =0;//需要移出的和
        for(int i = 0;i<nums.length;i++) {
            tar = (((tar + nums[i])%p)+p)%p;
        }
        if(tar == 0)return 0;
        mp.put(0,-1);
        int ret = nums.length;
        int sum = 0;
        for(int i = 0;i<nums.length;i++) {
            sum = (((sum + nums[i])%p)+p)%p;
            int temp = ((sum-tar)%p+p)%p;
            //System.out.println("i = "+i+", temp:"+temp+",sum ="+sum);
            if(mp.containsKey(temp)){
                //System.out.println(i+","+mp.get(temp));
                int l = i-mp.get(temp);
                ret = Math.min(l,ret);
            }
            mp.put(sum,i);
        }
        if(ret == nums.length)return -1;
        return ret;
    }
}