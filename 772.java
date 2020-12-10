class Solution {
    public int calculate(String s) {
        if (s == null) return 0;
        Queue<Character> queue = new LinkedList<>();
        for (char c : s.toCharArray()) {
            if (c != ' ')
                queue.offer(c);
        }
        queue.offer('#');
        return helper(queue);
    }
    int helper(Queue<Character> q) {
        int prev = 0, num = 0, sum = 0;
        char prevOp = '+';
        while (!q.isEmpty()) {
            char c = q.poll();
            if (Character.isDigit(c)) {
                num = num * 10 + c - '0';
            } else if (c == '(') {
                num = helper(q);
            } else {
                switch(prevOp) {
                    case '+':
                        sum += prev;
                        prev = num;
                        break;
                    case '-':
                        sum += prev;
                        prev = -num;
                        break;
                    case '*':
                        prev *= num;
                        break;
                    case '/':
                        prev /= num;
                        break;
                }
                 
                if(c == ')') break;
                prevOp = c;
                num = 0;
            }
        }
        return prev + sum;
    }
}