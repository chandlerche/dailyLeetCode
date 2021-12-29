class Solution {
public:
    int longestWPI(vector<int>& hours) {
        int res=0;
        stack<int> s;
        s.push(0);
        vector<int> sum(hours.size()+1);
        for(int i=0;i<hours.size();i++){
            sum[i+1]=hours[i]>8?sum[i]+1:sum[i]-1;
            if(s.empty()||sum[s.top()]>sum[i+1]) s.push(i+1);
        }
        for(int i=sum.size()-1;i>=0;i--){
            while(s.size()&&sum[i]>sum[s.top()]){
                res=max(res,i-s.top());
                s.pop();
            }
        }
        return res;
    }
};