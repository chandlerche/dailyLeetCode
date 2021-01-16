class Solution {
    public int openLock(String[] deadends, String target) {
        HashSet<String> dead = new HashSet<>(Arrays.asList(deadends));
        Set<String> visited = new HashSet<>();
        String start="0000";
        Queue<String> queue = new LinkedList<>();
        queue.offer(start);
        int step=0;
        if(dead.contains(target)||dead.contains("0000")) return -1;
        while(!queue.isEmpty()){
            int len = queue.size();
            for(int i = 0; i < len; i++) {
                String cur=queue.poll();
                if(target.equals(cur)){
                    return step;
                }
                List<String> nexts= getNexts(cur);
                for(String s:nexts){
                    if(!dead.contains(s)&&!visited.contains(s)){
                        visited.add(s);
                        queue.offer(s);
                    }
                }
            }
            step++;
        }
        return -1;
    }
    public List<String> getNexts(String cur){
        List<String> list = new ArrayList<>();
        
        for(int i=0;i<4;i++){
            StringBuilder curSb= new StringBuilder(cur);
            curSb.setCharAt(i,cur.charAt(i)=='0'?'9':(char)(cur.charAt(i)-1));
            list.add(curSb.toString());
            curSb.setCharAt(i,(char)cur.charAt(i)=='9'?'0':(char)(cur.charAt(i)+1));
            list.add(curSb.toString());
               
        }
        return list;
        
    }
}