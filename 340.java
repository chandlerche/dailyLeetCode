class Solution {
 2     public int lengthOfLongestSubstringKDistinct(String s, int k) {
 3         int max = 0;
 4         for(int i = 0; i < s.length(); i++) {
 5             for(int j = i + 1; j <= s.length(); j++) {
 6                 String sub = s.substring(i, j);
 7                 Set<Character> chars = new HashSet<>();
 8                 for(int t = i; t < j; t++) {
 9                     chars.add(s.charAt(t));
10                 }
11                 if(chars.size() <= k) {
12                     max = Math.max(max, sub.length());
13                 }
14             }
15         }
16         return max;
17 }
