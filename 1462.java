class Solution {
    public List<Boolean> checkIfPrerequisite(int n, int[][] prerequisites, int[][] queries) {
        boolean[][] G = new boolean[n][n];
        for(int i = 0; i < prerequisites.length; i++){
            G[prerequisites[i][0]][prerequisites[i][1]] = true;
        }

        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                for(int k = 0; k < n; k++){
                    if(G[j][i] && G[i][k])
                    G[j][k] = true;
                }
            }
        }

        List<Boolean> res = new ArrayList<>();
        for(int i = 0; i < queries.length; i++){
            res.add(G[queries[i][0]][queries[i][1]]);
        }
        return res;
    }
}