class Solution {
public:
    int lengthOfLongestSubstringTwoDistinct(string &s) {
        // Write your code here
        unordered_map<char,int> mpp;
        int i = 0 , j = 0 ;
        set<char> st;
        int ans = INT_MIN;
        while(1){
            if(i >= s.length() or j >= s.length()) break;
            char curr = s[j];
            mpp[curr]++;
            st.insert(curr);
            if(st.size() <= 2){
                ans = max(ans , j - i + 1);
                ++j;
                continue;
            }
            while(st.size() > 2){
                char ati = s[i];
                ++i;
                mpp[ati]--;
                if(mpp[ati] == 0){
                    st.erase(st.find(ati));
                }
                if(st.size() <= 2){
                    ans = max(ans , j - i + 1)  ;
                    ++j ;
                    break;
                }
            }
        }
        if(ans == INT_MIN) return 0; 
        return ans ;
    }
};