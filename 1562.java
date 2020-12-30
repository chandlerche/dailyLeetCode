class Solution {
    public int findLatestStep(int[] arr, int m) {
            if (m == arr.length) {
                return m;
            }
            TreeSet<Integer> treeSet = new TreeSet<>();
            treeSet.add(0);
            treeSet.add(arr.length + 1);
            for (int i = arr.length - 1; i >= 0; i--) {
                int divIndex = arr[i];
                int lower = treeSet.lower(divIndex);
                int higher = treeSet.higher(divIndex);
                if (divIndex - lower - 1 == m || higher - divIndex - 1 == m) {
                    return i;
                } else {
                    treeSet.add(divIndex);
                }
            }
            return -1;
        }
}