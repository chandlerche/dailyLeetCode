class Solution {
    public boolean parseBoolExpr(String expression) {
        Stack<Character> op = new Stack<>();
        String temp = "";
        for(int i = 0; i < expression.length(); i++){
            char c = expression.charAt(i);
            if(c == ')'){
                while(op.peek() != '('){
                    temp = op.pop() + temp;
                }
                op.pop();
                char operation = op.pop();
                op.push(isBool(temp, operation));
                temp = "";
            } else if(c != ','){
                op.push(c);
            }
        }
        if(op.peek() == 't'){
            return true;
        }
        return false;
    }
    public char isBool(String s, char op){
        if(op == '!'){
            if(s.equals("f")){
                return 't';
            }else{
                return 'f';
            }
        }else if(op == '|'){
            if(s.indexOf('t') != -1){
                return 't';
            }else{
                return 'f';
            }
        }else if(op == '&'){
            if(s.indexOf('f') != -1){
                return 'f';
            }else{
                return 't';
            }
        }
        return 'f';
    }
}