const int MAXV=1001;
int show_t[MAXV];
const int MAXN=50;
int cnt[MAXN];
const int MAXM=10;
int sum[1<<MAXM];
bool dp[MAXN][1<<MAXM];
class Solution {
public:
    bool canDistribute(vector<int>& nums, vector<int>& quantity) {
        memset(show_t,0,sizeof(show_t));
        for (int i:nums)
            ++show_t[i];
        memset(cnt,0,sizeof(cnt));
        int cnt_size=0;
        for (int i=1;i<MAXV;++i)
            if (show_t[i]!=0)
            {
                cnt[cnt_size]=show_t[i];
                ++cnt_size;
            }
        int quantity_size=quantity.size();
        int ALL=(1<<quantity_size)-1;
        memset(sum,0,sizeof(sum));
        for (int i=1;i<=ALL;++i)
        {
            int cur=i;
            int idx=0;
            while (cur!=0)
            {
                if ((cur&1)!=0)
                    sum[i]+=quantity.at(idx);
                cur>>=1;
                ++idx;
            }
        }
        memset(dp,false,sizeof(dp));
        for (int i=0;i<cnt_size;++i)
            dp[i][0]=true;
        for (int j=1;j<=ALL;++j)
            if (cnt[0]>=sum[j])
                dp[0][j]=true;
        for (int i=1;i<cnt_size;++i)
            for (int j=1;j<=ALL;++j)
            {
                if (dp[i-1][j])
                {
                    dp[i][j]=true;
                    continue;
                }
                int subset=j;
                do
                {
                    if (subset==0)
                        break;
                    int complements=(~subset)&j;
                    if (dp[i-1][complements] && cnt[i]>=sum[subset])
                    {
                        dp[i][j]=true;
                        break;
                    }
                    subset=(subset-1)&j;
                }while(subset!=j);
            }
        return dp[cnt_size-1][ALL];
    }
};