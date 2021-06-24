class Solution {
 2     public List<Integer> minAvailableDuration(int[][] slots1, int[][] slots2, int duration) {
 3         PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparing(a -> a[0]));
 4         for (int[] s : slots1) {
 5             if (s[1] - s[0] >= duration) {
 6                 pq.offer(s);
 7             }
 8         }
 9         for (int[] s : slots2) {
10             if (s[1] - s[0] >= duration) {
11                 pq.offer(s);
12             }
13         }
14         while (pq.size() > 1) {
15             if (pq.poll()[1] >= pq.peek()[0] + duration) {
16                 return Arrays.asList(pq.peek()[0], pq.peek()[0] + duration);
17             }
18         }
19         return Arrays.asList();
20     }
21 }