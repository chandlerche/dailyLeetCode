/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public int[] nextLargerNodes(ListNode head) {
        ListNode node = head;
        List<Integer> list = new ArrayList<>();
        while (node != null) {
            list.add(node.val);
            node = node.next;
        }
        int size = list.size();
        int[] res = new int[size];
        Stack<Integer> stack = new Stack<>();
        for (int i = size - 1; i >= 0; i--) {
            Integer cur = list.get(i);
            // 将小于cur的元素全部pop掉，栈中只留严格大于cur的元素
            while (!stack.isEmpty() && stack.peek() <= cur) {
                stack.pop();
            }
            res[i] = stack.isEmpty() ? 0 : stack.peek();
            stack.push(cur);
        }
        return res;
    }
}