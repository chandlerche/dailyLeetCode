class Solution {
    int max=0;
    public int tallestBillboard(int[] rods) {
        if(rods==null||rods.length<2)
            return 0;
        Arrays.sort(rods);
        int remain=0;
        for(int n:rods)
            remain+=n;
        dfs(rods,rods[rods.length-1],0,rods.length-2,remain-rods[rods.length-1]);
        dfs(rods,0,0,rods.length-2,remain-rods[rods.length-1]);
        return max;
    }
    public void dfs(int[] rods,int left,int right,int index,int remain){
        if(index<0){
            if(left==right&&left>max)
                max=left;
            return ;
        } 
        if(left+right+remain<=max*2||Math.abs(left-right)>remain)
            return ;
        dfs(rods,left+rods[index],right,index-1,remain-rods[index]);
        dfs(rods,left,right+rods[index],index-1,remain-rods[index]);
        dfs(rods,left,right,index-1,remain-rods[index]);
    }
}