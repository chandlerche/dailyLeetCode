class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        HashMap<Integer, HashSet<Integer>> graph = buildGraph(prerequisites);

        int[] visited = new int[numCourses];
        HashSet<Integer> memo = new HashSet<>();
        for (int i = 0; i < numCourses; i++) {
            if(!dfs(graph, visited, i, memo)) return false;
        }
        return true;
    }

    public boolean dfs(HashMap<Integer, HashSet<Integer>> graph, int[] visited, int curr, HashSet<Integer> memo) {
        if (memo.contains(curr)) return true;
        if (!graph.containsKey(curr)) return true;
        if (visited[curr] == 1) return false;
        visited[curr] = 1;
        for (Integer next : graph.get(curr)) {
            if (!dfs(graph, visited, next, memo)) return false;
        }
        memo.add(curr);
        visited[curr] = 0;
        return true;
    }

    public HashMap<Integer, HashSet<Integer>> buildGraph(int[][] prerequisites) {
        HashMap<Integer, HashSet<Integer>> graph = new HashMap<>();
        for (int i = 0; i < prerequisites.length; i++) {
            int from = prerequisites[i][0];
            int to = prerequisites[i][1];
            if (!graph.containsKey(from))
                graph.put(from, new HashSet<>());
            graph.get(from).add(to);
        }
        return graph;
    }
}