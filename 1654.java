class Solution {
    public int minimumJumps(int[] forbidden, int a, int b, int x) {
        HashSet<Integer> set = new HashSet<Integer>();
        for(int v:forbidden){
            set.add(v);
        }
        if(x==0) return 0;
        set.add(0);
        LinkedList<Integer> queue = new LinkedList<>();
        LinkedList<Boolean> status = new LinkedList<>();
        queue.add(0);
        status.add(true);
        int ans=0;
        while(queue.size()>0){
            ans++;
            int len=queue.size();
            for(int i=0;i<len;i++){
                int poll = queue.poll();
                boolean flag = status.poll();
                int npoll= poll+a;
                if(npoll==x) return ans;
                if(npoll<=6000&&!set.contains(npoll)) {queue.add(npoll);status.add(true);set.add(npoll);}
                if(flag) {
                    npoll= poll-b;
                    if(npoll==x) return ans;
                    if(npoll>0&&!set.contains(npoll)) {queue.add(npoll);status.add(false);}
                }
            }
        }
        return -1;
    }
}