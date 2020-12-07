class Solution {
    public String simplifyPath(String path) {
        List<String> list = Arrays.asList("",".","..");
        Deque<String> deque = new ArrayDeque<>();
        for (String s : path.split("/")) {
            if (!list.contains(s)){
                deque.add(s);
            }else if (!deque.isEmpty() && s.equals("..")){
                deque.pollLast();
            }
        }
        return "/" + String.join("/", deque);
    }
}