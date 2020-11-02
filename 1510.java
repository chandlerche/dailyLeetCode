class Solution {
        public boolean winnerSquareGame(int n) {
            boolean[] state = new boolean[n + 1];
            for (int i = 1; i <= n; i++) {
                int sqrt = (int) Math.sqrt(i);
                if (sqrt * sqrt == i) {
                    state[i] = true;
                } else {
                    for (int j = 1; j * j < i; j++) {
                        if (state[i - j * j] == false) {
                            state[i] = true;
                            break;
                        }
                    }
                }
            }
            return state[n];
        }
}