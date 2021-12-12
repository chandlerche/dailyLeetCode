class Solution {
public:
    int mctFromLeafValues(vector<int>& arr) {
        int res = 0;
        stack<int> s;
        s.push(INT_MAX);
        int n = arr.size();
        for (auto& a : arr) {
            while (s.top() <= a) {
                int temp = s.top();
                s.pop();
                res += temp * min(s.top(), a);
            }
            s.push(a);
        }
        while (s.size() > 2) {
            int temp = s.top();
            s.pop();
            res += temp * s.top();
        }
        return res;
    }
};