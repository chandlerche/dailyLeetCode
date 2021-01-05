class Solution {
    public boolean sequenceReconstruction(int[] org, List<List<Integer>> seqs) {
        //input check
        //
        int n = org.length;
        HashSet<Integer> set = new HashSet<>();
        for(List<Integer> list : seqs){
            for(Integer i : list){
                set.add(i);
            }
        }
        if(set.size()!=n)
            return false;
        HashMap<Integer, List<Integer>> map = new HashMap<>();
        for(List<Integer> list : seqs){
            for(int i=0; i<list.size()-1; i++){
                List<Integer> al = map.getOrDefault(list.get(i), new ArrayList<Integer>());
                al.add(list.get(i+1));
                map.put(list.get(i), al);
            }
        }
        int[] degree = new int[n+1];
        for(Integer key : map.keySet()){
            for(Integer i : map.get(key)){
                degree[i]++;
            }
        }
        int zeroInDegreeCount = 0;
        int index = 0;
        for(int i=1; i<=n; i++)
            if(degree[i]==0){
                zeroInDegreeCount++;
                index = i;
            }

        if(zeroInDegreeCount!=1)
            return false;
        Queue<Integer> queue = new LinkedList<>();
        queue.add(index);
        index=0;
        while(!queue.isEmpty()){
            int cur = queue.poll();
            if(cur!=org[index])
                return false;
            index++;
            if(map.containsKey(cur)){
                for(Integer a : map.get(cur)){
                    degree[a]--;
                    if(degree[a]==0){
                        queue.add(a);
                        if(queue.size()>1)
                            return false;
                    }
                }
            }
        }
        return index==n;
    }
}