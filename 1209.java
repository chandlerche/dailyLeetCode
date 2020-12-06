class Solution {
    public String removeDuplicates(String s, int k) {
        boolean flag = false;
        StringBuilder str = new StringBuilder();
        int index = 0;
        while(index < s.length())
        {
        	if(index+k <= s.length() ){
                boolean mark = true;
                for(int i = index+1; i < index+k ; i ++)
                    if(s.charAt(i) != s.charAt(index))
                    {
                        mark = false;
                        break;
                    }
                if(mark == true)
                {
                    flag = true;
        		    index+=k;
        		    continue;
                }
        	}
        	str.append(s.charAt(index));
        	index++;
        }
        if(flag == false)
            return new String(str);
        return removeDuplicates(new String(str),k);
    }
}