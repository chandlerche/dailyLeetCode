public class Remove_Interval {

    public static void main(String[] args) {
        Remove_Interval out = new Remove_Interval();
        Solution s = out.new Solution();

        System.out.println(s.removeInterval(new int[][]{ {0,2}, {3,4}, {5,7}}, new int[]{1,6})); // [[0,1],[6,7]]
    }

    // to clarify: overlap in between intervals ? if so then more complexed
    class Solution {
        public List<List<Integer>> removeInterval(int[][] intervals, int[] toBeRemoved) {

            List<List<Integer>> res = new ArrayList<>();

            if (intervals == null || intervals.length == 0) {
                return res;
            }

            for (int[] i : intervals) {
                // no overlap
                if (i[1] <= toBeRemoved[0] || i[0] >= toBeRemoved[1]) {
                    res.add(Arrays.asList(i[0], i[1]));
                }
                // i[1] > toBeRemoved[0] && i[0] < toBeRemoved[1]
                else {
                    // left end no overlap
                    if (i[0] < toBeRemoved[0]) {
                        res.add(Arrays.asList(i[0], toBeRemoved[0]));
                    }
                    // right end no overlap
                    if (i[1] > toBeRemoved[1]) {
                        res.add(Arrays.asList(toBeRemoved[1], i[1]));
                    }

                    // i inside of toBeRemoved, then remove. ie no add to result list
                }
            }
            return res;
        }
    }
}