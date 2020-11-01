class Solution {
    private Integer[] memo;
    public String stoneGameIII(int[] stoneValue) {
        memo = new Integer[stoneValue.length];
        int relative = stoneGameIII(stoneValue, 0);
        if(relative > 0)
            return "Alice";
        else if(relative == 0)
            return "Tie";
        return "Bob";
    }
    
    public int stoneGameIII(int[] stoneValue, int start) {
        if(start >= stoneValue.length)
            return 0;
        if(memo[start] != null) return memo[start];
        int ans = stoneValue[start] - stoneGameIII(stoneValue, start + 1);
        if(start + 1 < stoneValue.length)
            ans = Math.max(ans, stoneValue[start] + stoneValue[start+1] - stoneGameIII(stoneValue, start + 2));
        if(start + 2 < stoneValue.length)
            ans = Math.max(ans, stoneValue[start] + stoneValue[start+1] + stoneValue[start+2] - stoneGameIII(stoneValue, start + 3));
        return memo[start] = ans;
    }
}