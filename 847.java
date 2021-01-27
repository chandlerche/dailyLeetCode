class Solution {
    public int shortestPathLength(int[][] graph) {
        int n = graph.length;
        int dest = (1 << n) - 1;
        LinkedList<int[]> queue = new LinkedList<>();
        boolean[][] visited = new boolean[n][1 << n];
        for (int i = 0; i < n; i++) {
            queue.addLast(new int[]{i, 1 << i});
            visited[i][1 << i] = true;
        }
        int res = -1;
        while (!queue.isEmpty()) {
            res++;
            int size = queue.size();
            while (size-- > 0) {
                int[] cur = queue.removeFirst();
                if (cur[1] == dest) {
                    return res;
                }
                for (int next : graph[cur[0]]) {
                    int nextState = cur[1] | (1 << next);
                    if (visited[next][nextState]) continue;
                    queue.addLast(new int[]{next, nextState});
                    visited[next][nextState] = true;
                }
            }
        }
        return res;
    }
}