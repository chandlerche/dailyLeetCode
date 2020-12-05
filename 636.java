class Solution {
    public int[] exclusiveTime(int n, List<String> logs) {
        Stack<int[]> stack = new Stack<>();
        int[] res = new int[n];
        for (String log : logs) {
            String[] split = log.split(":");
            int id = Integer.parseInt(split[0]);
            int time = Integer.parseInt(split[2]);
            if ("start".equals(split[1])) {
                stack.push(new int[]{id, time});
            } else {
                int[] pop = stack.pop();
                int interval = time - pop[1] + 1;
                res[pop[0]] += interval;
                if (!stack.isEmpty()) {
                    res[stack.peek()[0]] -= interval;
                }
            }
        }
        return res;
    }
}