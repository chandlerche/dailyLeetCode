class Solution {
    public int strangePrinter(String s) {

        if(s.length() == 0) return 0;

        int n = s.length();
        int[][] f = new int[n + 1][n + 1];
        
        for(int len = 1; len <= n; len ++)
            for(int l = 0; l + len - 1 < n; l++) {
                
                int r = l + len  - 1;
                f[l][r] = f[l + 1][r] + 1;

                for(int k = l + 1; k <= r; k ++) 
                    if(s.charAt(k) == s.charAt(l))
                        f[l][r] = Math.min(f[l][r], f[l][k - 1] + f[k + 1][r]);
            }
            
        return f[0][n - 1];
    }
}