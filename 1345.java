class Solution {
    public int minJumps(int[] arr) {
        int l = arr.length;
        if (l==1) {
            return 0;
        }
        HashMap<Integer, Set<Integer>> hashMap = new HashMap<>();
        for (int i = 0; i < arr.length; ++i) {
            hashMap.computeIfAbsent(arr[i], k -> new HashSet<>());
            hashMap.get(arr[i]).add(i);
        }

        int[] res = new int[l];
        Deque<Integer> deque = new LinkedList<>();
        deque.addLast(0);
        while (!deque.isEmpty()) {
            int g = deque.removeFirst();
            if (g == l-1) {
                return res[l-1];
            }
            addQueue(g-1, g, res, deque);

            addQueue(g+1, g, res, deque);
            if (hashMap.get(arr[g]) != null) {
                for (int e : hashMap.get(arr[g])) {
                    addQueue(e, g, res, deque);
                }
                hashMap.remove(arr[g]);
            }
        }
        return res[l-1];
    }

    private void addQueue(int i, int g, int[] res, Deque<Integer> deque) {
        if (i <= 0 || res[i] !=0) {
            return;
        }
        deque.addLast(i);
        res[i] = res[g] + 1;
    }
}