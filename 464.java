class Solution {
    public boolean canIWin(int maxChoosableInteger, int desiredTotal) 
    {
        int sum=0;
        for(int i=1;i<=maxChoosableInteger;i++)
            sum+=i;
        if(sum<desiredTotal)
            return false;
        Map<Integer,Boolean> map=new HashMap<>();
        return canWin(maxChoosableInteger,desiredTotal,0,map);
    }
    
    public boolean canWin(int chooseable,int nowTarget,int used,Map<Integer,Boolean> map)
    {
        if(map.containsKey(used))
            return map.get(used);
        for(int i=1;i<=chooseable;i++)
        {
            if((used & (1<<i))==0)
            {
                if(nowTarget<=i || !canWin(chooseable,nowTarget-i,used | (1<<i),map))
                {
                    map.put(used,true);
                    return true;
                }
            }
        }
        map.put(used,false);
        return false;
    }
}