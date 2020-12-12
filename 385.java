class Solution {
    public NestedInteger deserialize(String s) {
        if(s.charAt(0)!='[') {
            return new NestedInteger(Integer.valueOf(s));
        }
        else {
            return deserialize1(s.substring(1));
        }
    }

    public NestedInteger deserialize1(String s) {
        NestedInteger res = new NestedInteger();
        for(int i=0;i<s.length();i++) {
            char c = s.charAt(i);
            if(c>='0'&&c<='9'||c=='-') {
                int n = 0; int flag = 1;
                for(;i<s.length();i++) {
                    c = s.charAt(i);
                    if(c>='0'&&c<='9') {
                        n = n*10 + c-'0';
                    } else if(c=='-'){
                        flag = -1;
                    } else {
                        i = i-1;
                        break;
                    }
                }
                res.add(new NestedInteger(flag*n));
            }
            else if(c=='[') {
                int index = i;
                int counter = 0;
                for(;i<s.length();i++) {
                    c = s.charAt(i);
                    if(c=='[') counter++;
                    else if(c==']') counter--;
                    if(counter==0) {
                        res.add(deserialize1(s.substring(index+1,i)));
                        break;
                    }
                }
            }
        }
        return res;
    }
}