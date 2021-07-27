class Solution {
    HashMap<String, HashMap<String, Double>> graph;
    public double dfs(String i, String j, HashSet visit){
        if (graph.get(i).containsKey(j)) return graph.get(i).get(j);
        visit.add(i);
        for (String child : graph.get(i).keySet()){
            if (!visit.contains(child)){
                visit.add(child);
                double rev = dfs(child, j, visit);
                if (rev != -1){
                    rev *= graph.get(i).get(child);
                    return rev;
                }
            }
        }
        return -1.0;
    }
    public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {
        graph = new HashMap<>();
        int size = values.length;
        for (int i = 0; i < size; i++){
            graph.put(equations.get(i).get(0), new HashMap<>());
            graph.put(equations.get(i).get(1), new HashMap<>());
        }
        for (int i = 0; i < size; i++){
            graph.get(equations.get(i).get(0)).put(equations.get(i).get(1), values[i]);
            graph.get(equations.get(i).get(1)).put(equations.get(i).get(0), 1/values[i]); 
        }
        double[] ans = new double[queries.size()];
        for (int k = 0; k < queries.size(); k++){
            String i = queries.get(k).get(0);
            String j = queries.get(k).get(1);
            if (!graph.containsKey(i) || !graph.containsKey(j)){
                ans[k] = -1.0;
            }
            else{
                if (i.equals(j)) ans[k] = 1.0;
                else{
                    ans[k] = dfs(i, j, new HashSet<>());
                }
            }
        }

        return ans;
    }
}