class StockSpanner {

    private Deque<Integer> stack;

    private ArrayList<Integer> array;

    public StockSpanner() {
        array = new ArrayList<Integer>();
        stack = new ArrayDeque<Integer>();
    }
    
    public int next(int price) {
        array.add(price);
        int index = array.size() - 1;
        while (!stack.isEmpty() && array.get(stack.peekLast()) <= price) {
            stack.pollLast();
        }
        int ans = stack.isEmpty() ? index + 1 : index - stack.peekLast();
        stack.addLast(index);
        return ans;
    }
}