class Solution {
    public int longestSubstring(String s, int k) {
        int[] count = new int[26];
        boolean[] isEnough = new boolean[26];
        char[] ch = s.toCharArray(); 
        for(char c:ch) if(++count[c-'a']>=k) isEnough[c-'a']=true;
        int l = 0,r=ch.length-1;
        while(l<r && !isEnough[ch[l]-'a'])l++;
        while(l<r && !isEnough[ch[r]-'a'])r--;
        for(int i=l;i<=r;i++){
            if(!isEnough[ch[i]-'a']) return Math.max(longestSubstring(s.substring(l,i),k),longestSubstring(s.substring(i+1,r+1),k));
        }
        return r-l+1;
    }
}