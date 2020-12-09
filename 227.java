class Solution {
    public int calculate(String s) {
        char sign = '+';
        Stack<Integer> numStack = new Stack<>();
        int num = 0;
        int result = 0;
        for(int i = 0; i < s.length(); i++){
            char cur = s.charAt(i);
            if(cur >= '0'){
                num = num*10 - '0' + cur;
            }
            if((cur < '0' && cur !=' ' )|| i == s.length()-1){
                switch(sign){
                    case '+': numStack.push(num);break;
                    case '-': numStack.push(-num);break;
                    case '*': numStack.push(numStack.pop()*num);break;
                    case '/': numStack.push(numStack.pop()/num);break;
                }
                sign = cur;
                num = 0;
            }
        }
        while(!numStack.isEmpty()){
            result += numStack.pop();
        }
        return result;
    }
}