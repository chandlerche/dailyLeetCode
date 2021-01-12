class Solution {
    public boolean isBipartite(int[][] graph) {
        int n=graph.length;
        int[] color=new int[n];
        LinkedList<Integer> queue=new LinkedList<Integer>();
        for(int i=0;i<n;i++){
            if(color[i]==0){
                color[i]=0xf0f;
                queue.addLast(i);
                while(queue.size()>0){
                    int cur=queue.removeFirst();
                    for(int next:graph[cur]){
                        if(color[next]==0){
                            color[next]=~color[cur];
                            queue.addLast(next);
                        }else if(color[next]!=~color[cur]){
                            return false;
                        }
                    }
                }
            }
        }
        return true;
    }
}