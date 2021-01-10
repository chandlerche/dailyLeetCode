class Solution {
    public int networkDelayTime(int[][] times, int N, int K) {
        K--;
        int[] dis = new int[N];
        for(int i=0; i<N; i++){
            dis[i] = Integer.MAX_VALUE;
        }
        dis[K] = 0;
        for(int i=0; i<N; i++){
            for(int[] edge: times){
                int u = edge[0]-1, v = edge[1]-1, w = edge[2];
                if(dis[u] != Integer.MAX_VALUE && dis[v] > dis[u]+w)
                    dis[v] = dis[u] + w;
            }
        }
        int res = 0;
        for(int i=0; i<N; i++){
            res = Math.max(res, dis[i]);
        }
        return res == Integer.MAX_VALUE? -1: res;        
    }
}