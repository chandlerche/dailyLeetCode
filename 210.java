class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {

        List<Integer>[] lists = new ArrayList[numCourses];
        int[] points = new int[numCourses];
        for(int[] p : prerequisites){
            points[p[0]]++;
            if(lists[p[1]] == null){
                lists[p[1]] = new ArrayList<>();
            }
            lists[p[1]].add(p[0]);
        }

        Queue<Integer> queue = new LinkedList<>();

        for(int i = 0; i < numCourses; i++){
            if(points[i] == 0){
                queue.add(i);
            }
        }

        int[] res = new int[numCourses];
        int idx = 0;

        while(!queue.isEmpty()){
            int size = queue.size();
            while(size-- > 0){
                int p = queue.poll();
                res[idx++] = p;
                List<Integer> list = lists[p];
                if(list == null){
                    continue;
                }
                for(int val : list){
                    points[val]--;
                    if(points[val] == 0){
                        queue.add(val);
                    }
                }
            }
        }
        return idx == numCourses ? res : new int[0];
    }
}