class Solution {
public:
    vector<int> sortItems(int n, int m, vector<int>& group, vector<vector<int>>& beforeItems) {
        int count = m;
        vector<int> ans;
        unordered_map<int,vector<int>> g2i;
        for(int i=0;i<n;++i){
            if(group[i]==-1){
                group[i] = count;
                g2i[count].push_back(i);
                ++count;
            }
            else{
                g2i[group[i]].push_back(i);
            }
        }

        vector<int> indegree_group(count,0);
        vector<unordered_set<int>> G_group(count);
        vector<vector<int>> G_item(n);
        vector<int> indegree_item(group.size(),0);

        //构造项目的图
        for(int i=0;i<beforeItems.size();++i){
            if(beforeItems[i].size()==0) continue;
            else{
                indegree_item[i] += beforeItems[i].size();
                for(int j=0;j<beforeItems[i].size();++j){
                    if(group[i] == group[beforeItems[i][j]]){
                        G_item[beforeItems[i][j]].push_back(i);
                    }
                    else{
                        G_item[beforeItems[i][j]].push_back(i);
                        if(G_group[group[beforeItems[i][j]]].find(group[i])==G_group[group[beforeItems[i][j]]].end()){
                            G_group[group[beforeItems[i][j]]].insert(group[i]);
                            ++indegree_group[group[i]];
                        }
                    }
                }
            }
        }

        queue<int> group_q;

        for(int i=0;i<indegree_group.size();++i){
            if(indegree_group[i]==0)
                group_q.push(i);
        }
       
        while(!group_q.empty()){
            int gu = group_q.front();
            group_q.pop();
            //cout << gu << endl;
            //对组内进行排序
            queue<int> item_q;
            for(int i=0;i<g2i[gu].size();++i){
                if(indegree_item[g2i[gu][i]]==0){
                    item_q.push(g2i[gu][i]);
                }
            }
            while(!item_q.empty()){
                
                int iu = item_q.front();
                //cout << iu << endl;
                item_q.pop();
                ans.push_back(iu);
                for(int i=0;i<G_item[iu].size();++i){
                    --indegree_item[G_item[iu][i]];
                    if(indegree_item[G_item[iu][i]]==0&&group[G_item[iu][i]]==gu)
                        item_q.push(G_item[iu][i]);
                }
            }
            //对组进行排序
            for(auto it=G_group[gu].begin();it!=G_group[gu].end();++it){
                --indegree_group[*it];
                if(indegree_group[*it] == 0)
                    group_q.push(*it);
            }
        }
        //cout << ans.size() << endl;
        if(ans.size()==n) return ans;
        else{
            ans.clear();
            return ans;
        }

    }
};