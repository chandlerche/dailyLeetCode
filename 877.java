class Solution {
    public boolean stoneGame(int[] piles) {
        int n=piles.length;
        int [][]dps=new int[n][n];
        for(int i=0;i<n;i++)
            dps[i][i]=piles[i];
        for(int d=1;d<n;d++){
            for(int j=0;j<n-d;j++){
                dps[j][d+j]=Math.max(piles[j]-dps[j+1][d+j],piles[d+j]-dps[j][d+j-1]);
            }
        }
        return dps[0][n-1]>0;
    }
}