class Solution {
    public int maxStudents(char[][] seats) {
        int m = seats.length;
        int n = seats[0].length;
        int[][] cache = new int[m][1 << n];
        for (int[] arr : cache) Arrays.fill(arr, -1);
        return dfs(seats, 0, 0, cache);
    }
    private int dfs(char[][] seats, int index, int preState, int[][] cache) {
        if (index >= seats.length) return 0;
        if (cache[index][preState] != -1) return cache[index][preState];
        int ans = 0;

        int all = 1 << seats[index].length;
        for (int state = 0; state < all; state++) {
            if (isOK(seats, index, state, preState)) {
                ans = Math.max(ans, Integer.bitCount(state) + dfs(seats, index + 1, state, cache));
            }
        }
        return cache[index][preState] = ans;
    }
    private boolean isOK(char[][] seats, int index, int cur, int pre) {
        if ((cur & (cur << 1)) != 0 || (cur & (pre << 1)) != 0 || (cur & (pre >> 1)) != 0) return false;
        for (int i = 0; i < seats[index].length; i++) {
            int bit = 1 << i;
            if ((cur & bit) != 0 && seats[index][i] == '#') return false;
        }
        return true;
    }
}