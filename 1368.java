class Solution {
    public int minCost(int[][] grid) {
        int m, n;
        if (grid == null || (m = grid.length) < 1 || (n = grid[0].length) < 1) {
            return -1;
        }
        int[] dx = {0, 0, 0, 1, -1};
        int[] dy = {0, 1, -1, 0, 0};
        Deque<Node> queue = new LinkedList<>();
        boolean[][] visit = new boolean[m][n];
        queue.add(new Node(0,0,0));
        while (!queue.isEmpty()){
            Node node = queue.pollFirst();
            int x = node.x;
            int y = node.y;
            int cost = node.cost;
            visit[x][y] = true;

            if (x==m-1 && y==n-1){
                return cost;
            }
            for (int i=1;i<=4;i++){
                int newDx = x + dx[i];
                int newDy = y + dy[i];
                if (newDx>=0 && newDx<m && newDy>=0 && newDy<n && !visit[newDx][newDy]){
                    if (grid[x][y]==i){
                        queue.addFirst(new Node(newDx,newDy,cost));
                    }else {
                        queue.addLast(new Node(newDx,newDy,cost+1));
                    }
                }
            }
        }
        return -1;
    }

    class Node {
        int x;
        int y;
        int cost;
        Node(int x, int y, int cost) {
            this.x = x;
            this.y = y;
            this.cost = cost;
        }
    }
}